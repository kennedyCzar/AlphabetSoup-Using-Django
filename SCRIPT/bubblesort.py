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
Time Cmomplexity: O(N*LogN)
Space complexity: O(1)

"""
import time
class bubblesort(object):
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
    
    
class Qksort:
        
    def quicksort(list_seq):
        
        '''
        Arguments:
            @seq: list of intergers
            @Return: A list or array of sorted integers
            
        '''
        #if the list in the array is less than 1 return same
        #no need to sort
        
        start_time = time.clock()
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
        #return time.clock() - start_time
        return Qksort.quicksort(left)+ [pivot_point]+ Qksort.quicksort(right)
                    

class BinarySearch(object):
    def __init__(self, sequence):
        self.sequence = sequence
        
    def Divide_and_conquer(self):
        '''Arguments:
            Sequence: sequence of integers to search
            element: element to search for in the sequence
            
        Complexity:
            Time: O(logN)
            Space: O(1)
        '''
        self.low = 0
        self.high = len(self.sequence) - 1
        
        self.start_time = time.clock()
        while self.low <= self.high:
            mid = (self.low + self.high) // 2
            
            if self.sequence[mid] < mid:
                self.low = mid + 1
            elif self.sequence[mid] > mid:
                self.high = mid - 1
            else:
                return self.sequence[mid], time.clock() - self.start_time
        return 'key not found'
    
    def Naive_code(self):
        '''
        Argument:
            takes a sequence number
            
        Complexity:
            Time: O(N)
            Space: O(1)
        '''
        self.start_time = time.clock()
        for seq_no in range(len(self.sequence)):
            if self.sequence[seq_no] == seq_no:
                return self.sequence[seq_no], time.clock() - self.start_time
        return 'key not found'

#%% test quicksort                 
A = [-2, -1, 2, 4, 8]
Qksort.quicksort([3, 6, 8, 2, 4])
bubblesort([3, 6, 8, 2, 4]).bubblesort()
BinarySearch(A).Divide_and_conquer()
BinarySearch(A).Naive_code()

'''
Compare perfomance:
    
    Qksort.quicksort([3, 6, 8, 2, 4])
    Out[69]: 1.9753092601604294e-06
    
   bubblesort([3, 6, 8, 2, 4]).bubblesort()
   Out[96]: ([2, 3, 4, 6, 8], 'Running time 9.086423688131617e-06secs') 
   
Conclusion:
            Shows from the output that QuickSort is almost
            9X faster than bubblesort. Meaning Bubblesort took 
            9X the time to sort the numbers.
            So for deployment you could employ divide and conquer 
            in design of your algorithm.

BinarySearch(A).Divide_and_conquer()
Out[64]: (2, 1.5802462892854165e-06)

BinarySearch(A).Naive_code()
Out[65]: (2, 2.7654310059688214e-06)        
    
'''















