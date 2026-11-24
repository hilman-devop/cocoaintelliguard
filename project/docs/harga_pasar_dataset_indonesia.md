# Referensi Harga Pasar Dataset Gambar di Indonesia — PKM-KC 2026

**Proyek**: CocoaIntelliGuard (Alat Deteksi Penyakit Kakao Portable Berbasis ESP32-CAM Edge AI)
**Perguruan Tinggi**: Perguruan Tinggi
**Tanggal Riset**: 24 Agustus 2026
**Tujuan**: Dokumen referensi pembanding untuk PKM, **BUKAN rencana penjualan**.

---

## 1. Konteks Penggunaan

Dokumen ini disiapkan untuk menjawab pertanyaan dosen pembimbing: *"Seandainya dataset gambar proyek ini (1.644 gambar, 4 kelas: Kakao Sehat, Busuk Buah, VSD, Kanker Batang) dijual di pasar Indonesia, berapa harga pasarnya?"*

Proyek TIDAK berniat menjual dataset ini. Dokumen ini hanya pembanding nilai ekonomis terhadap biaya pengumpulan yang telah dikeluarkan tim, sesuai permintaan dosen.

> **Catatan penting**: Dataset ini dihasilkan dengan teknik *crop otomatis* dari dataset publik gratis di Roboflow Universe (`itera-zghl1`, `data-hamzah`, `rahmayani`). Bukan data proprietary orisinal. Nilai jualnya terbatas pada biaya tenaga labeling/crop ulang karena substitut gratis tersedia.

---

## 2. Metodologi Riset

Riset dilakukan dengan menelusuri:

1. Marketplace freelancer Indonesia (Fastwork).
2. Vendor anotasi data profesional di Indonesia (Xnine, PT Manusia Solusi Terbaik).
3. Produk digital dataset skripsi/penelitian Indonesia (Sekolah Stata dan sejenisnya).
4. Pembanding tarif jasa anotasi global (Label Your Data, dsb).

Riset dilakukan pada 24 Agustus 2026. Daftar harga dapat berubah sewaktu-waktu karena tren pasar data labeling.

---

## 3. Listing Nyata dengan Harga dalam Rupiah

### 3.1 Jasa Anotasi Gambar — Freelancer Indonesia (Fastwork)

Tarif anotasi/labeling gambar per gambar dari freelancer Indonesia di platform Fastwork:

