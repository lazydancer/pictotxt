from PIL import Image, ImageDraw, ImageFont
import numpy as np
from skimage.util.shape import view_as_blocks

def solve_section(section, letters):
    min_score = 1000000
    min_letter = None
    id = 0
    
    for k in letters:
        score = np.sum(np.absolute(letters[k] - section))
        if score < min_score:
            min_score = score
            min_letter = letters[k]
            min_id = k
            
    return (min_id, min_letter)
'''
def solve(sections, letters):
    results = []
    ids = []
    for s in sections:
        id, min_letter = solve_section(s, letters)
        results.append(min_letter)
        ids.append(id)

    return (ids, np.stack(results, axis=0))
'''

def solve(letter_images, images_slices):
    result = []
    for y in images_slices:
        row = []
        for x in y:
            id, _ = solve_section(x, letter_images)
            row.append(id)
        result.append(row)

    return result 
