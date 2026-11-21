import os
from roboflow import Roboflow

print("[INFO] Mengunduh dataset dari Roboflow (format yolov8)...")
rf = Roboflow(api_key="ROBOFLOW_API_KEY_DISINI")
project = rf.workspace("itera-zghl1").project("tugas-akhir-hama-penyakit-kakao")
dataset = project.version(1).download("yolov8")
print("[SUCCESS] Unduhan selesai! Lokasi dataset:", dataset.location)
