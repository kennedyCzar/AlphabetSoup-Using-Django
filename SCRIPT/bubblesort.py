# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 01:24:46 2018

@author: kennedy
"""


"""
Bubble sort algorithm
--------------------------
Naive sorting algorithm that compares and swap integers in ascending order
Time Cmomplexity: O(n**2) --> Worst case
Space complexity: O(1)

Quick sort algorithm
------------------------------
Uses partitioning or recursive divide and conquer of the list
Time Cmomplexity: O(n**2)
Space complexity: O(n**2)

"""
import time
class sort(object):
    def __init__(self, list_seq):
        '''
        Argument:
            @self: refer to the init argument
            @list_seq: refer to the list of array we want to sort
            @Return: list or array of sorted integers.
        '''
        self.list_seq = list_seq
        
    def bubblesort(self):
        #check the size of the list
        self.start_time = time.clock()
        for ii in range(len(self.list_seq)):
            #check each elements of the array 
            for n in range(1, len(self.list_seq) - ii):
                #perform a loop...Check if the Nth number is bigger than the Nth - 1 number after it
                if self.list_seq is None:
                    raise('Empty list or array')
                if self.list_seq[n] <= 1:
                    self.list_seq
                elif self.list_seq[n] <= self.list_seq[n - 1]: 
                    #if so...swap the Nth and last number N- 1
                    self.list_seq[n- 1], self.list_seq[n] = self.list_seq[n], self.list_seq[n - 1]
        return self.list_seq, 'Running time {}secs'.format(time.clock() - self.start_time)
    
    
class quicksort(object):
    
    def __init__(self, list_seq):
        '''
        Argument:
            @self: refer to the init argument
            @list_seq: refer to the list of array we want to sort
            @Return: list or array of sorted integers.
        '''
        self.list_seq = list_seq
        
    def quicksort(self):
        
        '''
        Arguments:
            @seq: list of intergers
            @Return: A list or array of sorted integers
            
        '''
        #if the list in the array is less than 1 return same
        #no need to sort
        if self.list_seq is None:
            raise('Empty array')
        elif len(self.list_seq) <= 1:
            return self.list_seq
        else:
            self.middle_point = self.list_seq[0]
            self.left, self.right = [], []
            for ii in self.list_seq[1:]:
                if ii < self.middle_point:
                    self.left.append(ii)
                else:
                    self.list_seq.append(ii)
        return self.quicksort(self.left), [self.middle_point], self.quicksort(self.right)
                    
                    


            
