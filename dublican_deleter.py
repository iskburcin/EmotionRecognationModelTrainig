from PIL import Image
import os
import numpy as np

# bu file ı oluşturdum ama kullanmadım, belki ilerde kullanılabilir
# Dosya içerisindeki aynı resimlerden birini siliyor
# recolor, resize dosyalarında yapılarn işlemi tekrarlayabilirsin ya da sadece istediğin dosya yolundakileri temizleyebilirsin

def compare_images(img1_path, img2_path):
    img1 = Image.open(img1_path)
    img2 = Image.open(img2_path)
    
    # Convert images to numpy arrays
    arr1 = np.array(img1)
    arr2 = np.array(img2)
    
    # Compare images
    return np.array_equal(arr1, arr2)

def delete_duplicates(folder_path):
    print("Process stareted...")
    # List all files in the folder
    files = os.listdir(folder_path)
    
    # Dictionary to keep track of duplicates
    duplicates = {}
    
    # Iterate over all files in the folder
    for i in range(len(files)):
        for j in range(i + 1, len(files)):
            file1 = os.path.join(folder_path, files[i])
            file2 = os.path.join(folder_path, files[j])
            
            # Compare the two images
            if compare_images(file1, file2):
                # If they are duplicates, add to the dictionary
                duplicates[file2] = file1
    
    # Delete duplicate files
    for duplicate in duplicates:
        os.remove(duplicate)
        print(f"Deleted duplicate file: {duplicate}")

    print("All duplicates have been removed.")

# Example usage
folder_path = 'datasett/dataset1/train/Angry'  # Replace with your folder path
delete_duplicates(folder_path)
