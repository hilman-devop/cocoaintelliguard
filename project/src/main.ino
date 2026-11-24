/*
 * CocoaIntelliGuard - Firmware ESP32-CAM
 * PKM-KC 2026 - Perguruan Tinggi
 * 
 * Kodingan ini merupakan kerangka dasar untuk me-load model AI cacao_model.tflite
 * menggunakan TensorFlow Lite for Microcontrollers, mengambil gambar dari kamera OV2640,
 * dan melakukan inferensi klasifikasi penyakit kakao secara lokal.
 */

#include "esp_camera.h"
#include "Arduino.h"
#include "cacao_model_data.h" // File header model yang sudah kita buat

// Jalankan instalasi pustaka: TensorFlowLite_ESP32 melalui Library Manager Arduino
#include "tensorflow/lite/micro/micro_mutable_op_resolver.h"
#include "tensorflow/lite/micro/micro_interpreter.h"
#include "tensorflow/lite/schema/schema_generated.h"
#include "tensorflow/lite/micro/micro_error_reporter.h"

// Pustaka layar LCD TFT ST7735
#include <Adafruit_GFX.h>    // Core graphics library
#include <Adafruit_ST7735.h> // Hardware-specific library for ST7735
#include <SPI.h>

// SAKLAR KOMUNIKASI CLOUD (Set ke true jika ingin mengaktifkan Wi-Fi & Firebase)
#define ENABLE_CLOUD false

#if ENABLE_CLOUD
  #include <WiFi.h>
  #include <FirebaseESP32.h>
  
  #define WIFI_SSID "NAMA_WIFI_KAMU"
  #define WIFI_PASSWORD "PASSWORD_WIFI_KAMU"
  #define FIREBASE_HOST "your-project-default-rtdb.firebaseio.com"
  #define FIREBASE_AUTH "DATABASE_SECRET_TOKEN"
  
  FirebaseData firebaseData;
  FirebaseConfig firebaseConfig;
  FirebaseAuth firebaseAuth;
#endif

// Pin kamera untuk modul ESP32-CAM AI-Thinker
#define PWDN_GPIO_NUM     32
#define RESET_GPIO_NUM    -1
#define XCLK_GPIO_NUM      0
#define SIOD_GPIO_NUM     26
#define SIOC_GPIO_NUM     27
#define Y9_GPIO_NUM       35
#define Y8_GPIO_NUM       34
#define Y7_GPIO_NUM       39
#define Y6_GPIO_NUM       36
#define Y5_GPIO_NUM       21
#define Y4_GPIO_NUM       19
#define Y3_GPIO_NUM       18
#define Y2_GPIO_NUM        5
#define VSYNC_GPIO_NUM    25
#define HREF_GPIO_NUM     23
#define PCLK_GPIO_NUM     22

// Pin untuk TFT LCD ST7735 1.44" SPI (Software SPI untuk hemat pin & bebas konflik)
#define TFT_CS    15
#define TFT_DC     2
#define TFT_MOSI 13
#define TFT_SCLK 14
#define TFT_RST  12

Adafruit_ST7735 tft = Adafruit_ST7735(TFT_CS, TFT_DC, TFT_MOSI, TFT_SCLK, TFT_RST);

// TFLite Global variables
const tflite::Model* model = nullptr;
tflite::MicroInterpreter* interpreter = nullptr;
TfLiteTensor* input = nullptr;
TfLiteTensor* output = nullptr;

// Alokasi memori tensor arena (3MB area pSRAM)
constexpr int kTensorArenaSize = 3 * 1024 * 1024;
byte* tensor_arena = nullptr;

// Daftar kelas penyakit kakao sesuai indeks alfabetis model 4-kelas kita
const char* class_names[] = {
  "Busuk Buah",
  "Kanker Batang",
  "Kakao Sehat",
  "VSD"
};

