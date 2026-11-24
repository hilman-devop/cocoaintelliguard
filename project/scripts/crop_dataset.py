import os
import glob
from PIL import Image

# ponytail: crop both standard YOLO bbox and YOLO polygon segmentation format
def crop_yolo_dataset():
    input_base = os.path.join("raw_data", "Tugas-Akhir-Hama-Penyakit-Kakao-1")
    output_base = "dataset"
    
    # Map class IDs to output folder names
    class_map = {
        0: "busuk_buah",
        1: "helopeltis",
        2: "sehat",
        3: "penggerek_buah"
    }
    
    # Ensure output folders exist
    for folder in class_map.values():
        os.makedirs(os.path.join(output_base, folder), exist_ok=True)
        
    print("[INFO] Memulai cropping gambar berdasarkan bounding box/poligon YOLO...")
    
    splits = ["train", "valid", "test"]
    crop_count = 0
    
    for split in splits:
        img_dir = os.path.join(input_base, split, "images")
        label_dir = os.path.join(input_base, split, "labels")
        
        if not os.path.exists(img_dir) or not os.path.exists(label_dir):
            continue
            
        # Find all label files
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
                
            # Read annotations
            with open(label_file, "r") as f:
                lines = f.readlines()
                
            if not lines:
                continue
                
            try:
                img = Image.open(img_path)
                w, h = img.size
            except Exception as e:
                continue
                
            for idx, line in enumerate(lines):
                parts = line.strip().split()
                if len(parts) < 5:
                    continue
                    
                class_id = int(parts[0])
                
                # Check if it is YOLO segmentation format (more than 5 values)
                if len(parts) > 5:
                    coords = [float(p) for p in parts[1:]]
                    # x is even indices, y is odd indices
                    x_coords = coords[0::2]
                    y_coords = coords[1::2]
                    if not x_coords or not y_coords:
                        continue
                    xmin, xmax = min(x_coords), max(x_coords)
                    ymin, ymax = min(y_coords), max(y_coords)
                    
                    left = int(xmin * w)
                    right = int(xmax * w)
                    top = int(ymin * h)
                    bottom = int(ymax * h)
                else:
                    # Standard YOLO box format (5 values)
                    x_center = float(parts[1])
                    y_center = float(parts[2])
                    box_w = float(parts[3])
                    box_h = float(parts[4])
                    
                    left = int((x_center - box_w / 2) * w)
                    right = int((x_center + box_w / 2) * w)
                    top = int((y_center - box_h / 2) * h)
                    bottom = int((y_center + box_h / 2) * h)
                
                # Clip to image boundaries
                left = max(0, left)
                top = max(0, top)
                right = min(w, right)
                bottom = min(h, bottom)
                
                # Check for valid box dimensions
                if right - left < 5 or bottom - top < 5:
                    continue
                    
                # Crop and save
                try:
                    cropped_img = img.crop((left, top, right, bottom))
                    class_name = class_map.get(class_id, "unknown")
                    if class_name == "unknown":
                        continue
                        
                    output_filename = f"{base_name}_crop_{idx}.jpg"
                    output_path = os.path.join(output_base, class_name, output_filename)
                    
                    cropped_img.convert("RGB").save(output_path, "JPEG")
                    crop_count += 1
                except Exception as e:
                    pass
                    
    print(f"[SUCCESS] Berhasil memotong {crop_count} gambar dan menyimpannya ke folder klasifikasi!")

if __name__ == "__main__":
    crop_yolo_dataset()
