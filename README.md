# CocoaIntelliGuard

![Python](https://img.shields.io/badge/Python-2f81f7?style=flat) ![Computer Vision](https://img.shields.io/badge/Computer_Vision-2f81f7?style=flat) ![Edge AI](https://img.shields.io/badge/Edge_AI-2f81f7?style=flat) ![Roboflow](https://img.shields.io/badge/Roboflow-2f81f7?style=flat)

> Eksperimen deteksi penyakit kakao dari dataset, preprocessing, pencarian data, dan evaluasi model.

## Tentang proyek

Eksperimen deteksi penyakit kakao dari dataset, preprocessing, pencarian data, dan evaluasi model. Dokumentasi ini dibuat sebagai panduan singkat untuk memahami ruang lingkup proyek, menjalankannya secara lokal, dan membaca batasan penggunaannya.

## Fitur utama

- Pipeline download dan preprocessing dataset
- Eksperimen pencarian serta validasi data
- Struktur script terpisah untuk eksperimen
- Dirancang agar model dapat dibawa ke perangkat edge

## Teknologi

- Python
- Computer Vision
- Edge AI
- Roboflow

## Menjalankan secara lokal

Prasyarat dan konfigurasi dapat berbeda menurut sistem operasi. Contoh langkah utama:

```bash
pip install -r requirements.txt
python Ibad/scripts/preprocess.py
```

## Struktur dan pengembangan

Mulai dari entry point dan folder konfigurasi proyek. Pisahkan credential lokal dari source code, tambahkan test untuk perubahan penting, dan gunakan environment variable untuk konfigurasi deployment.

## Keamanan

- Jangan commit API key, password, token, session ID, atau data pribadi.
- Gunakan file environment lokal dan contoh konfigurasi tanpa nilai rahasia.
- Uji perubahan pada environment development sebelum deployment.

## Status

Proyek ini merupakan bagian dari portofolio **Hilman Arifin Ilham** dan dapat dikembangkan sesuai kebutuhan penggunaan.

> **Catatan:** API key dataset harus disediakan melalui environment variable atau konfigurasi lokal. Jangan menaruh credential di source code.

## Lisensi

Belum ada lisensi open-source yang dinyatakan di repository ini. Hubungi pemilik repository sebelum menggunakan ulang atau mendistribusikan kode.

---

Dibuat oleh [Hilman Arifin Ilham](https://github.com/hilman-devop).
