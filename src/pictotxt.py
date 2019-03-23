from PIL import Image, ImageDraw, ImageFont
import numpy as np
from skimage.util.shape import view_as_blocks

import font_glypher
import pic_splitter
import pic_combiner
import solver


char_width = 10
char_height = 18
image_slices = pic_splitter.get_image_slices('../tests/octocat.png', char_width, char_height)

images = image_slices.reshape(image_slices.shape[0]*image_slices.shape[1], image_slices.shape[2], image_slices.shape[3])
nb_across = image_slices.shape[0]
nb_down = image_slices.shape[1]

letters_idx, letters = font_glypher.convert('../fonts/SFMono-Regular.otf')

ids, result = solver.solve(images, letters)

result_string = ""
i = 1
for id in ids:
    result_string += letters_idx[id]
    if i % image_slices.shape[1] == 0:
        result_string += '\n'
    i += 1

print(result_string)