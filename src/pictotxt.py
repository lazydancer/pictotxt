from PIL import Image, ImageDraw, ImageFont
import numpy as np
import matplotlib.pyplot as plt
from skimage.util.shape import view_as_blocks

def trim_image(matrix, size_x, size_y):
    height, width = matrix.shape
    trim_height = height % size_y
    trim_width = width % size_x
    
    if trim_height > 0:
        matrix = matrix[:-trim_height,...]
    
    if trim_width > 0:
        matrix = matrix[...,:-trim_width]
    
    return matrix
    
def get_image_slices(image_path, char_width, char_height):
    image = Image.open(image_path)
    image = image.convert('L') #greyscale
    
    data = list(image.getdata())
    image_2D = np.reshape(data, (image.height, image.width))
    
    image_2D = trim_image(image_2D, char_width, char_height)
    image_slices = view_as_blocks(image_2D, block_shape=(char_height,char_width))
    
    return image_slices

def font_images(font_path):
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


def solve_section(section, letters):
    min_score = 1000000
    min_letter = None
    id = 0
    
    for letter in letters:
        score = np.sum(np.absolute(letter - section))
        if score < min_score:
            min_score = score
            min_letter = letter
            min_id = id
        id += 1
            
    return (min_id, min_letter)

def solve(sections, letters):
    results = []
    ids = []
    for s in sections:
        id, min_letter = solve_section(s, letters)
        results.append(min_letter)
        ids.append(id)

    return (ids, np.stack(results, axis=0))


char_width = 10
char_height = 18
image_slices = get_image_slices('../bird-twitter.png', char_width, char_height)

images = image_slices.reshape(image_slices.shape[0]*image_slices.shape[1], image_slices.shape[2], image_slices.shape[3])
nb_across = image_slices.shape[0]
nb_down = image_slices.shape[1]

letters_idx, letters = font_images('../fonts/SFMono-Regular.otf')

ids, result = solve(images, letters)

result_string = ""
i = 1
for id in ids:
    result_string += letters_idx[id]
    if i % image_slices.shape[1] == 0:
        result_string += '\n'
    i += 1

print(result_string)