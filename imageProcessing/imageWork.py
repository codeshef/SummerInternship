
from PIL import Image, ImageFilter

import os

size_200 = (200, 200)

# listdir() list all content of dir

for f in os.listdir():

    if f.endswith('.jpeg'):

        img = Image.open(f)

        fn, text = os.path.splitext(f)

        print('File Name : ', fn, 'Extension : ', text)

         # To change size

        img.thumbnail(size_200)

        # change extension to png and save in png dir

        img.save('png/{}.png'.format(fn))

print("File Extension changed to PNG .....")

img1 = Image.open('1.jpeg')

# rotate image
img1.rotate(90).save('1_90.jpeg')

# convert into black and white image

img1.convert(mode='L').save('1_black_white.jpeg')

# Gaussian

img1.filter(ImageFilter.GaussianBlur(15)).save('i_Gauss_blur.jpeg')

print('Image saved!!')








