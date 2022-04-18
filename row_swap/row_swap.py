# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 11:41:45 2022

@author: liaoyuxuan
"""
import numpy as np

A = np.arange(25).reshape(5,5)
print(A)
A[0,:] = A[4,:]
print(A)
