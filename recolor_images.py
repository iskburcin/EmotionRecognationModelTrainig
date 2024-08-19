from PIL import Image
import os


def convert_to_grayscale(input_folder, output_folder):
    print("started...")
    # Check if output folder exists, if not, create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        # Build full file path
        file_path = os.path.join(input_folder, filename)

        # Open an image file
        with Image.open(file_path) as img:
            # Convert image to grayscale
            grayscale_img = img.convert("L")

            # Save grayscale image to the output folder
            grayscale_img.save(os.path.join(output_folder, filename))

    print("All images have been converted to grayscale and saved to", output_folder)


# Önce dataset1 klasörüne tüm duyguların adıyla oluşturulmuş boş klasörleri içeren test1 klasörünü oluştur
# Sonra test 'in içindeki her duygu klasörünün adını path'de değiştir
# Aynı işlemi train için de yap, train1 vs...
# En son eski test ve train klasörlerini silip yeni test1, train1 klasörlerinin isimlerini güncelle
input_folder = "datasett/dataset1/test/Happy"
output_folder = "datasett/dataset1/test1/Happy"

convert_to_grayscale(input_folder, output_folder)