void setup_camera() {
  camera_config_t config;
  config.pin_d0 = Y2_GPIO_NUM;
  config.pin_d1 = Y3_GPIO_NUM;
  config.pin_d2 = Y4_GPIO_NUM;
  config.pin_d3 = Y5_GPIO_NUM;
  config.pin_d4 = Y6_GPIO_NUM;
  config.pin_d5 = Y7_GPIO_NUM;
  config.pin_d6 = Y8_GPIO_NUM;
  config.pin_d7 = Y9_GPIO_NUM;
  config.pin_xclk = XCLK_GPIO_NUM;
  config.pin_pclk = PCLK_GPIO_NUM;
  config.pin_vsync = VSYNC_GPIO_NUM;
  config.pin_href = HREF_GPIO_NUM;
  config.pin_sccb_sda = SIOD_GPIO_NUM;
  config.pin_sccb_scl = SIOC_GPIO_NUM;
  config.pin_pwdn = PWDN_GPIO_NUM;
  config.pin_reset = RESET_GPIO_NUM;
  config.xclk_freq_hz = 20000000;
  config.ledc_timer = LEDC_TIMER_0;
  config.ledc_channel = LEDC_CHANNEL_0;
  
  // Menggunakan RGB565 agar pemrosesan & resizing piksel lokal lebih mudah
  config.pixel_format = PIXFORMAT_RGB565;
  config.frame_size = FRAMESIZE_QVGA; // QVGA (320x240)
  config.fb_count = 1;

  // Inisialisasi kamera
  esp_err_t err = esp_camera_init(&config);
  if (err != ESP_OK) {
    Serial.printf("Kamera gagal diinisialisasi: 0x%x\n", err);
    tft.setCursor(15, 110);
    tft.setTextColor(ST7735_RED);
    tft.print("Cam Init Fail!");
    return;
  }
  Serial.println("Kamera siap!");
  tft.setCursor(15, 80);
  tft.setTextColor(ST7735_GREEN);
  tft.print("Kamera: OK");
}

void setup_tflite() {
  model = tflite::GetModel(g_cacao_model_data);
  if (model->version() != TFLITE_SCHEMA_VERSION) {
    Serial.println("Versi skema model tidak cocok!");
    tft.setCursor(15, 110);
    tft.setTextColor(ST7735_RED);
    tft.print("Model Version Err!");
    return;
  }

  tensor_arena = (byte*)ps_malloc(kTensorArenaSize);
  if (!tensor_arena) {
    Serial.println("Gagal mengalokasikan pSRAM untuk Tensor Arena!");
    tft.setCursor(15, 110);
    tft.setTextColor(ST7735_RED);
    tft.print("pSRAM Allocation Fail!");
    return;
  }

  static tflite::MicroMutableOpResolver<10> micro_op_resolver;
  micro_op_resolver.AddConv2D();
  micro_op_resolver.AddDepthwiseConv2D();
  micro_op_resolver.AddReshape();
  micro_op_resolver.AddFullyConnected();
  micro_op_resolver.AddSoftmax();
  micro_op_resolver.AddAveragePool2D();

  static tflite::MicroErrorReporter micro_error_reporter;
  static tflite::MicroInterpreter static_interpreter(
      model, micro_op_resolver, tensor_arena, kTensorArenaSize, &micro_error_reporter, nullptr, nullptr);
  interpreter = &static_interpreter;

  if (interpreter->AllocateTensors() != kTfLiteOk) {
    Serial.println("Gagal mengalokasikan memori tensor!");
    tft.setCursor(15, 110);
    tft.setTextColor(ST7735_RED);
    tft.print("Tensor Alloc Fail!");
    return;
  }

  input = interpreter->input(0);
  output = interpreter->output(0);
  Serial.println("TensorFlow Lite Micro siap!");
  tft.setCursor(15, 95);
  tft.setTextColor(ST7735_GREEN);
  tft.print("TFLite: OK");
}

