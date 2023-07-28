from PIL import Image
from os import listdir

source_dir = "images/"
new_dir = "/opt/icons/"

rotate_90dg = -90
resize_128p = (128, 128)
format_jpeg = "JPEG"

image_files = [f for f in listdir(source_dir) if f.startswith("ic_")]

for file in image_files :
    src_image = Image.open(source_dir + file)
    new_image = src_image.rotate(rotate_90dg).resize(resize_128p).convert("RGB").save(new_dir + file, format_jpeg)