# Timeline & Daftar Tugas Proyek - CocoaIntelliGuard

Dokumen ini memuat estimasi waktu, daftar tugas (*task list*), timeline, serta rencana pelaporan untuk menyelesaikan proyek PKM-KC **CocoaIntelliGuard** sampai alat berfungsi penuh.

---

## ⏱️ Estimasi Waktu Penyelesaian
Berdasarkan sisa pekerjaan fisik dan integrasi sistem, estimasi waktu yang dibutuhkan sampai alat selesai dan berfungsi adalah **4 hingga 6 minggu** (bekerja secara paralel dalam tim).

---

## 📋 Daftar Tugas (Task List) Sampai Alat Jadi

### A. Rekayasa Perangkat Keras (Hardware) - Penanggung Jawab: Anggota Tim 4
1. [ ] **Pengadaan Komponen**: Membeli modul charger TP4056, baterai Li-Po 3.7V, saklar switch, layar TFT LCD 1.44" SPI, dan resistor sesuai justifikasi anggaran.
2. [ ] **Cetak Casing 3D**: Mengirim file desain 3D CocoaIntelliGuard (dimensi 15x8x4 cm) ke jasa 3D printing.
3. [ ] **Fabrikasi PCB Custom**: Menguji sirkuit pada prototipe breadboard, lalu mencetak PCB custom (dana kampus).
4. [ ] **Assembly**: Merakit ESP32-CAM, baterai, LCD, dan PCB ke dalam casing 3D.

### B. Pemrograman Firmware (ESP32-CAM) - Penanggung Jawab: Anggota Tim 1 & Anggota Tim 2
1. [ ] **Setup Library TFLite Micro**: Mengonfigurasi Arduino IDE agar mendukung *TensorFlow Lite for Microcontrollers*.
2. [ ] **Integrasi Model TFLite**: Memasukkan file C++ array `models/cacao_model_data.h` ke dalam kode program C++ (firmware ESP32-CAM).
3. [ ] **Pemrosesan Citra Lokal**: Menulis kode untuk mengambil foto dari kamera, mengubah resolusi ke 224x224, melakukan inferensi model secara lokal di ESP32-CAM, dan menampilkan hasil serta tingkat keyakinan (confidence score) di layar LCD.
4. [ ] **Komunikasi Nirkabel (Wi-Fi/Internet)**: Menulis fungsi pengunggahan data hasil deteksi ke Firebase Cloud.

### C. Integrasi Cloud & Dashboard - Penanggung Jawab: Anggota Tim 2 & Anggota Tim 3
1. [ ] **Setup Firebase**: Mengonfigurasi Realtime Database / Firestore di Firebase.
2. [ ] **Pembuatan Dashboard Web**: Membuat web sederhana (HTML/JS) untuk menampilkan riwayat deteksi hama, lokasi, dan rekomendasi penanganan berdasarkan data Firebase.

### D. Pengujian & Kalibrasi Lapangan - Penanggung Jawab: Anggota Tim 5
1. [ ] **Uji Fungsionalitas Dasar**: Menguji daya tahan baterai, kejelasan tangkapan kamera, dan kestabilan koneksi Wi-Fi.
2. [ ] **Uji Akurasi Lapangan**: Menguji pembacaan alat secara langsung pada tanaman kakao sehat dan sakit di lapangan (dibandingkan dengan diagnosis manual ahli).
3. [ ] **Survei Petani**: Meminta feedback dari petani/pengguna mengenai kemudahan genggaman dan pembacaan alat.

---

## 📅 Timeline Kegiatan (Sisa 6 Minggu)

| Minggu | Kegiatan Utama | Luaran / Output |
|---|---|---|
| **Minggu 1** | Pengadaan komponen fisik & Penyusunan sirkuit pada breadboard. | Komponen lengkap & skema sirkuit teruji. |
| **Minggu 2** | Cetak casing 3D, pembuatan PCB, dan Setup program dasar ESP32-CAM. | Casing fisik jadi & kamera aktif. |
| **Minggu 3** | Integrasi `models/cacao_model_data.h` ke firmware ESP32-CAM + Output ke Layar LCD. | Alat bisa mendeteksi secara lokal (luring). |
| **Minggu 4** | Setup database Firebase & Pembuatan Dashboard Web pemantau. | Data deteksi terkirim ke cloud secara *real-time*. |
| **Minggu 5** | Perakitan final ke casing (*Assembly*) & Pengujian Lapangan (lokasi uji lapangan). | Prototipe final teruji akurasinya. |
| **Minggu 6** | Evaluasi hasil pengujian, pengisian akun media sosial, & Penyusunan Laporan Akhir. | Laporan akhir siap & publikasi luaran. |

---

## 🤝 Rencana Pertemuan & Laporan Perkembangan Mingguan
Gunakan rencana ini untuk bahan diskusi/laporan internal tim dengan Dosen Pendamping (Dosen Pendamping):

1. **Pertemuan 1 (Mulai Minggu 1)**: 
   * *Yang dilaporkan*: Keberhasilan model AI 5-kelas (Akurasi 91%) dan ukuran TFLite 2.4 MB.
   * *Tujuan*: Menunjukkan kesiapan otak AI dan memvalidasi skema sirkuit sebelum cetak PCB.
2. **Pertemuan 2 (Minggu 2)**:
   * *Yang dilaporkan*: Hasil cetak casing 3D dan sirkuit awal.
   * *Tujuan*: Aligning desain fisik alat agar nyaman digenggam sesuai spesifikasi.
3. **Pertemuan 3 (Minggu 3)**:
   * *Yang dilaporkan*: Demo alat melakukan klasifikasi lokal (mengarahkan ESP32-CAM ke gambar contoh dan hasilnya muncul di LCD).
   * *Tujuan*: Membuktikan kemampuan *Edge AI Processing* (luring) berhasil.
4. **Pertemuan 4 (Minggu 4)**:
   * *Yang dilaporkan*: Integrasi Wi-Fi dan sinkronisasi data ke dashboard web.
   * *Tujuan*: Memvalidasi fungsi *Cloud Predictive* berjalan.
5. **Pertemuan 5 (Minggu 5)**:
   * *Yang dilaporkan*: Hasil akurasi pengujian di lapangan dan feedback petani.
   * *Tujuan*: Menguji ketangguhan alat di bawah sinar matahari/kondisi kebun sebenarnya.
6. **Pertemuan 6 (Minggu 6)**:
   * *Yang dilaporkan*: Draft Laporan Akhir, Artikel Ilmiah, dan akun media sosial (Luaran PKM).
   * *Tujuan*: Finalisasi administrasi PKM untuk persiapan PIMNAS.
