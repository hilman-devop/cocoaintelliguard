import os
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import MobileNetV2

# ponytail: simple transfer learning using MobileNetV2 and TFLite conversion
def train_model():
    data_dir = "dataset"
    img_size = (224, 224)
    batch_size = 32
    
    print("[INFO] Memuat training & validation dataset...")
    # Load dataset
    train_ds = tf.keras.utils.image_dataset_from_directory(
        data_dir,
        validation_split=0.2,
        subset="training",
        seed=123,
        image_size=img_size,
        batch_size=batch_size,
        label_mode='categorical'
    )
    
    val_ds = tf.keras.utils.image_dataset_from_directory(
        data_dir,
        validation_split=0.2,
        subset="validation",
        seed=123,
        image_size=img_size,
        batch_size=batch_size,
        label_mode='categorical'
    )
    
    class_names = train_ds.class_names
    num_classes = len(class_names)
    print(f"[INFO] Kelas yang dideteksi: {class_names} ({num_classes} kelas)")
    
    # Prefetching for performance
    AUTOTUNE = tf.data.AUTOTUNE
    train_ds = train_ds.prefetch(buffer_size=AUTOTUNE)
    val_ds = val_ds.prefetch(buffer_size=AUTOTUNE)
    
    print("[INFO] Membangun model MobileNetV2 untuk Edge AI...")
    # Base model MobileNetV2 (sangat ringan untuk ESP32-CAM)
    base_model = MobileNetV2(input_shape=(224, 224, 3), include_top=False, weights='imagenet')
    base_model.trainable = False  # Freeze weights agar training cepat
    
    model = models.Sequential([
        layers.Rescaling(1./255, input_shape=(224, 224, 3)), # Normalisasi gambar
        base_model,
        layers.GlobalAveragePooling2D(),
        layers.Dropout(0.2),
        layers.Dense(num_classes, activation='softmax')
    ])
    
    model.compile(
        optimizer='adam',
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    
    model.summary()
    
    # Jumlah epoch (bisa dinaikkan nanti untuk akurasi optimal, misal 20-50)
    epochs = 5
    print(f"[INFO] Memulai training selama {epochs} epoch...")
    history = model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=epochs
    )
    
    model_path = os.path.join("models", "cacao_model")
    model.export(model_path)
    print(f"[SUCCESS] Model keras berhasil diexport ke folder '{model_path}'")
    
    # Konversi ke TFLite dengan Kuantisasi agar muat di ESP32-CAM
    print("[INFO] Mengonversi model ke format TensorFlow Lite terkuantisasi (optimized for Edge AI)...")
    converter = tf.lite.TFLiteConverter.from_saved_model(model_path)
    converter.optimizations = [tf.lite.Optimize.DEFAULT]
    tflite_model = converter.convert()
    
    tflite_file = os.path.join("models", "cacao_model.tflite")
    with open(tflite_file, "wb") as f:
        f.write(tflite_model)
    print(f"[SUCCESS] Model TFLite berhasil disimpan sebagai '{tflite_file}'!")

if __name__ == "__main__":
    train_model()
