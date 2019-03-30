from PIL import Image, ImageDraw, ImageFont
import numpy as np
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
    
def get_image_slices(image_path, slice_width, slice_height):
    image_2D = np.asarray(Image.open(image_path).convert('L'))

    image_2D = trim_image(image_2D, slice_width, slice_height)
    
    image_slices = view_as_blocks(image_2D, block_shape=(slice_height,slice_width))
    
    return image_slices