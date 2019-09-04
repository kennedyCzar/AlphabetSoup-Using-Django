#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 11:33:30 2019

@author: kenneth
"""
#--Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __repr__(self):
        return repr(self.data)

#--Singly linked list      
class Linkedlist(object):
    def __init__(self):
        self.head = None
    
    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(repr(current))
            current = current.next
        return '[' + ','.join(nodes)+']'
    
    def push(self, data):
        '''
        :param: new insertion data
        :Complexity: Time: O(1)
        '''
        newData = Node(data)
        newData.next = self.head
        self.head = newData
        
    def insertbetween(self, prev, data):
        '''
        :param: new insertion data
        :Complexity: Time: O(1)
        '''
        newData = Node(data)
        newData.next = prev.next
        prev.next = newData
    
    def append(self, data):
        '''
        :param: new insertion data
        :Complexity: Time: O(1)
        '''
        if not self.head:
            self.head = Node(data)
        final = self.head
        while final.next:
            final = final.next
        final.next = Node(data)
            
    def find(self, data):
        '''
        param: data: key to find
        :return data is present else None
        '''
        current = self.head
        while current and current.data != data:
            current = current.next
        return current
    
    def remove(self, data):
        '''
        param: data: key to remove
        '''
        current, prev = self.head, None
        while current and current.data != data:
            prev = current
            current = current.next
        if prev is None:
            self.head = current.next
        elif current:
            prev.next = current.next
            current.next = None
        return
    
            
#%%     
        
        
ll = Linkedlist()
ll.push(1)
ll.push(2)
ll.push(3)
print(ll)





