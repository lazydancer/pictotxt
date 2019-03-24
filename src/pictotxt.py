import numpy as np
import string

import font_glypher
import pic_splitter
import pic_combiner
import pic_matcher

def main():    
    input_letters = string.printable
    size = 15
    letter_images = font_glypher.convert('fonts/SFMono-Regular.otf', input_letters, size)

    char_width, char_height = 10, 18
    image_slices = pic_splitter.get_image_slices('tests/octocat.png', char_width, char_height)

    result = pic_matcher.solve(letter_images, image_slices)

    print('\n'.join([''.join(row) for row in result]))
  
if __name__== "__main__":
    main()