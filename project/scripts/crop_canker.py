import os
import glob
import shutil
from PIL import Image

# ponytail: move downloaded dataset, crop canker bounding boxes (class 5) and save to dataset/kanker_batang/
def main():
    src_dir = "penyakit-1"
    dest_dir = os.path.join("raw_data", "penyakit-1")
    
    # 1. Move folder to raw_data if it exists in root
    if os.path.exists(src_dir):
        print(f"[INFO] Memindahkan folder {src_dir} ke {dest_dir}...")
        os.makedirs("raw_data", exist_ok=True)
        # If destination already exists, delete it first to avoid nesting or conflicts
        if os.path.exists(dest_dir):
            shutil.rmtree(dest_dir)
        shutil.move(src_dir, dest_dir)
        print("[SUCCESS] Folder berhasil dipindahkan!")
        
    if not os.path.exists(dest_dir):
        print(f"[ERROR] Folder dataset tidak ditemukan di {dest_dir}!")
        return

    output_base = "dataset"
    class_name = "kanker_batang"
    target_class_id = 5 # kanker batang kakao based on data.yaml
    
    os.makedirs(os.path.join(output_base, class_name), exist_ok=True)
    print(f"[INFO] Memulai cropping gambar untuk kanker_batang dari {dest_dir}...")
    
    splits = ["train", "valid", "test"]
    crop_count = 0
    
    for split in splits:
        img_dir = os.path.join(dest_dir, split, "images")
        label_dir = os.path.join(dest_dir, split, "labels")
        
        if not os.path.exists(img_dir) or not os.path.exists(label_dir):
            continue
            
        label_files = glob.glob(os.path.join(label_dir, "*.txt"))
        
        for label_file in label_files:
            base_name = os.path.splitext(os.path.basename(label_file))[0]
            img_path = None
            for ext in [".jpg", ".jpeg", ".png", ".JPG", ".PNG"]:
                temp_path = os.path.join(img_dir, base_name + ext)
                if os.path.exists(temp_path):
                    img_path = temp_path
                    break
                    
            if not img_path:
                continue
                
            with open(label_file, "r") as f:
                lines = f.readlines()
                
            if not lines:
                continue
                
            img = None
            w, h = 0, 0
            
            for idx, line in enumerate(lines):
                parts = line.strip().split()
                if len(parts) < 5:
                    continue
                    
                class_id = int(parts[0])
                if class_id != target_class_id:
                    continue
                    
                # Lazy load image only when we find target class
                if img is None:
                    try:
                        img = Image.open(img_path)
                        w, h = img.size
                    except Exception as e:
                        print(f"[WARNING] Gagal membuka gambar {img_path}: {e}")
                        break
                
                # Standard YOLO box format (5 values)
                try:
                    x_center = float(parts[1])
                    y_center = float(parts[2])
                    box_w = float(parts[3])
                    box_h = float(parts[4])
                    
                    left = int((x_center - box_w / 2) * w)
                    right = int((x_center + box_w / 2) * w)
                    top = int((y_center - box_h / 2) * h)
                    bottom = int((y_center + box_h / 2) * h)
                    
                    # Clip boundaries
                    left = max(0, left)
                    top = max(0, top)
                    right = min(w, right)
                    bottom = min(h, bottom)
                    
                    if right - left < 5 or bottom - top < 5:
                        continue
                        
                    cropped_img = img.crop((left, top, right, bottom))
                    output_filename = f"canker_{base_name}_crop_{idx}.jpg"
                    output_path = os.path.join(output_base, class_name, output_filename)
                    
                    cropped_img.convert("RGB").save(output_path, "JPEG")
                    crop_count += 1
                except Exception as e:
                    print(f"[WARNING] Gagal memproses box pada {label_file}: {e}")
                    pass
                    
    print(f"[SUCCESS] Berhasil memotong {crop_count} gambar kanker batang!")

if __name__ == "__main__":
    main()
