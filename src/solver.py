from PIL import Image, ImageDraw, ImageFont
import numpy as np
from skimage.util.shape import view_as_blocks

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
