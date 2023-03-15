from PIL import Image, ImageEnhance, ImageFilter
import os

path = "D:\Python\Projects\ImageEditing\Images"
pathOut = "D:\Python\Projects\ImageEditing\EditedImages"

print()

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    # sharpening, CMYK, Blur
    edit = img.filter(ImageFilter.SHARPEN).convert('CMYK').filter(ImageFilter.BLUR)

    # contrast
    factor = 1.2
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    # ADD MORE EDITS FROM DOCUMENTATION https://pillow.readthedocs.io/en/stable/

    clean_name = os.path.splitext(filename)[0]


    edit.save(f'{pathOut}/{clean_name}_edited.JPG')