void display_result(const char* class_name, float confidence) {
  tft.fillScreen(ST7735_BLACK);
  
  // Header bar hijau premium
  tft.fillRect(0, 0, 128, 20, ST7735_GREEN);
  tft.setCursor(12, 6);
  tft.setTextColor(ST7735_BLACK);
  tft.setTextSize(1);
  tft.print("IntelliGuard AI");
  
  // Label Diagnosis
  tft.setTextColor(ST7735_WHITE);
  tft.setCursor(10, 32);
  tft.print("DIAGNOSIS:");
  
  // Diagnosis Text (Skala dinamis agar tidak kepotong)
  tft.setCursor(10, 48);
  if (strcmp(class_name, "Kakao Sehat") == 0) {
    tft.setTextColor(ST7735_GREEN);
  } else {
    tft.setTextColor(ST7735_RED);
  }
  
  if (strlen(class_name) > 11) {
    tft.setTextSize(1);
  } else {
    tft.setTextSize(2);
  }
  tft.print(class_name);
  
  // Label Confidence
  tft.setTextColor(ST7735_WHITE);
  tft.setTextSize(1);
  tft.setCursor(10, 80);
  tft.print("CONFIDENCE:");
  
  // Confidence Score
  tft.setCursor(10, 95);
  tft.setTextSize(2);
  tft.setTextColor(ST7735_YELLOW);
  tft.print(confidence * 100, 1);
  tft.print("%");
}

// Fungsi memotong bagian tengah (crop 240x240 dari 320x240) dan mengecilkan ke 224x224
void process_image(camera_fb_t* fb) {
  if (fb->format != PIXFORMAT_RGB565) {
    Serial.println("Format gambar salah! Harus RGB565.");
    return;
  }

  for (int ty = 0; ty < 224; ty++) {
    for (int tx = 0; tx < 224; tx++) {
      // Potong bagian tengah secara horizontal (mulai dari kolom ke-40)
      int sx = 40 + (tx * 240) / 224;
      int sy = (ty * 240) / 224;
      
      int pixel_idx = (sy * 320 + sx) * 2;
      uint8_t hb = fb->buf[pixel_idx];
      uint8_t lb = fb->buf[pixel_idx + 1];
      uint16_t pixel = (hb << 8) | lb;
      
      // Ekstrak komponen R, G, B dari format RGB565 (5-6-5 bits) dan skala ke 0-255
      uint8_t r = ((pixel >> 11) & 0x1F) * 255 / 31;
      uint8_t g = ((pixel >> 5) & 0x3F) * 255 / 63;
      uint8_t b = (pixel & 0x1F) * 255 / 31;
      
      // Masukkan ke float buffer model (Model Keras kita memiliki layer rescaling di awal)
      int tensor_idx = (ty * 224 + tx) * 3;
      input->data.f[tensor_idx]     = (float)r;
      input->data.f[tensor_idx + 1] = (float)g;
      input->data.f[tensor_idx + 2] = (float)b;
    }
  }
}

