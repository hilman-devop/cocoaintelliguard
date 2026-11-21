import os

# ponytail: simple binary file to C header array converter for TFLite Micro
def convert_tflite_to_header():
    tflite_path = os.path.join("models", "cacao_model.tflite")
    header_path = os.path.join("models", "cacao_model_data.h")
    
    if not os.path.exists(tflite_path):
        print(f"[ERROR] File model TFLite tidak ditemukan di: {tflite_path}")
        return
        
    print(f"[INFO] Membaca file model TFLite dari: {tflite_path}...")
    with open(tflite_path, "rb") as f:
        tflite_content = f.read()
        
    print(f"[INFO] Mengonversi file (.tflite) menjadi C Array...")
    
    # Format ke byte array hex untuk C
    hex_lines = []
    for i in range(0, len(tflite_content), 12):
        chunk = tflite_content[i:i+12]
        hex_line = ", ".join([f"0x{b:02x}" for b in chunk])
        hex_lines.append("  " + hex_line)
        
    header_content = f"""#ifndef CACAO_MODEL_DATA_H
#define CACAO_MODEL_DATA_H

// Model TFLite Terkuantisasi untuk deteksi penyakit Kakao
// Ukuran file asli: {len(tflite_content)} bytes

alignas(8) const unsigned char g_cacao_model_data[] = {{
{",\n".join(hex_lines)}
}};

const unsigned int g_cacao_model_data_len = {len(tflite_content)};

#endif // CACAO_MODEL_DATA_H
"""

    print(f"[INFO] Menulis header file ke: {header_path}...")
    with open(header_path, "w") as f:
        f.write(header_content)
        
    print(f"[SUCCESS] Berhasil mengonversi model! Silakan sertakan file '{header_path}' di proyek Arduino IDE kamu.")

if __name__ == "__main__":
    convert_tflite_to_header()
