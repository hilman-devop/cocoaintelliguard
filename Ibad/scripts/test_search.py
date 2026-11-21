from roboflow import Roboflow

try:
    rf = Roboflow(api_key="ROBOFLOW_API_KEY_DISINI")
    # Coba akses workspace cacao
    workspace = rf.workspace("cacao")
    print("[SUCCESS] Berhasil mengakses workspace 'cacao'")
    projects = workspace.projects()
    for p in projects:
        print(f"  - {p}")
except Exception as e:
    print(f"[ERROR] Gagal: {e}")
