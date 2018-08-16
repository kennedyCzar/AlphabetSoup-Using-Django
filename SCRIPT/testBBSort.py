# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 02:34:40 2018

@author: kennedy

This file is used for unit testing
our sort class
"""
#import required library
from bubblesort import sort, quicksort
import numpy as np

list_np = np.random.random(1000)

list_ex = [23, 34, 54, 12, 65, 23, 65, 78, 65, 28, 34]
#innitialize the class using the list data
c = sort(list_ex)
c.bubblesort()
c.quicksort()

#%% Alphabet soup

from AlphabetSoup import AlphabetSoup


c = AlphabetSoup('gggggggg', 'tgfsdhdgfh')
c.Alphabet()



            
            
            
            
            
            
            
            
            
            
            
            
            
            
    