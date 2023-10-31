import os
from PIL import Image

out = './out/'
files = os.listdir('./images')
for file in files:
    filename = file.split('.')[0]
    png_image = Image.open('./images/' + file)
    png_image.save(out + filename + '.gif')

os.system('rm -rf ./images/*')