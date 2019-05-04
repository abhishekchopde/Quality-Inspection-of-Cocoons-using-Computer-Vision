# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 12:40:42 2017

@author: Abhishek
"""
from __future__ import division
import numpy as np

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
            
#mean of x and y coordinates        
x_mean = np.mean(x)
y_mean = np.mean(y)

#mean adjusted x and y matrices
mean_adjusted_matrix_x = x - x_mean
mean_adjusted_matrix_y = y - y_mean

#value is the number of data points in x and y coordinates each
value = mean_adjusted_matrix_x.shape[0]
cov_matrix = np.empty((2,2),dtype =float)
print "interation_range =",value
#covariance of x co-ordinates
sum_x = 0
for k in range(value):
    sum_x = sum_x + (mean_adjusted_matrix_x[k])*(mean_adjusted_matrix_x[k])
sum_x = sum_x/value
cov_matrix[0,0] = sum_x

#covariance of y co-ordinates
sum_y = 0
for k1 in range(value):
    sum_y = sum_y + (mean_adjusted_matrix_y[k1])*(mean_adjusted_matrix_y[k1])
sum_y = sum_y/value
cov_matrix[1,1] = sum_y

#covariance of xy coordinates
sum_xy = 0
for k2 in range(value):
    sum_xy = sum_xy + (mean_adjusted_matrix_x[k2])*(mean_adjusted_matrix_y[k2])
cov_matrix[0,1] = sum_xy/value

sum_yx = 0
for k3 in range(value):
    sum_yx = sum_yx + (mean_adjusted_matrix_y[k3])*(mean_adjusted_matrix_x[k3])
cov_matrix[1,0] = sum_yx/value

print "cov_matrix = ",cov_matrix

lamda,V = np.linalg.eig(cov_matrix)
print "eig_vector =",V
print "eig_values =", lamda

theta = np.arctan(V[1,0]/V[1,1])
print "Theta = ", theta