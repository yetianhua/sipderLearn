import tesserocr

from PIL import Image

image = Image.open('C:/Users/qq115/Pictures/image.png')
print(tesserocr.image_to_text(image))