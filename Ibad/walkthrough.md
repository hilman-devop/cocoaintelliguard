# Walkthrough - Penyelesaian Firmware Lokal & Web Dashboard CocoaIntelliGuard

Kami telah berhasil menyelesaikan penulisan firmware offline/lokal untuk ESP32-CAM serta membangun dashboard pemantau berbasis web yang estetik dan terintegrasi dengan Firebase secara real-time.

---

## Perubahan yang Diterapkan 🛠️

### 1. Integrasi Layar TFT LCD 1.44" SPI
* Mengonfigurasi modul driver ST7735 menggunakan **Software SPI** pada pin MicroSD bebas:
  * **CLK** -> GPIO 14
  * **SDA** -> GPIO 13
  * **CS** -> GPIO 15
  * **DC** -> GPIO 2
  * **RST** -> GPIO 12
* Menambahkan inisialisasi LCD dengan skema warna dan startup screen khusus yang menampilkan teks **COCOA INTELLIGUARD** saat alat pertama kali dinyalakan.

### 2. Akuisisi & Pemrosesan Citra Lokal
* Mengubah konfigurasi kamera menjadi format raw `PIXFORMAT_RGB565` pada resolusi QVGA (320x240).
* Menulis fungsi `process_image` yang bertugas:
  * Memotong bagian tengah gambar (*center crop*) sebesar `240x240` agar rasio aspek tetap simetris (mencegah distorsi).
  * Melakukan penyusutan ukuran gambar (*nearest-neighbor resizing*) menjadi `224x224` piksel.
  * Mengekstrak nilai warna R, G, B dan mengisi float buffer model TFLite Micro secara dinamis.

### 3. Tampilan Hasil Deteksi Dinamis
* Menulis fungsi `display_result` untuk memperbarui antarmuka LCD setiap kali inferensi model selesai (setiap 3 detik).
* Teks kelas diagnosis (e.g., `Kakao Sehat` dengan warna hijau, atau penyakit lain dengan warna merah) dan confidence score (warna kuning) akan menampilkan ukuran teks dinamis untuk menghindari teks terpotong.

### 4. Integrasi Wi-Fi & Firebase di ESP32-CAM
* Menambahkan opsionalitas Wi-Fi dan pengiriman data Firebase menggunakan pustaka `Firebase ESP32 Client` (dikendalikan via saklar makro `#define ENABLE_CLOUD false` di file [main.ino](file:///c:/TheGame/Money/PKM/Ibad/src/main.ino) sehingga bisa diaktifkan/dimatikan dengan mudah).

### 5. Web Dashboard Pemantau Premium (Glassmorphism UI)
* Menerapkan desain gelap premium dengan efek Glassmorphism (`backdrop-filter`) di berkas [style.css](file:///c:/TheGame/Money/PKM/Ibad/dashboard/style.css).
* Menggunakan **Chart.js** untuk merender grafik tren mingguan dan **Leaflet.js** untuk peta sebaran kebun di berkas [app.js](file:///c:/TheGame/Money/PKM/Ibad/dashboard/app.js).
* Menyediakan fitur simulasi luring real-time (Demo Mode) ketika Firebase tidak terhubung agar dashboard tetap berfungsi interaktif saat di-load di browser.

---

## Screenshot Hasil Pengujian Dashboard 📷

````carousel
![Tampilan Dashboard Awal](C:\Users\Elz\.gemini\antigravity-ide\brain\8aeb1e66-ae21-47d5-bfa6-1a859f1cc5d1\dashboard_loaded_1783448929453.png)
<!-- slide -->
![Tampilan Dashboard Setelah Simulasi Dijalankan](C:\Users\Elz\.gemini\antigravity-ide\brain\8aeb1e66-ae21-47d5-bfa6-1a859f1cc5d1\dashboard_verified_1783449017009.png)
````

---

## Berkas yang Diperbarui & Ditambahkan 📂

* **[main.ino](file:///c:/TheGame/Money/PKM/Ibad/src/main.ino)**: Kode program Arduino C++ utama untuk ESP32-CAM (Ditambahkan fitur cloud opsional).
* **[platformio.ini](file:///c:/TheGame/Money/PKM/Ibad/platformio.ini)**: Konfigurasi compiler PlatformIO untuk mendownload libraries otomatis.
* **[index.html](file:///c:/TheGame/Money/PKM/Ibad/dashboard/index.html)**: Struktur HTML5 Dashboard.
* **[style.css](file:///c:/TheGame/Money/PKM/Ibad/dashboard/style.css)**: Gaya styling Glassmorphism UI.
* **[app.js](file:///c:/TheGame/Money/PKM/Ibad/dashboard/app.js)**: Logika simulasi real-time, grafik, dan Leaflet map.
* **[task.md](file:///c:/Users/Elz/.gemini/antigravity-ide/brain/8aeb1e66-ae21-47d5-bfa6-1a859f1cc5d1/task.md)**: Daftar tugas pengerjaan yang semuanya telah selesai ditandai.
* **[estimasi_anggaran.md](file:///c:/TheGame/Money/PKM/Ibad/docs/estimasi_anggaran.md)**: Dokumen estimasi rencana anggaran biaya (RAB) proyek total.

---

## Langkah Verifikasi Selanjutnya Menggunakan VS Code + PlatformIO 🖥️

Kita telah menyediakan berkas [platformio.ini](file:///c:/TheGame/Money/PKM/Ibad/platformio.ini) di root proyek. Jadi, kamu tidak perlu mengunduh pustaka secara manual lagi!

1. Buka folder proyek ini di **VS Code**.
2. Instal ekstensi **PlatformIO IDE** dari Extension Marketplace VS Code.
3. PlatformIO akan mengunduh semua pustaka yang dibutuhkan (`Adafruit GFX`, `Adafruit ST7735`, `Firebase ESP32 Client`, dan `TensorFlow Lite Micro` khusus ESP32).
4. Sambungkan board ESP32-CAM ke laptop menggunakan modul USB-to-TTL.
5. Klik ikon **PlatformIO** (logo semut) di sidebar kiri VS Code:
   * Klik **Build** untuk melakukan kompilasi kode secara otomatis.
   * Klik **Upload** untuk mengunggah program ke ESP32-CAM.
   * Klik **Monitor** untuk membuka Serial Monitor (baud rate 115200) untuk melihat logs diagnosa.
6. Untuk membuka Web Dashboard: Buka file [index.html](file:///c:/TheGame/Money/PKM/Ibad/dashboard/index.html) langsung di browser Chrome/Firefox kamu.
