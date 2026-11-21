# CocoaIntelliGuard — Deteksi Penyakit Kakao Edge AI

> Sistem deteksi penyakit buah dan daun kakao berbasis ESP32-CAM dengan inferensi offline di perangkat dan dashboard pemantau.

## ✨ Fitur

- Inferensi TFLite on-device (MobileNetV2)
- Pipeline pelatihan model di Python
- Dashboard pemantau (Chart.js + Leaflet)
- Kalibrasi dan preprocessing dataset
- Diajukan sebagai PKM-Karsa Cipta 2026

## 🛠 Tech Stack

"ESP32-CAM" "TensorFlow Lite" "MobileNetV2" "PlatformIO" "Python" "Chart.js"

## 🚀 Menjalankan

```
pip install -r requirements.txt   # pipeline dataset
# buka Ibad/ dengan PlatformIO untuk firmware
python train.py
```

## 📌 Catatan

Proyek ini merupakan bagian dari portofolio pribadi. Kode disusun untuk kebutuhan nyata,
bukan sekadar demo, sehingga sebagian konfigurasi spesifik lingkungan mungkin perlu
disesuaikan sebelum dijalankan.
