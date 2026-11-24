# Changelog - CocoaIntelliGuard Project

Semua perubahan dan perkembangan pada proyek PKM-KC ini dicatat di sini.

## [1.2.0] - 2026-07-08

### Added
* Membuat Web Dashboard pemantau kesehatan kebun kakao di folder `dashboard/` menggunakan **HTML5**, **Vanilla CSS (Glassmorphism)**, dan **Javascript**.
* Mengintegrasikan grafik data tren menggunakan **Chart.js** dan peta lokasi pohon terinfeksi luring interaktif menggunakan **Leaflet.js**.
* Menambahkan berkas konfigurasi **[platformio.ini](../platformio.ini)** di root proyek untuk mempermudah perakitan, build, dan flash firmware tanpa harus menggunakan Arduino IDE.
* Menambahkan pustaka `Firebase ESP32 Client` ke dalam PlatformIO dan kode konektivitas Wi-Fi serta pengiriman JSON data ke Realtime Database di [main.ino](../src/main.ino) (dikendalikan via `#define ENABLE_CLOUD false`).

### Changed
* Merancang ulang tampilan dashboard sesuai standar **UI/UX Pro Max**: Mengganti font bawaan menjadi **Fira Code** (headings & data) dan **Fira Sans** (body), serta mengganti seluruh emoji luring dengan **Inline SVG Icons** yang bersih dan profesional.
* Memperbaiki bug transisi `switchRec` di `dashboard/app.js` ketika dipanggil secara programatik saat halaman pertama kali dimuat.

## [1.1.0] - 2026-07-08

### Added
* Membuat skrip `download_canker.py` untuk mengunduh dataset Kanker Batang Kakao dari Roboflow (`penyakit-fmvt8` oleh Rahmayani).
* Membuat skrip `crop_canker.py` untuk mengekstrak dan memotong gambar berlabel `kanker batang kakao` (ID kelas 5) dari dataset tersebut ke `dataset/kanker_batang/` (berhasil mendapatkan 55 citra baru).
* Mengonversi model 4-kelas baru ke `.tflite` terkuantisasi (`models/cacao_model.tflite`) dan memperbarui C++ array header (`models/cacao_model_data.h`) menggunakan `convert_to_header.py`.

### Removed
* Menghapus kelas hama (`helopeltis` dan `penggerek_buah`) agar model AI hanya terfokus pada kelas yang diminta dalam proposal (Kanker Batang, VSD, Busuk Buah, dan Sehat).

### Changed
* Melatih kembali model MobileNetV2 dengan **4 kelas aktif**, berhasil meningkatkan akurasi validasi menjadi **99.09%** (Training: **98.56%**).

## [1.0.0] - 2026-07-07

### Added
* Membuat skrip `preprocess.py` untuk inisialisasi direktori dataset dan data augmentation menggunakan TensorFlow/Keras.
* Membuat skrip `download.py` & `download_vsd.py` untuk mengunduh dataset secara otomatis dari Roboflow menggunakan API Key pengguna.
* Membuat skrip `crop_dataset.py` & `crop_vsd.py` dengan algoritma parsing poligon YOLOv8 (format segmentasi) untuk memotong objek buah kakao secara otomatis ke dalam folder klasifikasi masing-masing.
* Membuat skrip `train.py` untuk pelatihan transfer learning menggunakan arsitektur MobileNetV2 dan otomatis mengonversi model menjadi format `.tflite` terkuantisasi (optimized for Edge AI).
* Model akhir `models/cacao_model.tflite` (2.4 MB) berhasil dilatih dengan akurasi validasi **91.01%** dengan 5 kelas aktif.
* Membuat skrip `convert_to_header.py` untuk mengubah model `.tflite` menjadi file C++ Header array `models/cacao_model_data.h` untuk Arduino IDE.
* Membuat kerangka kode Arduino C++ `src/main.ino` untuk memuat model TFLite Micro dan melakukan klasifikasi lokal dengan sensor kamera OV2640.

### Fixed
* Memperbaiki masalah `UnicodeEncodeError` pada terminal Windows dengan mengganti emoji cetak menjadi teks standar.
* Memperbaiki isu kompatibilitas TensorFlow yang tidak mendukung Python 3.14 dengan mengalihkan instalasi dependensi ke **Python 3.12**.
* Memperbaiki kesalahan parsing format download Roboflow dari `'folder'` ke `'yolov8'` agar kompatibel dengan proyek berjenis Object Detection/Segmentation.
* Memperbaiki masalah penyimpanan model di Keras 3 dengan mengganti `model.save()` menjadi `model.export()` guna mengekspor format `SavedModel` untuk konverter TFLite.
* Merapikan struktural direktori workspace menjadi folder terpisah: `dataset/`, `docs/`, `models/`, `raw_data/`, `scripts/`, dan `src/` serta memperbarui path file di seluruh skrip.
