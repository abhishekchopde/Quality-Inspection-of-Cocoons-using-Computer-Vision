import scipy
from scipy import misc
import numpy as numpy
import os

image = scipy.misc.imread('DSC_0365.png')
image = scipy.misc.imresize(image,(1792,3072,3))
scipy.misc.imsave('patch_material_3.png',image)
