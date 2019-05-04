# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 15:00:13 2017

@author: Abhishek
"""

from __future__ import division
import numpy as np
from PIL import Image

im = np.array(Image.open('rotated_45_anti.jpg').convert('L'),'f')
row,col = im.shape
I = []
x = []
y = []
for i in range(row):
    for j in range(col):
        if(im[i][j] > 128):
            I.append(im[i][j])
            x.append(j)
            y.append(i)

m = 50 #rotated rnge of a (180,230)
n = 30 #rotated range of b (130,160)
acc = np.zeros((m,n))
print acc
deltaA = 1 #min length of acc cell for a
deltaB = 1  #min length of acc cell for b
x0 = 180
y0 = 135
theta = 0.719797662767 # this theta is i radians

for k in range(n):
    print "value of k:",k
    for k1 in range(len(x)):
        print "value of k1:",k1
        x1 = x[k1]
        y1 = y[k1]
        bi = 130 + deltaB * k
        term1 = (x1-x0)*np.cos(theta)+(y1-y0)*np.sin(theta)
        term2 = np.sqrt(abs(1-((x1-x0)*np.sin(theta)+(y1-y0)*np.cos(theta))**2/bi**2))
        ai = abs(term1/term2)
        #ai = abs((x1-x0) * np.floor(1/np.sqrt(abs(1-((y1-y0)**2/bi**2)))))
        if(ai>=180 and ai<230):
            ai = ai-180
            q = np.floor(ai/deltaA)
            acc[q,k] = acc[q,k] + 1

print acc
b_index_max = np.argmax(np.max(acc, axis=0))
a_index_max = np.argmax(np.max(acc, axis=1))
b = 130 + deltaB * b_index_max
a = 180 + deltaA * a_index_max
print "a = ",a, "b = ",b
