from roboflow import Roboflow

try:
    rf = Roboflow(api_key="ROBOFLOW_API_KEY_DISINI")
    project = rf.workspace("data-hamzah").project("terserang-vsd-daun-kakao")
    print(f"[SUCCESS] Berhasil mengakses proyek 'terserang-vsd-daun-kakao'")
    # Download versi 2
    dataset = project.version(2).download("yolov8")
    print(f"[SUCCESS] Dataset terunduh ke: {dataset.location}")
except Exception as e:
    print(f"[ERROR] Gagal mengunduh: {e}")
