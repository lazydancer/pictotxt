from PIL import Image, ImageDraw, ImageFont
import numpy as np

def convert(font_path):
    fnt = ImageFont.truetype(font_path, 15)
    import string
    letters = string.printable
    results = []

    for letter in letters:
        img = Image.new('RGB', (10, 18), color=(255,255,255))
        d = ImageDraw.Draw(img)
        d.text((0,0),letter, font=fnt, fill=(0,0,0))
        img = img.convert('L') #greyscale
        
        d = list(img.getdata())
        image_2D = np.reshape(d, (img.height, img.width))
        
        results.append(image_2D)
        
    return (letters, np.stack(results, axis=0))
