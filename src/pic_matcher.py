from PIL import Image, ImageDraw, ImageFont
import numpy as np
from skimage.util.shape import view_as_blocks

def solve_section(section, letters):
    min_score = float('inf')
    min_letter = None
    
    for k in letters:
        score = np.sum(np.absolute(letters[k] - section))
        if score < min_score:
            min_score = score
            min_letter = k
            
    return min_letter

def solve(letter_images, images_slices):
    result = []
    for y in images_slices:
        row = []
        for x in y:
            letter = solve_section(x, letter_images)
            row.append(letter)
        result.append(row)

    return result 
