import numpy as np 
import skimage.util.shape as view_as_blocks
import skimage
import scipy
from scipy import misc
import os

patch = []
for file in os.listdir('finalimages'):
	path = os.path.join('finalimages',file)
	image = scipy.misc.imread(path)
	patch_i = skimage.util.view_as_blocks(image,block_shape = (256,256,1))
	print patch_i.shape
	patch.append(patch_i)

index = 1
for i in range(8):
	for j in range(6):
		for k in range(12):
			for l in range(4):
				newpath = os.path.join('patches_i', str(index) + '.png')
				scipy.misc.imsave(newpath,patch[i][j][k][l])
				index = index + 1	



#for i in range(4):
	#print patch[0][1][i]


