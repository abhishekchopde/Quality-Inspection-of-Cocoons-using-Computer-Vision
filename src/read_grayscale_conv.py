# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 20:47:47 2017

@author: Abhishek
"""

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

im = np.array(Image.open('rotated_45_anti.jpg').convert('L'),'f')
print im.shape, im.dtype
plt.imshow(im, cmap = plt.get_cmap('gray'))
plt.show
