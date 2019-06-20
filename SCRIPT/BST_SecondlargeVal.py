#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 18:44:33 2019

@author: kenneth
"""

'''
Given the root to a binary search tree, 
find the second largest node in the tree.
'''

def largestNode(rootNode):
    currentNode = rootNode
    
    while currentNode:
        if not currentNode.right:
            return currentNode.value
        else:
            currentNode = currentNode.right
            
def secondLargetNode(rootNode):
    if (rootNode is None or (rootNode.left is None and rootNode.right)) :
        return
    else: currentNode = rootNode
    
    while currentNode:
        if largestNode.left and not largestNode.right:
            return largestNode(largestNode.left)
        if currentNode.right and not currentNode.right.left and not currentNode.right.left:
            return currentNode.value
        currentNode = currentNode.right