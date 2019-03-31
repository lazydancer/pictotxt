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

    results = []

    for letter in characters:
        img = Image.new('RGB', font_dimensions, color=(255,255,255))
        d = ImageDraw.Draw(img)
        d.text((0,0),letter, font=font, fill=(0,0,0))
        img = img.convert('L') # greyscale
        image_2D = np.reshape(list(img.getdata()), (img.height, img.width))
        
        results.append(image_2D)

    letter_imgs = np.stack(results, axis=0)
        
    return dict(zip(characters, letter_imgs))

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

def solve(letter_images, images_slices):
    def solve_section(section, letters):
        min_score = float('inf')
        min_letter = None

        for k in letters:
            score = np.sum(np.absolute(letters[k] - section))
            if score < min_score:
                min_score = score
                min_letter = k
                
        return min_letter

    result = []
    for y in images_slices:
        row = []
        for x in y:
            letter = solve_section(x, letter_images)
            row.append(letter)
        result.append(row)

    return result 


def main():
    def random_val(dictionary):
        return next(iter(dictionary.values()))
    
    input_letters = string.ascii_letters + string.digits + string.punctuation + ' '

    font = ImageFont.truetype('fonts/DroidSansMono/DroidSansMono.ttf', 15)
    letter_images = extract_glyphs(font, input_letters)

    image_2D = np.asarray(Image.open('tests/octocat.png').convert('L'))
    char_height, char_width = random_val(letter_images).shape
    image_slices = get_image_slices(image_2D, char_width, char_height)

    result = solve(letter_images, image_slices)

    print('\n'.join([''.join(row) for row in result]))
  
if __name__== "__main__":
    main()