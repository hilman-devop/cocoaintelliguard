import os
import time
from roboflow import Roboflow

max_retries = 3
for attempt in range(1, max_retries + 1):
    try:
        print(f"[INFO] Mencoba mengunduh dataset (Percobaan {attempt}/{max_retries})...")
        rf = Roboflow(api_key="ROBOFLOW_API_KEY_DISINI")
        project = rf.workspace("rahmayani").project("penyakit-fmvt8")
        print("[SUCCESS] Berhasil mengakses proyek 'penyakit-fmvt8'")
        
        dataset = project.version(1).download("yolov8")
        print(f"[SUCCESS] Dataset terunduh ke: {dataset.location}")
        break
    except Exception as e:
        print(f"[WARNING] Percobaan {attempt} gagal: {e}")
        if attempt < max_retries:
            print("[INFO] Menunggu 5 detik sebelum mencoba lagi...")
            time.sleep(5)
        else:
            print("[ERROR] Semua percobaan gagal. Silakan periksa koneksi internet.")

