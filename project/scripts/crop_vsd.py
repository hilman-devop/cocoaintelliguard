import os
import glob
from PIL import Image

# ponytail: crop VSD dataset images and map all to "vsd" class
def crop_vsd_dataset():
    input_base = os.path.join("raw_data", "TERSERANG-VSD-DAUN-KAKAO-2")
    output_base = "dataset"
    class_name = "vsd"
    
    os.makedirs(os.path.join(output_base, class_name), exist_ok=True)
    print("[INFO] Memulai cropping gambar untuk VSD...")
    
    splits = ["train", "valid", "test"]
    crop_count = 0
    
    for split in splits:
        img_dir = os.path.join(input_base, split, "images")
        label_dir = os.path.join(input_base, split, "labels")
        
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
                
            try:
                img = Image.open(img_path)
                w, h = img.size
            except Exception as e:
                continue
                
            for idx, line in enumerate(lines):
                parts = line.strip().split()
                if len(parts) < 5:
                    continue
                    
                # Semua koordinat dipetakan sebagai kelas "vsd"
                if len(parts) > 5:
                    coords = [float(p) for p in parts[1:]]
                    x_coords = coords[0::2]
                    y_coords = coords[1::2]
                    if not x_coords or not y_coords:
                        continue
                    xmin, xmax = min(x_coords), max(x_coords)
                    ymin, ymax = min(y_coords), max(y_coords)
                    left, right = int(xmin * w), int(xmax * w)
                    top, bottom = int(ymin * h), int(ymax * h)
                else:
                    x_center, y_center = float(parts[1]), float(parts[2])
                    box_w, box_h = float(parts[3]), float(parts[4])
                    left = int((x_center - box_w / 2) * w)
                    right = int((x_center + box_w / 2) * w)
                    top = int((y_center - box_h / 2) * h)
                    bottom = int((y_center + box_h / 2) * h)
                
                left, top = max(0, left), max(0, top)
                right, bottom = min(w, right), min(h, bottom)
                
                if right - left < 5 or bottom - top < 5:
                    continue
                    
                try:
                    cropped_img = img.crop((left, top, right, bottom))
                    output_filename = f"vsd_{base_name}_crop_{idx}.jpg"
                    output_path = os.path.join(output_base, class_name, output_filename)
                    cropped_img.convert("RGB").save(output_path, "JPEG")
                    crop_count += 1
                except Exception as e:
                    pass
                    
    print(f"[SUCCESS] Berhasil memotong {crop_count} gambar VSD!")

if __name__ == "__main__":
    crop_vsd_dataset()
