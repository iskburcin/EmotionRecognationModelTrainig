from PIL import Image
import os

# Önce dataset1 klasörüne tüm duyguların adıyla oluşturulmuş boş klasörleri içeren test1 klasörünü oluştur
# Sonra test 'in içindeki her duygu klasörünün adını path'de değiştir
# Aynı işlemi train için de yap, train1 vs...
# En son eski test ve train klasörlerini silip yeni test1, train1 klasörlerinin isimlerini güncelle

input_folder = "datasett/dataset1/test/Happy"
output_folder = "datasett/dataset1/test1/Happy"
target_size = 224


def resize_images(input_folder, output_folder, target_size):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith((".jpg", ".jpeg", ".png", ".bmp")):
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)
            img = img.resize((target_size, target_size), Image.LANCZOS)

            save_path = os.path.join(output_folder, filename)
            img.save(save_path)

    print(f"All images resized and saved to {output_folder}")


resize_images(input_folder, output_folder, target_size)
resize_images(input_folder, output_folder, target_size)
