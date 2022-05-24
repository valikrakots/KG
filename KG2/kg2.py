from PIL import Image
import os

count = 1
for root, dirs, files in os.walk('images'):
    for file in files:
        image = Image.open('images/' + file)
        print('Image', count)
        print('  Filename:', image.filename)
        print('  Size:', image.size)
        print('  DPI:', image.info.get('dpi'))
        print('  Color depth:', image.mode)
        print('  Compression:', image.info.get('compression'))
        count += 1
