# Draft Laporan Kemajuan - PKM-KC 2026

**Judul Proyek**: Alat Deteksi Penyakit Kakao Portable Berbasis ESP32-CAM Edge AI Processing dan Cloud Predictive Intelligence System (CocoaIntelliGuard)  
**Perguruan Tinggi**: Universitas Muhammadiyah Jember  
**Ketua Tim**: Ahmad Furqonul Ibad  
**Dosen Pendamping**: Iswahyudi, S.T., M.T.  

---

## Ringkasan Progres Utama (Capai Target: ~80%)
Hingga saat ini, proyek telah mencapai perkembangan yang sangat signifikan pada bagian **Kecerdasan Buatan (AI Model)**, **Pengembangan Firmware Lokal**, dan **Web Dashboard Pemantau Cloud**. Seluruh infrastruktur perangkat lunak (*software*) luring dan daring telah selesai dibangun dan diverifikasi secara fungsional.

---

## 1. Perkembangan Kegiatan yang Telah Dicapai

### A. Pengumpulan & Strukturisasi Dataset
* Tim telah berhasil mengumpulkan dan mengintegrasikan dataset dari Roboflow Universe dengan total **1.644 gambar** setelah melalui pemrosesan. Citra tersebut bersumber dari tiga dataset publik utama:
  1. **Dataset Kakao Sehat & Busuk Buah**: Diambil dari proyek Roboflow [tugas-akhir-hama-penyakit-kakao](https://universe.roboflow.com/itera-zghl1/tugas-akhir-hama-penyakit-kakao) oleh workspace `itera-zghl1` (Versi 1).
  2. **Dataset VSD (Vascular Streak Dieback)**: Diambil dari proyek Roboflow [terserang-vsd-daun-kakao](https://universe.roboflow.com/data-hamzah/terserang-vsd-daun-kakao) oleh workspace `data-hamzah` (Versi 2).
  3. **Dataset Kanker Batang**: Diambil dari proyek Roboflow [penyakit-fmvt8](https://universe.roboflow.com/rahmayani/penyakit-fmvt8) oleh workspace `rahmayani` (Versi 1).
* Skrip otomatis [crop_dataset.py](file:///c:/TheGame/Money/PKM/Ibad/scripts/crop_dataset.py), [crop_vsd.py](file:///c:/TheGame/Money/PKM/Ibad/scripts/crop_vsd.py), dan [crop_canker.py](file:///c:/TheGame/Money/PKM/Ibad/scripts/crop_canker.py) berhasil memisahkan citra objek penyakit dari format deteksi/segmentasi YOLO/YOLOv8 menjadi kelas klasifikasi:
  * Kakao Sehat (`sehat`): 668 gambar
  * Busuk Buah (`busuk_buah`): 438 gambar
  * Vascular Streak Dieback (`vsd`): 483 gambar
  * Kanker Batang (`kanker_batang`): 55 gambar

### B. Pelatihan Model CNN (Deep Learning)
* Pelatihan model menggunakan teknik *Transfer Learning* berbasis arsitektur **MobileNetV2** yang sangat optimal untuk komputasi tepi (*edge computing*).
* Model dilatih menggunakan skrip [train.py](file:///c:/TheGame/Money/PKM/Ibad/train.py) dengan pembagian data 80% latihan dan 20% validasi.
* **Hasil Akurasi**: Mencapai **98.56% (Training)** dan **99.09% (Validation)** pada epoch ke-5 dengan 4 kelas aktif (3 penyakit + 1 sehat). Hasil ini melampaui standar kelayakan PKM-KC (target awal $\ge$90%).

### C. Optimalisasi Edge AI (TensorFlow Lite)
* Model Keras yang besar berhasil dikonversi ke format **TensorFlow Lite terkuantisasi** ([cacao_model.tflite](file:///c:/TheGame/Money/PKM/Ibad/models/cacao_model.tflite)).
* Ukuran model berhasil dipangkas menjadi hanya **2.4 MB**, menjadikannya sangat ringan untuk dijalankan secara luring (*offline*) langsung di dalam memori internal mikrokontroler **ESP32-CAM**. Untuk kebutuhan pemrograman C++ di mikrokontroler, data biner ini juga telah diekspor menjadi array byte C++ di file [cacao_model_data.h](file:///c:/TheGame/Money/PKM/Ibad/models/cacao_model_data.h).

### D. Pengembangan Firmware Lokal & PlatformIO Workspace
* Menyusun kode program Arduino C++ utama pada [main.ino](file:///c:/TheGame/Money/PKM/Ibad/src/main.ino) dengan fitur:
  * Inisialisasi layar TFT LCD 1.44" ST7735 menggunakan software SPI (hemat pin & bebas konflik pembacaan kartu SD).
  * Pemrosesan citra dari kamera OV2640 ke format raw `PIXFORMAT_RGB565`.
  * Algoritma *Center Crop* (240x240) dan *Nearest-Neighbor Resizing* (224x224) untuk mencegah distorsi aspek rasio sebelum masuk ke tensor input model.
  * Normalisasi piksel float `[0,1]` ke dalam input buffer TFLite Micro.
* Migrasi pemrograman firmware ke lingkungan **VS Code + PlatformIO IDE** lewat [platformio.ini](file:///c:/TheGame/Money/PKM/Ibad/platformio.ini) untuk mempermudah compile/upload otomatis tanpa ketergantungan pada Arduino IDE.

### E. Pembangunan Dashboard Pemantau & Integrasi Cloud (Firebase)
* Menyiapkan opsi integrasi Wi-Fi dan pengiriman payload data JSON secara real-time ke Firebase Realtime Database (dikendalikan via saklar makro `#define ENABLE_CLOUD` di firmware).
* Membuat aplikasi **Web Dashboard Pemantau** luring/daring di direktori `dashboard/` menggunakan standar **UI/UX Pro Max** (Glassmorphism, Fira Code & Sans, Lucide-based inline SVG Icons). Web ini menampilkan:
  * Statistik ringkasan pemindaian total, sehat, sakit, dan akurasi model.
  * Grafik visualisasi sebaran tren deteksi harian/mingguan menggunakan **Chart.js**.
  * Peta geospasial sebaran infeksi di kebun menggunakan **Leaflet.js** (pusat koordinat di kebun Puslitkoka Jember).
  * Tab interaktif rekomendasi penanganan otomatis dan log riwayat pemindaian real-time.

---

## 2. Rencana Tahapan Berikutnya (Sisa Pekerjaan)

1. **Perakitan Perangkat Keras (Hardware Assembly)**:
   * Pembuatan sirkuit integrasi fisik ESP32-CAM dengan modul charger baterai TP4056 dan layar TFT LCD 1.44" ST7735 pada PCB custom.
   * Pencetakan casing fisik alat menggunakan teknologi *3D printing* berdimensi 15x8x4 cm.
2. **Koneksi Firebase Asli**:
   * Melakukan migrasi data dari Demo Mode (simulasi) di dashboard ke Firebase Realtime Database asli milik tim untuk uji coba sinkronisasi luring-daring di lapangan.
3. **Uji Coba & Kalibrasi Lapangan**:
   * Pengujian akurasi deteksi langsung di kebun kakao lokal Jember/Puslitkoka Jember untuk mengukur interferensi cahaya luar terhadap performa pembacaan model Edge AI.

---

## 3. Justifikasi Anggaran Belanja Terpakai
* **Belanja Bahan (Komponen Elektronik & Sensor)**: Telah dipesan untuk kebutuhan perakitan awal (ESP32-CAM, baterai, LCD, modul charger, PCB).
* **Biaya Langganan Software & Pihak Ketiga**: Digunakan untuk akses API Roboflow dan Cloud Database pendukung serta pencetakan casing 3D.
