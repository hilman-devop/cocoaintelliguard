# Memory Proyek - CocoaIntelliGuard (PKM-KC 2026)

Dokumen ini mencatat keputusan teknis, konfigurasi lingkungan, kredensial, dan status pengembangan saat ini sebagai referensi memori pengembangan.

## ⚙️ Lingkungan Pengembangan & dependensi
* **Versi Python**: Python 3.12 (PENTING: Jangan gunakan Python 3.14 karena TensorFlow belum menyediakannya secara resmi).
* **Dependensi Utama**: `tensorflow`, `roboflow`, `matplotlib`, `pillow`.
* **Platform Target**: ESP32-CAM (Edge AI lokal & Cloud prediction).
* **PlatformIO Environment**: Menggunakan compiler VS Code PlatformIO IDE dengan file [platformio.ini](../platformio.ini) untuk auto-install dependensi C++ (`Adafruit GFX`, `Adafruit ST7735`, `Firebase ESP32 Client`, dan `TensorFlow Lite Micro`).

## 🔑 Kredensial & Sumber Dataset Roboflow
* **Private API Key**: `ROBOFLOW_API_KEY_DISINI`
* **Public API Key**: `rf_kCIZb1hJRsPH5Hh6zMjzJAQ6rQ03`
* **Dataset Asal**:
  1. `itera-zghl1/tugas-akhir-hama-penyakit-kakao` (Versi 1) - Untuk kelas `sehat` & `busuk_buah`
  2. `data-hamzah/terserang-vsd-daun-kakao` (Versi 2) - Untuk kelas `vsd`
  3. `rahmayani/penyakit-fmvt8` (Versi 1) - Untuk kelas `kanker_batang`

## 📊 Status Dataset Saat Ini
Dataset asli didekripsi dan digabung sehingga menghasilkan total **1.644 gambar hasil potong**:
* `dataset/sehat/` - Berisi foto buah kakao sehat.
* `dataset/busuk_buah/` - Berisi foto buah kakao yang terserang busuk buah (*Black Pod*).
* `dataset/vsd/` - Berisi 483 foto daun kakao terserang VSD (diunduh dari proyek Data Hamzah).
* `dataset/kanker_batang/` - Berisi 55 foto kanker batang kakao (diambil dan dipotong dari dataset Roboflow `penyakit-fmvt8` oleh Rahmayani).

## 🤖 Detail Model AI
* **Arsitektur**: MobileNetV2 (dengan weights `imagenet` yang dibekukan untuk transfer learning cepat).
* **Input Resolusi**: `224x224` piksel RGB.
* **Epoch Latihan**: 5 Epoch (Model dilatih ulang dengan 4 kelas aktif sesuai target proposal: busuk_buah, kanker_batang, sehat, vsd).
* **Model Terkuantisasi**: `models/cacao_model.tflite` berukuran **2.4 MB** (Optimasi standard kuantisasi dinamis).
* **Array Header C++**: `models/cacao_model_data.h` (dibuat menggunakan `convert_to_header.py`).

## 🖥️ Web Dashboard Pemantau
* **Lokasi**: [dashboard/](../dashboard/)
* **Teknologi**: HTML5, Vanilla CSS (Glassmorphism UI), Javascript, Chart.js, Leaflet.js.
* **UI/UX Standar**: Fira Code & Fira Sans fonts, inline SVG icons (Lucide-based) untuk kejelasan visual data analitik.
* **Mode Firebase & Demo**: Secara default berjalan dalam *Demo Mode* (simulasi data) jika URL database tidak diubah, namun otomatis sinkron saat Firebase Database SDK diaktifkan.

## 🔮 Rencana Pengembangan & Langkah Berikutnya
1. **Pemasangan Firmware**: Membuka folder proyek di VS Code dengan ekstensi PlatformIO terpasang. PlatformIO akan otomatis membaca berkas [platformio.ini](../platformio.ini) dan mengunduh pustaka C++.
2. **Koneksi Wi-Fi & Firebase**: Mengubah nilai `#define ENABLE_CLOUD` menjadi `true` di berkas [main.ino](../src/main.ino) dan melengkapi kredensial Wi-Fi & Firebase Host untuk pengujian di kebun nyata.
3. **Penyusunan Berkas Laporan**: Menyalin data hasil latihan akurasi model (99.09%) dan diagram sistem untuk diserahkan ke Simbelmawa melalui [draft_laporan_kemajuan.md](../docs/draft_laporan_kemajuan.md).