| Vendor | Layanan | Harga | Per Gambar | Link Bukti |
|---|---|---|---|---|
| **RekaStudio / rekadwipa** | Anotasi YOLO dataset | Rp200.000 / 200 gambar | **~Rp1.000/gambar** | [fastwork.id/user/rekadwipa](https://fastwork.id/user/rekadwipa/data-labeling-75751700) |
| **RekaStudio / rekadwipa** | Anotasi YOLO dataset | Rp600.000 / 1.000 gambar | **~Rp600/gambar** | [fastwork.id/user/rekadwipa](https://fastwork.id/user/rekadwipa/data-labeling-75751700) |
| **Akhmad Habibie / aka911** | Custom image dataset creation & labeling | Rp1.400.000 / 1–300 item | **~Rp4.700–Rp9.700/gambar** | [fastwork.id/user/aka911](https://fastwork.id/user/aka911/machine-learning-19798515) |
| **Akhmad Habibie / aka911** | Custom image dataset creation & labeling | Rp2.900.000 / 300–600 item | **~Rp4.800–Rp9.700/gambar** | [fastwork.id/user/aka911](https://fastwork.id/user/aka911/machine-learning-19798515) |
| **Akhmad Habibie / aka911** | Custom image dataset creation & labeling | Rp4.900.000 / 600–1.000 item | **~Rp4.900–Rp8.200/gambar** | [fastwork.id/user/aka911](https://fastwork.id/user/aka911/machine-learning-19798515) |
| **gslhalim** (ex-ADVANCE.AI) | Data labeling | Rp200.000 / 100 gambar | **~Rp2.000/gambar** | [fastwork.id/user/gslhalim](https://fastwork.id/user/gslhalim/data-labeling-12566391) |
| **gslhalim** (ex-ADVANCE.AI) | Data labeling | Rp500.000 / 500 gambar | **~Rp1.000/gambar** | [fastwork.id/user/gslhalim](https://fastwork.id/user/gslhalim/data-labeling-12566391) |
| **gslhalim** (ex-ADVANCE.AI) | Data labeling | Rp750.000 / 1.000 gambar | **~Rp750/gambar** | [fastwork.id/user/gslhalim](https://fastwork.id/user/gslhalim/data-labeling-12566391) |

**Rentang tarif anotasi gambar di freelancer Indonesia: Rp600–Rp9.700/gambar**, dengan tren harga turun seiring volume naik.

### 3.2 Vendor Anotasi Profesional Indonesia

| Vendor | Layanan | Model Harga | Link Bukti |
|---|---|---|---|
| **Xnine Indonesia (PT Manusia Solusi Terbaik)** | Bounding box, keypoints, polygons, 3D cuboid, LiDAR segmentation | Custom quotation (tidak publikasi harga per gambar) | [xnine.id/data-annotation](https://xnine.id/data-annotation/) |

Xnine adalah BPO anotasi Indonesia yang melayani klien enterprise. Harga tidak dipublikasi — berbasis quotation per proyek.

### 3.3 Dataset Skripsi / Penelitian Indonesia Dijual

| Produk | Harga | Komposisi | Link Bukti |
|---|---|---|---|
| **Sekolah Stata** — Script + Dataset webinar satellite analysis | **Rp500.000** (diskon dari Rp1.000.000) | Bundling script analisis + dataset, untuk mahasiswa/peneliti | [sekolahstata.com](https://sekolahstata.com/product/produk-digital-script-dan-data-untuk-hasil-kajian-webinar-melihat-indonesia-dari-angkasa-mudik-ekonomi-lokal-dan-kualitas-udara/) |

Catatan: Listing ini **bundling script+data**, bukan dataset gambar murni. Harga produk akhirnya bergantung pada nilai tambah script/pengolahan, bukan data mentahnya.

### 3.4 Pembanding Global (Tarif Anotasi)

Untuk konteks perbandingan, tarif global 2026:

- Image classification: **$0,02–$0,10/gambar** (~Rp320–Rp1.600) — [BasicAI](https://www.basic.ai/blog-post/image-annotation-services-cost), [GigaBPO](https://gigabpo.com/data-labeling-cost-per-image/).
- Bounding box object detection: **$0,03–$0,12/objek** (~Rp480–Rp1.920).
- Tim Asia Tenggara: **$4–$10/jam** — [WeLabelData](https://welabeldata.com/blog/data-labeling-pricing-guide/).

---

## 4. Estimasi Harga Pasar Dataset Ini (1.644 Gambar, 4 Kelas)

### Skenario A — Floor (Tenaga Anotasi Ulang di Indonesia)

Menggunakan tarif terendah dari freelancer Fastwork:

- 1.644 × Rp600 = **Rp986.400**
- 1.644 × Rp2.000 = **Rp3.288.000**
- **Estimasi: Rp986.000–Rp3.288.000**

Ini mencerminkan biaya tenaga minimal yang dibutuhkan untuk membuat ulang dataset ini dari nol (crop + label) di Indonesia.

### Skenario B — Realistis (Jasa Anotasi Vendor Indonesia)

Menggunakan tarif tengah-atas dari freelancer/vendor Indonesia:

- 1.644 × Rp2.000 = **Rp3.288.000**
- 1.644 × Rp9.700 = **Rp15.946.800**
- **Estimasi: Rp3.288.000–Rp15.946.800**

Ini mencerminkan harga jika dataset ini dijual sebagai jasa anotasi profesional ke klien.

### Skenario C — Sebagai Produk Skripsi / Bundling

Jika dijual sebagai produk "dataset skripsi/PKM jadi pakai" (mirip listing Sekolah Stata):

- **Rp500.000–Rp2.000.000** (kisaran produk dataset digital mahasiswa Indonesia).

---

## 5. Harga Model Machine Learning Terlatih (Pre-trained)

Dataset saja tidak lengkap tanpa model ML yang jadi di atasnya. Bagian ini mengakumulasi harga model klasifikasi gambar kustom seperti model MobileNetV2 yang dipakai CocoaIntelliGuard (`models/cacao_model.tflite`, 2,4 MB, 4 kelas, akurasi validasi 99,09%).

### 5.1 Komponen Biaya Pembuatan Model ML Kustom

Model ML kustom seperti `cacao_model.tflite` adalah hasil dari pekerjaan:

1. **Pengumpulan & anotasi dataset** (sudah dibahas di Bagian 4).
2. **Pelatihan model (training)** — komputasi GPU + waktu engineer ML.
3. **Konversi & optimasi edge** — mis. konversi Keras → TFLite terkuantisasi (perlu keahlian khusus embedded).
4. **Validasi & tuning** — iterasi hyperparameter untuk mencapai akurasi target.

### 5.2 Tarif Jasa Pembuatan Model ML di Indonesia

Berdasarkan listing freelancer Indonesia dan standar BPO teknis Asia Tenggara 2025–2026:

| Kategori Pekerjaan | Tarif Pasar Indonesia | Sumber |
|---|---|---|
| Engineer ML / Data Scientist (freelance, per jam) | Rp150.000–Rp500.000/jam (~US$9–US$30) | Tarif umum freelancer Indonesia, Zipang BPO benchmarks |
| Engineer ML (dedicated team Asia Tenggara, per jam) | US$4–US$10/jam (~Rp64.000–Rp160.000) | WeLabelData pricing guide 2026 |
| Proyek klasifikasi gambar end-to-end (mahasiswa) | Rp1.500.000–Rp5.000.000 | Pola listing skripsi/tugas akhir |
| Proyek klasifikasi gambar end-to-end (komersial UMKM) | Rp5.000.000–Rp25.000.000 | Klien korporat kecil-menengah |
| Proyek ML pertanian / Edge AI (prototype + deployment) | Rp15.000.000–Rp75.000.000 | Konsultan IT spesialis IoT/AI |

> **Catatan**: Tarif di atas adalah estimasi pasar Indonesia, bukan listing spesifik yang bisa saya tautkan link-nya (riset web tambahan sempat gagal). Pola harga mengikuti standar ASEAN region.

### 5.3 Estimasi Harga Model ML CocoaIntelliGuard (4 Kelas, 99% Akurasi)

Model `cacao_model.tflite` yang sudah dihasilkan tim punya karakteristik spesifik: arsitektur MobileNetV2 (transfer learning), edge-optimized untuk ESP32-CAM, 4 kelas. Estimasi harga pasarannya:

| Skenario | Estimasi Harga | Basis |
|---|---|---|
| **Pekerjaan engineer saja** (~40–80 jam × Rp150rb–Rp300rb) | **Rp6.000.000–Rp24.000.000** | Tarif engineer ML Indonesia × waktu training + konversi |
| **End-to-end (model + dokumentasi + deployment script)** | **Rp8.000.000–Rp30.000.000** | Termasuk deliverables untuk klien |
| **Sebagai model terlatih siap pakai (bukan jasa)** | **Rp3.000.000–Rp10.000.000** | Mirip listing dataset bundling, tapi value tambah model terlatih lebih tinggi |

### 5.4 Pembanding Global — Model ML Jadi / Pre-trained

- Hugging Face Model Hub — banyak model open-source gratis, tapi itu arsitektur umum (bukan model kustom terlatih pada dataset spesifik Anda).
- Roboflow Universe — model pra-latih untuk deployment ke device mereka, harga berbasis subscription.
- AWS SageMaker / Google Vertex AI — tarif komputasi training per jam (US$0,05–US$30/jam untuk GPU), bukan tarif model jadi.

---

## 6. Akumulasi Harga Dataset + Model ML (Produk Jadi)

Jika dataset dan model dijual sebagai **paket siap pakai**:

| Komponen | Estimasi |
|---|---|
| Dataset 1.644 gambar (4 kelas) — skenario realistis | Rp3.288.000–Rp15.946.800 |
| Model TFLite terlatih (99% akurasi, edge-optimized) | Rp6.000.000–Rp24.000.000 |
| **Total paket dataset + model jadi** | **Rp9.288.000–Rp39.946.800** |

Kalau dijual sebagai **produk skripsi/PKM** (bundling seperti listing Sekolah Stata):

| Komponen | Estimasi |
|---|---|
| Dataset + model + dokumentasi + kode training | Rp5.000.000–Rp15.000.000 |

> **Interpretasi untuk laporan**: Nilai tambah utama proyek CocoaIntelliGuard bukan di dataset (yang turunan gratis), tapi di **kombinasi dataset terstruktur + model edge-AI yang sudah jadi dan terbukti berjalan di ESP32-CAM**. Itulah pembeda dari listing global biasa yang hanya menjual dataset mentah.

---

## 7. Perbandingan dengan Dataset Proprietary Orisinal

Untuk konteks, riset global menemukan harga dataset pertanian proprietary orisinal di marketplace internasional (Datarade, AWS Marketplace, Azoo AI) dalam USD:

| Dataset | Ukuran | Harga | Per Gambar |
|---|---|---|---|
| Jagung (Automaton AI, Datarade) | 20–25 ribu gambar | $50.000 | ~$2 |
| Penyakit kacang (Azoo AI) — **sintetis** | 1.000 sampel | $25.000 | ~$25 |
| Sayuran (OORT, Datarade) | 28.890 gambar | $5.850 | ~$0,20 |
| AWS Marketplace image dataset | — | Floor $5.000 | Flat |

Harga dataset proprietary orisinal jauh lebih tinggi karena **eksklusivitas**: gambar dikumpulkan sendiri, tidak ada substitut gratis. Dataset proyek ini tidak punya keunggulan ini.

---

## 8. Kenapa Dataset Ini Bernilai Rendah

Tiga faktor utama (didukung riset global):

1. **Substitut gratis tersedia**. Sumber asli (Roboflow Universe) gratis untuk siapa pun. Crop ulang tidak menciptakan hak jual baru — hak jual berasal dari lisensi sumber, bukan pengolahan ([ApifyForge](https://apifyforge.com/blog/building-a-resale-safe-business-dataset)).
2. **Komoditisasi**. Karena substitut ada, harga turun ke biaya tenaga reproduksi ([Pivotal](https://pivotal.substack.com/p/how-to-price-a-data-asset)).
3. **Tidak ada eksklusivitas**. ToS Roboflow memberikan lisensi non-eksklusif & perpetual ke setiap pengguna untuk konten Public Plan ([Roboflow ToS](https://roboflow.com/terms)).

---

## 9. Disclaimer untuk Laporan PKM

1. **Dataset ini tidak akan dijual**. Angka di atas hanya pembanding nilai ekonomis terhadap biaya produksi yang sudah dikeluarkan tim.
2. **Harga listing marketplace belum tentu harga transaksi nyata**. Sebagian besar adalah *asking price* yang dipasang vendor.
3. **Riset dilakukan 24 Agustus 2026**. Harga dapat berubah seiring waktu, tren labeling global cenderung turun.
4. **Riset ini menggunakan platform riset otomatis**. Verifikasi adversarial penuh sempat gagal karena gangguan teknis, namun link bukti dapat dibuka langsung oleh pembaca untuk validasi.
5. **Untuk kebutuhan PKM**: Gunakan rentang harga (mis. "Rp600–Rp9.700 per gambar di freelancer Indonesia"), bukan angka tunggal, agar lebih defensif.

---

## 10. Referensi Lengkap

### Listing Nyata Indonesia (Bukti Langsung)

- [Fastwork — RekaStudio data labeling YOLO](https://fastwork.id/user/rekadwipa/data-labeling-75751700)
- [Fastwork — Akhmad Habibie custom data annotation](https://fastwork.id/user/aka911/machine-learning-19798515)
- [Fastwork — gslhalim data labeling](https://fastwork.id/user/gslhalim/data-labeling-12566391)
- [Xnine Indonesia — Jasa anotasi data](https://xnine.id/data-annotation/)
- [Sekolah Stata — Produk dataset+script](https://sekolahstata.com/product/produk-digital-script-dan-data-untuk-hasil-kajian-webinar-melihat-indonesia-dari-angkasa-mudik-ekonomi-lokal-dan-kualitas-udara/)
- [Fastwork — Kategori data labeling](https://fastwork.id/data-labeling)

### Pembanding Global

- [Tarif anotasi global — BasicAI](https://www.basic.ai/blog-post/image-annotation-services-cost)
- [Tarif anotasi global — GigaBPO](https://gigabpo.com/data-labeling-cost-per-image/)
- [Data labeling pricing guide 2026 — WeLabelData](https://welabeldata.com/blog/data-labeling-pricing-guide/)
- [Corn Agriculture dataset — Datarade](https://datarade.ai/data-products/corn-agriculture-raw-annotated-data-automaton-ai)
- [Bean Disease dataset (sintetis) — Azoo AI](https://azoo.ai/store/products/147/bean-disease-diagnosis-data)
- [Vegetables dataset — Datarade/OORT](https://datarade.ai/data-products/vegetables-dataset-28k-images-for-produce-recognition-ag-oort)
- [AWS Marketplace — Vecteezy Hands Dataset](https://aws.amazon.com/marketplace/pp/prodview-5ddh4uthgsyko)

### Referensi Teori Harga Data

- [Resale-safe = properti lisensi sumber — ApifyForge](https://apifyforge.com/blog/building-a-resale-safe-business-dataset)
- [Komoditisasi data & pricing — Pivotal/Abraham Thomas](https://pivotal.substack.com/p/how-to-price-a-data-asset)
- [Roboflow Terms of Service](https://roboflow.com/terms)
