#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 20:22:20 2019

@author: kenneth
"""

color = ['G', 'G', 'G', 'R', 'R', 'R', 'B', 'B']

def sort_colr(color):
    '''
    params: color: string of characters
    return type: sorted string
    
    ex: sort_colr(color)
    >> ['B', 'B', 'G', 'G', 'G', 'R', 'R', 'R']
    
    ex: sort_colr(color)[::-1]
    >> ['R', 'R', 'R', 'G', 'G', 'G', 'B', 'B']
    '''
    if not color:
        return []
    else:
        return (sort_colr([x for x in color[1:] if x < color[0]]) + [color[0]] +\
                sort_colr([x for x in color[1:] if x>= color[0]]))
        