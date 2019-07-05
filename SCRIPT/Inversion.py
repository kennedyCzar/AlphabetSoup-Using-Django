#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 15:27:33 2019

@author: kenneth
"""

def inversion(x):
    '''
    param: x: list or array of distinct numbers
    Time complexity: O(N^2)
    
    ex.
    >> x = [1, 2, 3, 4, 5]
    >> inversion(x)
    >> 0
    >> [2, 4, 1, 3, 5]
    >> inversion(x)
    >> 3
    >> [5, 4, 3, 2, 1]
    >> 10
    '''
    inversions = 0
    for ii in range(len(x)):
        for ij in range(ii+1, len(x)):
            if x[ii] > x[ij]: inversions+=1
    
    return inversions

x = [5, 4, 3, 2, 1]
inversion(x)
