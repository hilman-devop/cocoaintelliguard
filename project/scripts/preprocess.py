import os
import sys

# ponytail: simple local folder structure setup, integration with Roboflow API can be configured by user
def setup_directories():
    """Membuat struktur folder untuk dataset penyakit kakao"""
    base_dir = "dataset"
    classes = ["sehat", "kanker_batang", "vsd", "busuk_buah"]
    
    print("[DIR] Membuat struktur folder dataset...")
    for cls in classes:
        path = os.path.join(base_dir, cls)
        os.makedirs(path, exist_ok=True)
        print(f"  - {path}/")
    print("[SUCCESS] Folder dataset berhasil dibuat!")
    return base_dir

def show_roboflow_guide():
    """Menampilkan instruksi cara mengunduh dataset menggunakan Roboflow API"""
    guide = """
========================================================================
[INFO] CARA MENGUNDUH DATASET DARI ROBOFLOW:
========================================================================
1. Instal library Roboflow:
   pip install roboflow tensorflow matplotlib

2. Dapatkan API Key gratis dengan mendaftar di https://roboflow.com

3. Jalankan kode Python berikut untuk mengunduh dataset:

   from roboflow import Roboflow
   rf = Roboflow(api_key="MASUKKAN_API_KEY_KAMU_DISINI")
   project = rf.workspace("workspace-anda").project("proyek-dataset-anda")
   dataset = project.version(1).download("folder")
   
   # Pindahkan gambar hasil unduhan ke folder 'dataset/' sesuai kelasnya.
========================================================================
"""
    print(guide)

def load_and_augment_data(data_dir):
    """Contoh fungsi pemrosesan dan augmentasi gambar menggunakan Keras"""
    try:
        import tensorflow as tf
        from tensorflow.keras.preprocessing.image import ImageDataGenerator
        print("[INFO] TensorFlow terdeteksi, menyiapkan data pipeline...")
    except ImportError:
        print("[ERROR] TensorFlow tidak terdeteksi. Silakan instal terlebih dahulu menggunakan: pip install tensorflow")
        return

    # Parameter gambar (ESP32-CAM biasanya menggunakan resolusi QVGA atau VGA, untuk CNN 224x224 sangat ideal)
    IMG_SIZE = (224, 224)
    BATCH_SIZE = 32

    # Augmentasi data gambar untuk memperbanyak data secara buatan
    train_datagen = ImageDataGenerator(
        rescale=1./255,           # Normalisasi piksel ke [0,1]
        rotation_range=20,        # Rotasi gambar acak
        width_shift_range=0.2,    # Geser horizontal
        height_shift_range=0.2,   # Geser vertikal
        shear_range=0.2,          # Pergeseran sudut kemiringan
        zoom_range=0.2,           # Zoom acak
        horizontal_flip=True,     # Balik gambar secara horizontal
        validation_split=0.2      # Split data 80% training, 20% validasi
    )

    print(f"[INFO] Memuat data dari folder '{data_dir}'...")
    try:
        train_generator = train_datagen.flow_from_directory(
            data_dir,
            target_size=IMG_SIZE,
            batch_size=BATCH_SIZE,
            class_mode='categorical',
            subset='training'
        )
        
        val_generator = train_datagen.flow_from_directory(
            data_dir,
            target_size=IMG_SIZE,
            batch_size=BATCH_SIZE,
            class_mode='categorical',
            subset='validation'
        )
        
        print("[SUCCESS] Data pipeline berhasil dibuat!")
        return train_generator, val_generator
    except Exception as e:
        print(f"[WARNING] Gagal memuat data (mungkin folder masih kosong): {e}")

if __name__ == "__main__":
    base_dir = setup_directories()
    show_roboflow_guide()
    load_and_augment_data(base_dir)
