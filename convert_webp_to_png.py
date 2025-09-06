import os
from PIL import Image

# Script'in çalıştığı ana klasör
base_folder = os.getcwd()

# Bütün alt klasörleri ve dosyaları gez
for root, dirs, files in os.walk(base_folder):
    for file in files:
        if file.lower().endswith(".webp"):
            file_path = os.path.join(root, file)

            # Dosya adını uzantısız al
            file_name_without_ext = os.path.splitext(file)[0]

            # Çıktı dosyası, aynı klasöre kaydedilecek
            output_path = os.path.join(root, file_name_without_ext + ".png")

            # Aynı isimde dosya varsa üzerine yazmamak için (1), (2) ekle
            counter = 1
            while os.path.exists(output_path):
                output_path = os.path.join(root, f"{file_name_without_ext}({counter}).png")
                counter += 1

            # WebP dosyasını aç ve PNG olarak kaydet
            try:
                img = Image.open(file_path).convert("RGBA")
                img.save(output_path, "PNG")
                print(f"Dönüştürüldü: {output_path}")
            except Exception as e:
                print(f"Hata oluştu ({file_path}): {e}")

print("✅ Tüm klasörler tarandı, WebP dosyaları PNG formatına dönüştürüldü!")
