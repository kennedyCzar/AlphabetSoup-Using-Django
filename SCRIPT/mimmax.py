#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 13:09:07 2019

@author: kenneth
"""


def minmax(array):
    '''
    :param: array: array or list
    :returntype: minimum and maximum value
    : Time complexity: O(N*logN)
    : Space complexity: O(1)
    
    ex:
    >> ls = [1, 34, 53, 64, 21, 64, 12, 43, 42]
    >> min, max = minmax(ls)
    >> 1
    >> 64
    '''
    minval = array[0]
    maxval = array[0]
    for ii in array:
        if ii < minval:
            minval = ii
        elif ii > maxval:
            maxval = ii
    return minval, maxval

ls = [1, 34, 53, 64, 21, 64, 12, 43, 42]       
minval, maxval = minmax(ls)
