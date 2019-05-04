# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 22:04:35 2017

@author: Abhishek
"""

from PIL import Image
from scipy.misc import imsave
import numpy
import matplotlib.pyplot as plt


def binarize_image(img_path, target_path, threshold):
    """Binarize an image."""
    image_file = Image.open("Ellipse Detection Image.jpg")
    image = image_file.convert('L')  # convert image to monochrome
    image = numpy.array(image)
    image = binarize_array(image, threshold)


def binarize_array(numpy_array, threshold=200):
    """Binarize a numpy array."""
    for i in range(len(numpy_array)):
        for j in range(len(numpy_array[0])):
            if numpy_array[i][j] > threshold:
                numpy_array[i][j] = 255
            else:
                numpy_array[i][j] = 0
    return numpy_array

plt.imshow(image, cmap = plt.get_cmap('gray'))

cols,rows = image.size
pixels = list(image.getdata())

# an indexer into the flat list of pixels
# head ranges from 0 to len(pixels) with step cols
# tail ranges from cols to len(pixels) with step cols
head_tail = zip(range(0,len(pixels)+1,cols),range(cols,len(pixels)+1,cols))
im_data = np.ndarray(shape=(cols,rows), dtype=np.uint8)

# extract each row of pixels and save it to the numpy array
for i,(head,tail) in enumerate(head_tail):
    im_data[i] = np.array(pixels[head:tail], dtype=np.uint8)

pl.imshow(im_data, cmap='bone')

