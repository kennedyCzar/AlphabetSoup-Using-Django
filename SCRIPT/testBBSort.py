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


c = AlphabetSoup('this is what i mean', 'what i really mean')
c.Alphabet()


message =  'this is what i mean'
alphabet = 'what i really mean'
setA = set(message)
setB = set(alphabet)
            
setB.intersection(setA)        
            
#%% TESTING NEW FUNCTION

message = 'UVZQDEQTQZDFMHVMZMFGFIMCJOUJMRYIIRJTORJCCYXWHJTTZFUCEGYCHHZNFEGOXHHTXLFCVQXDFABH'
alphabet = 'RBWGHGDTQJOJGOXFWFMPZDYYDGABTEUZHTHAZOYYXNIPNQDIODQDIZNSKZWZFXVVIRHSGNAQAPHBJPYZNCMLUWVRBOUOWLNJPSLCCHJFBHJBFSYCDVJBCEGM'

import time
def fcn(message, alphabet):
    listA = list(message)
    listB = list(alphabet)
    final = []
    start_time = time.clock()
    while listA != []:
        for msg in listA:
            if msg in listB:
                final.append(msg)
                listA.remove(msg)
                listB.remove(msg)
            elif msg not in listB:
                listA.remove(msg)
        continue
    if sorted(final) == sorted(list(message)):
        return True, final, listA, listB, time.clock() - start_time
    else:
        return False, final, listA, listB, time.clock() - start_time

fcn(message, alphabet)


#def ret():
#    while listA != []:
#        print('yes')
#        break
#    return 'funnish'
#ret()    
            
            
#%% quicksort 

def quicksort(list_seq):
    
    '''
    Arguments:
        @seq: list of intergers
        @Return: A list or array of sorted integers
        
    '''
    #if the list in the array is less than 1 return same
    #no need to sort

    if list_seq is None:
        return []
    elif len(list_seq) <= 1:
        return list_seq
    else:
        pivot_point = list_seq[0]
        left, right = [], []
        for ii in list_seq[1:]:
            if ii < pivot_point:
                left.append(ii)
            else:
                right.append(ii)
    return quicksort(left)+ [pivot_point]+ quicksort(right)
          
quicksort([7,1,6, 3, 0, 1])           
            
            
    