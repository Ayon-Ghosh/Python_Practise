# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 15:45:43 2019

@author: 140524
"""

# Matrix:
# =============================================================================
# 
# https://www.mathsisfun.com/algebra/matrix-multiplying.html
# https://www.geeksforgeeks.org/numpy-dot-python/
# =============================================================================

#https://medium.com/@ian.dzindo01/what-is-numpy-newaxis-and-when-to-use-it-8cb61c7ed6ae

#1D array
import numpy as np
arr = np.arange(4)
arr
arr.shape

#reshape
arr1 = arr.reshape(1,-1)
arr1

arr2 = arr.reshape(-1,1)
arr2


# make it as row vector by inserting an axis along first dimension
row_vec = arr[np.newaxis, :]
row_vec
row_vec.shape


# make it as column vector by inserting an axis along second dimension
col_vec = arr[:, np.newaxis]
col_vec
col_vec.shape

# reshape(1,-1) is same as using arr[np.newaxis, :]
# reshape(-1,1) is same as using arr[:, np.newaxis]

# adding the 2 differnt length arrays

x1 = np.array([1, 2, 3, 4, 5])
x2 = np.array([5, 4, 3])
x1_new = x1[:, np.newaxis]
x1_new
x1_new + x2