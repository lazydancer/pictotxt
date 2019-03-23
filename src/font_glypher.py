from PIL import Image, ImageDraw, ImageFont
import numpy as np

def convert(font_path, characters, size):
    '''
    Returns a dictionary, keys: character as string
                          value: Image data representing character as an narray
    '''
    fnt = ImageFont.truetype(font_path, size)
    results = []

    for letter in characters:
        img = Image.new('RGB', (10, 18), color=(255,255,255))
        d = ImageDraw.Draw(img)
        d.text((0,0),letter, font=fnt, fill=(0,0,0))
        img = img.convert('L') #greyscale
        
        d = list(img.getdata())
        image_2D = np.reshape(d, (img.height, img.width))
        
        results.append(image_2D)

    letter_imgs = np.stack(results, axis=0)
        
    return dict(zip(characters, letter_imgs))
