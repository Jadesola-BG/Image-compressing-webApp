import os
from PIL import Image

def determine_image_size(folder, image_name):
    return os.path.getsize(os.path.join(folder,image_name))

def open_image(folder, image_name):
    return Image.open(os.path.join(folder,image_name))

def compress_image(image_name, results_folder):
    original_image = open_image(results_folder,image_name)
    original_image_size = determine_image_size(results_folder, image_name)  
    original_image.save(os.path.join(results_folder, "compressed_" + image_name), optimize=True, quality=65)
    compressed_image = open_image(results_folder,  "compressed_" + image_name)
    compressed_image_size = determine_image_size(results_folder,  "compressed_" + image_name)   
    return [image_name, compressed_image_size, original_image_size]
    