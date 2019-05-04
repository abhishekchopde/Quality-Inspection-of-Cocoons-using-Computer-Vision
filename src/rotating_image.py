# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 17:09:50 2017

@author: Abhishek
"""

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

im = Image.open('Ellipse Detection Image.jpg')
im2 = im.rotate(45)
im2.save('im2.jpg')
plt.imshow(im, cmap = plt.get_cmap('gray'))
plt.show