#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 15:44:11 2018

@author: rm
"""       
M_asList = [[1, 2, 3],
        [4,5,6],
        [7,8,9]]
print("\nM as list: ",M_asList)

#From: Lutz, Mark. Learning Python (p. 586). 
#O'Reilly Media. Kindle Edition. 
print("[1st element] of all rows (using list comprehension): ", \
      [[row[0]] for row in M_asList],  "<<<<<<<<<<<<<<<<<<<<<<<")
#print("1st element of all rows: ", row[0] for row in M_asList)

import numpy as np

M_asMatrix = np.asarray(M_asList)
print("\nM as array:\n",M_asMatrix)

print("\narray of 1st element from each Row of M_asMatrix: ", \
                  (M_asMatrix[:, 0]), " <<<<<<<<<<<<<<<<<<<<<<<")
#array([1, 4, 7])
print("1st element of all M_asMatrix rows (using list comprehension): ", \
      [row[0] for row in M_asMatrix], " <<<<<<<<<<<<<<<<<<<<<<<")

print("Type of M_asMatrix[:, 0]: ", type(M_asMatrix[:, 0]))
#<class 'numpy.ndarray'>

print("Dim of M_asMatrix[:, 0] (is 1-D array): ", (M_asMatrix[:, 0].ndim))
#1

print("Len of 1-D array of 1st element from each Row of M_asMatrix: ", \
                  len(M_asMatrix[:, 0]))
#3

#len(M_asMatrix[:, 0][0])
#*** TypeError: object of type 'numpy.int64' has no len()

print("1st Element of list of 1st elements of M_asMatrix: ", \
                  (M_asMatrix[:, 0][0]))
#1

z_asList = [M_asMatrix[:, 0]]

print("\nList z_asList initialized with the 1st Row of M_asMatrix: ", z_asList)
#[array([1, 4, 7])]

# z_asList is a list that has just one element. That element is the 1st row
# of M_asMatrix.
print("type of z_asList: ", type(z_asList))
print("Len of z_asList: ", len(z_asList))

z_asArray = np.asarray(z_asList)

print("Dimension of z_asArray: ",\
      z_asArray.ndim)
#2

print("Shape of z_asArray: ", z_asArray.shape)
#(1, 3)

z_asArray_t = z_asArray.T

print("Transpose of z_asArray: \n", z_asArray_t)
#array([[1],
#       [4],
#       [7]])

print("Shape of z_asArray transpose: ", z_asArray_t.shape)
#(3, 1)

print("\n\tDONE: ", __file__)
