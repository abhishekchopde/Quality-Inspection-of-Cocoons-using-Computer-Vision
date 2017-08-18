import scipy
from scipy import misc
import numpy as np  
import os
#import sqlite3 as lite
#import sys

def trainset():
	i=0
	single_patches = []
	for file in os.listdir('Good'):
		path = os.path.join('Good',file)
		image = scipy.misc.imread(path)
		a = []
		a.append(image)
		a.append(1)
		single_patches.append(a)

	for file in os.listdir('Bad'):
		path = os.path.join('Bad',file)
		image = scipy.misc.imread(path)
		a = []
		a.append(image)
		a.append(0)
		single_patches.append(a)
	return single_patches
		


 
	