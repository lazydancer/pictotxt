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
    
def get_image_slices(image_path, char_width, char_height):
    image = Image.open(image_path)
    image = image.convert('L') #greyscale
    
    data = list(image.getdata())
    image_2D = np.reshape(data, (image.height, image.width))
    
    image_2D = trim_image(image_2D, char_width, char_height)
    image_slices = view_as_blocks(image_2D, block_shape=(char_height,char_width))
    
    return image_slices