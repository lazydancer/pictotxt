import numpy as np
import string
from PIL import Image, ImageDraw, ImageFont

import pic_splitter
import pic_matcher

def random_val(dictionary):
    return next(iter(dictionary.values()))

def extract_glyphs(font_path, characters, size):
    '''
    Returns a dictionary, key: character
                          value: character image as narray
    '''
    font = ImageFont.truetype(font_path, size)
    
    # mono-font has the same width, decender used to set height
    font_dimensions = font.getsize('j') 

    results = []

    for letter in characters:
        img = Image.new('RGB', font_dimensions, color=(255,255,255))
        d = ImageDraw.Draw(img)
        d.text((0,0),letter, font=font, fill=(0,0,0))
        img = img.convert('L') # greyscale
        d = list(img.getdata())
        image_2D = np.reshape(d, (img.height, img.width))
        
        results.append(image_2D)

    letter_imgs = np.stack(results, axis=0)
        
    return dict(zip(characters, letter_imgs))


def main():    
    input_letters = string.ascii_letters + string.digits + string.punctuation + ' '

    letter_images = extract_glyphs('fonts/DroidSansMono/DroidSansMono.ttf', input_letters, size=15)

    char_height, char_width = random_val(letter_images).shape
    image_slices = pic_splitter.get_image_slices('tests/octocat.png', char_width, char_height)

    result = pic_matcher.solve(letter_images, image_slices)

    print('\n'.join([''.join(row) for row in result]))
  
if __name__== "__main__":
    main()