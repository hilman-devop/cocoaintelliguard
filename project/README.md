# CocoaIntelliGuard - PKM-KC 2026

Proyek Karsa Cipta (PKM-KC) dari Perguruan Tinggi untuk mendeteksi penyakit buah dan daun kakao menggunakan perangkat portable berbasis **ESP32-CAM** dengan kemampuan **Edge AI Processing (Offline)** dan terintegrasi dengan **Web Dashboard Pemantau (Cloud)**.

---

## 📁 Struktur Workspace yang Rapi

* `dashboard/` - Kode program Web Dashboard pemantau (HTML, CSS, JS, Chart.js, Leaflet.js).
* `dataset/` - Folder penyimpanan citra kakao terklasifikasi untuk training (sehat, busuk buah, vsd, kanker batang).
* `design-system/` - File panduan UI/UX Pro Max (`MASTER.md`).
* `docs/` - Dokumen pendukung proyek (Proposal PDF, draf laporan kemajuan, timeline, memory pengembangan, changelog, estimasi anggaran).
* `src/` - Kode program utama ESP32-CAM luring & daring (`main.ino`).
* `models/` - Folder penyimpanan output model (`cacao_model.tflite` dan format saved model Keras).
* `raw_data/` - Folder dataset mentah yang diunduh langsung dari Roboflow.
* `scripts/` - Skrip Python pembantu:
  * `scripts/download.py` & `scripts/download_vsd.py` & `scripts/download_canker.py` - Pengunduh dataset Roboflow.
  * `scripts/crop_dataset.py`, `scripts/crop_vsd.py`, `scripts/crop_canker.py` - Pemotong gambar berdasarkan anotasi YOLO.
* `platformio.ini` - Konfigurasi PlatformIO IDE untuk compile & upload program ke ESP32-CAM.
* `train.py` - Skrip utama untuk melatih model MobileNetV2 (Transfer Learning) dan mengonversinya ke format TFLite.

---

## 🛠️ Persyaratan Lingkungan (Environment)

### 1. Model AI Training (Python)
Proyek ini memerlukan Python versi stabil yang didukung TensorFlow (**Python 3.12** sangat direkomendasikan).
```bash
pip install tensorflow roboflow matplotlib pillow
```

### 2. Compile & Upload Firmware
Direkomendasikan menggunakan **VS Code** dengan ekstensi **PlatformIO IDE**. PlatformIO akan membaca [platformio.ini](./platformio.ini) dan menginstal pustaka C++ berikut secara otomatis:
* `Adafruit GFX Library`
* `Adafruit ST7735 and ST7789 Library`
* `Firebase ESP32 Client`
* `TensorFlowLite_ESP32`

---

## 🚀 Alur Penggunaan & Uji Coba

### 1. Pelatihan Model AI Lokal
1. **Unduh & Potong Dataset**:
   ```bash
   python scripts/download.py
   python scripts/download_vsd.py
   python scripts/download_canker.py
   python scripts/crop_dataset.py
   python scripts/crop_vsd.py
   python scripts/crop_canker.py
   ```
2. **Latih Model**:
   ```bash
   python train.py
   ```
3. **Konversi ke Header C++**:
   ```bash
   python scripts/convert_to_header.py
   ```

### 2. Flashing ESP32-CAM (Offline & Online Mode)
1. Buka folder root proyek ini di **VS Code** dengan ekstensi PlatformIO terpasang.
2. Sambungkan ESP32-CAM ke laptop menggunakan modul FTDI (USB-to-TTL).
3. Jika ingin mengaktifkan sinkronisasi database cloud: Ubah `#define ENABLE_CLOUD` menjadi `true` di [main.ino](./src/main.ino) dan sesuaikan kredensial Wi-Fi serta Firebase Anda.
4. Klik tombol **Build** ($\checkmark$) lalu **Upload** ($\rightarrow$) di status bar bagian bawah VS Code.

### 3. Membuka Dashboard Pemantau
Buka file **[dashboard/index.html](./dashboard/index.html)** langsung di browser web Anda.
* Dashboard secara otomatis menggunakan **Demo Mode** (simulasi real-time) untuk demonstrasi antarmuka.
* Jika Firebase Anda sudah aktif, dashboard akan mendengarkan data deteksi asli dari kebun secara real-time.
