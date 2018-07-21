# coding: utf-8
import numpy as np

B = np.asarray([[5],[5]])
A = np.asarray([[1, 2], [3, 4]])
print("A:\n", A)
print("B:\n", B)
print("A + B: \n", A + B)
print("B.T:\n",B.T)
print("A + B.T: \n", A + B.T)

B = np.asarray([[5, 10],[5, 10]])
print("A + B: \n", A + B)
print("B.T:\n",B.T)
print("A + B.T: \n", A + B.T)
