# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 14:57:33 2017

@author: Abhishek
"""
from __future__ import division
import numpy as np
from PIL import Image

im = np.array(Image.open('Ellipse Detection Image.jpg').convert('L'),'f')
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

m = 50 #from range of a = (200,250)
n = 40 #from rage of b = (135,175) 
acc = np.zeros((m,n))
print acc
deltaA = 1 #min length of acc cell for a
deltaB = 1  #min length of acc cell for b
x0 = 335
y0 = 177
theta = -0.0663

for k in range(n):
    print "value of k:",k
    for k1 in range(len(x)):
        print "value of k1:",k1
        x1 = x[k1]
        y1 = y[k1]
        bi = 135 + deltaB * k
        term1 = (x1-x0)*np.cos(theta)+(y1-y0)*np.sin(theta)
        term2 = np.sqrt(abs(1-((x1-x0)*np.sin(theta)+(y1-y0)*np.cos(theta))**2/bi**2))
        ai = abs(term1/term2)
        #ai = abs((x1-x0) * np.floor(1/np.sqrt(abs(1-((y1-y0)**2/bi**2)))))
        if(ai>=200 and ai<250):
            ai = ai-200
            q = np.floor(ai/deltaA)
            acc[q,k] = acc[q,k] + 1

print acc
b_index_max = np.argmax(np.max(acc, axis=0))
a_index_max = np.argmax(np.max(acc, axis=1))
b = 135 + deltaB * b_index_max
a = 200 + deltaA * a_index_max
print "a = ",a, "b = ",b

 


    


            
            