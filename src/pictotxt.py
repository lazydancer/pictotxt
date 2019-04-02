import string
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

def main(file_path):
    input_chars = string.ascii_letters + string.digits + string.punctuation + ' '

    font = ImageFont.truetype('fonts/DroidSansMono/DroidSansMono.ttf', 13)
    char_images = slice_font(font, input_chars)

    image = np.asarray(Image.open(file_path).convert('L'))
    char_height, char_width = char_images[input_chars[0]].shape
    image_slices = slice_image(image, char_width, char_height)

    result = match(char_images, image_slices)

    print('\n'.join([''.join(row) for row in result]))

def slice_font(font, characters):
    # mono-font has the same width, decender used to set height
    font_dimensions = font.getsize('j') 

    results = {}
    for char in characters:
        img = Image.new('L', font_dimensions, color=255)
        draw = ImageDraw.Draw(img)
        draw.text((0,0), char, font=font, fill=0)
        array = np.array(list(img.getdata()), dtype='uint8')
        results[char] = np.reshape(array, (img.height, img.width))
        
    return results

def slice_image(image, slice_width, slice_height):
    height = image.shape[0] // slice_height
    width = image.shape[1] // slice_width
    
    result = np.zeros((height, width, slice_height, slice_width))
    for y in range(height):
        for x in range(width):
            start_x = x * slice_width
            start_y = y * slice_height
            result[y][x] = image[start_y:start_y + slice_height, start_x:start_x + slice_width]

    return result

def match(char_images, image_slices):
    def match_section(image, characters):
        return min(char_images, key=lambda char : np.sum(np.absolute(characters[char] - image)**2))

    return [[match_section(img, char_images) for img in row] for row in image_slices] 

def test():
    return 7

if __name__== "__main__":
    main(sys.argv[1])    