void setup() {
  Serial.begin(115200);
  
  // Mengaktifkan pSRAM untuk penampung memori besar
  psramInit();
  
  // Inisialisasi Layar LCD
  tft.initR(INITR_144GREENTAB);
  tft.fillScreen(ST7735_BLACK);
  tft.setRotation(1);
  
  // Tampilkan Startup Screen premium
  tft.drawRect(5, 5, 118, 118, ST7735_GREEN);
  tft.setCursor(15, 20);
  tft.setTextColor(ST7735_GREEN);
  tft.setTextSize(1);
  tft.print("COCOA");
  tft.setCursor(15, 35);
  tft.setTextSize(2);
  tft.setTextColor(ST7735_WHITE);
  tft.print("INTELLI");
  tft.setCursor(15, 55);
  tft.print("GUARD");
  
  setup_camera();
  setup_tflite();

#if ENABLE_CLOUD
  tft.fillRect(6, 110, 116, 12, ST7735_BLACK);
  tft.setCursor(15, 112);
  tft.setTextSize(1);
  tft.setTextColor(ST7735_YELLOW);
  tft.print("Connecting Wi-Fi...");
  
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  int wifi_timeout = 0;
  while (WiFi.status() != WL_CONNECTED && wifi_timeout < 15) {
    delay(500);
    Serial.print(".");
    wifi_timeout++;
  }
  
  if (WiFi.status() == WL_CONNECTED) {
    Serial.println("\nTerkoneksi ke Wi-Fi!");
    tft.fillRect(6, 110, 116, 12, ST7735_BLACK);
    tft.setCursor(15, 112);
    tft.setTextColor(ST7735_GREEN);
    tft.print("Wi-Fi Connected!");
    
    // Inisialisasi Firebase
    firebaseConfig.host = FIREBASE_HOST;
    firebaseConfig.signer.tokens.legacy_token = FIREBASE_AUTH;
    Firebase.begin(&firebaseConfig, &firebaseAuth);
    Firebase.reconnectWiFi(true);
  } else {
    Serial.println("\nWi-Fi tidak terhubung. Masuk ke mode offline.");
    tft.fillRect(6, 110, 116, 12, ST7735_BLACK);
    tft.setCursor(15, 112);
    tft.setTextColor(ST7735_RED);
    tft.print("Offline Mode");
  }
#endif
  
  delay(1500); // Tahan tampilan loading sebentar
}

void loop() {
  camera_fb_t* fb = esp_camera_fb_get();
  if (!fb) {
    Serial.println("Gagal mengambil gambar dari kamera");
    tft.fillRect(0, 110, 128, 18, ST7735_RED);
    tft.setCursor(4, 115);
    tft.setTextColor(ST7735_WHITE);
    tft.setTextSize(1);
    tft.print("Camera Err");
    delay(2000);
    return;
  }

  // Proses gambar & masukkan ke buffer input AI
  process_image(fb);

  Serial.println("Menjalankan inferensi model...");
  TfLiteStatus invoke_status = interpreter->Invoke();
  if (invoke_status != kTfLiteOk) {
    Serial.println("Gagal menjalankan inferensi!");
    tft.fillRect(0, 110, 128, 18, ST7735_RED);
    tft.setCursor(4, 115);
    tft.setTextColor(ST7735_WHITE);
    tft.setTextSize(1);
    tft.print("TFLite Invoke Err");
  } else {
    // Cari index dengan probabilitas tertinggi (4 kelas)
    int max_idx = 0;
    float max_val = 0.0;
    
    for (int i = 0; i < 4; i++) {
      float score = output->data.f[i];
      if (score > max_val) {
        max_val = score;
        max_idx = i;
      }
    }
    
    Serial.printf("Hasil Prediksi: %s dengan Confidence: %.2f%%\n", class_names[max_idx], max_val * 100);
    display_result(class_names[max_idx], max_val);

#if ENABLE_CLOUD
    if (WiFi.status() == WL_CONNECTED) {
      Serial.println("Mengirim data deteksi ke Firebase...");
      
      FirebaseJson json;
      json.set("diagnosis", class_names[max_idx]);
      json.set("confidence", max_val);
      json.set("timestamp", "/.info/serverTimeOffset");
      
      // Simulasi koordinat kebun kakao di sekitar lokasi uji lapangan
      json.set("latitude", 0.0 + (((float)random(0, 100) - 50.0f) / 50000.0f));
      json.set("longitude", 0.0 + (((float)random(0, 100) - 50.0f) / 50000.0f));

      if (Firebase.pushJSON(firebaseData, "/detections", json)) {
        Serial.println("Data terunggah ke Firebase!");
      } else {
        Serial.println("Gagal mengunggah data: " + firebaseData.errorReason());
      }
    }
#endif
  }

  esp_camera_fb_return(fb);
  delay(3000); // Inferensi ulang setiap 3 detik
}
