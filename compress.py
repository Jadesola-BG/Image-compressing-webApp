import os
from PIL import Image

def compress_image(image_name, results_folder):
    old_image = Image.open(os.path.join(results_folder,image_name))
    old_image_size = os.path.getsize(os.path.join(results_folder,image_name))
    old_image.save(os.path.join(results_folder, "compressed_" + image_name), optimize=True, quality=65)
    compressed_image = Image.open(os.path.join(results_folder,  "compressed_" + image_name))
    compressed_image_size = os.path.getsize(os.path.join(results_folder,  "compressed_" + image_name))
    return [image_name, compressed_image_size, old_image_size]
    