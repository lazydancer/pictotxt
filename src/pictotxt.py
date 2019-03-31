import numpy as np
import string
from PIL import Image, ImageDraw, ImageFont

def extract_glyphs(font, characters):
    '''
    Returns a dictionary, key: character
                          value: character image as narray
    '''  
    # mono-font has the same width, decender used to set height
    font_dimensions = font.getsize('j') 

    results = {}
    for letter in characters:
        img = Image.new('L', font_dimensions, color=255)
        draw = ImageDraw.Draw(img)
        draw.text((0,0), letter, font=font, fill=0)
        array = np.array(list(img.getdata()), dtype='uint8')
        results[letter] = np.reshape(array, (img.height, img.width))
        
    return results

def get_image_slices(image_2D, slice_width, slice_height):
    '''
    Returns an image of images (4D array)
    '''
    height = image_2D.shape[0] // slice_height
    width = image_2D.shape[1] // slice_width
    
    result = np.zeros((height, width, slice_height, slice_width))
    for y in range(height):
        for x in range(width):
            start_x = x * slice_width
            start_y = y * slice_height
            result[y][x] = image_2D[start_y:start_y + slice_height, start_x:start_x + slice_width]

    return result

def match(letter_images, image_slices):
    '''
    Returns 2d array matching shape of image slices of 'best' letter match
    '''
    def match_section(section, letters):
        return min(letter_images, key=lambda ltr : np.sum(np.absolute(letters[ltr] - section)**2))

    return [[match_section(img, letter_images) for img in row] for row in image_slices] 


def main(file_path='tests/octocat.png'):
    input_letters = string.ascii_letters + string.digits + string.punctuation + ' '

    font = ImageFont.truetype('fonts/DroidSansMono/DroidSansMono.ttf', 15)
    letter_images = extract_glyphs(font, input_letters)

    image_2D = np.asarray(Image.open(file_path).convert('L'))
    char_height, char_width = letter_images[input_letters[0]].shape
    image_slices = get_image_slices(image_2D, char_width, char_height)

    result = match(letter_images, image_slices)

    return '\n'.join([''.join(row) for row in result])
  
if __name__== "__main__":
    print(main())