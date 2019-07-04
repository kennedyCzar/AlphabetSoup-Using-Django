#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 21:28:24 2019

@author: kenneth
"""

'''
This problem was asked by Microsoft.
Given the root to such a binary tree, 
write a function to evaluate it.

    *
   / \
  +    +
 / \  / \
3  2  4  5
'''
class Node(object):
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
    
    @staticmethod
    def evaluateExpression(root):
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return int(root.data)
        else:
            #recursively call all left and right roots.
            leftTree = Node.evaluateExpression(root.left)
            rightTree = Node.evaluateExpression(root.right)
            
            if root.data == '+':
                return leftTree + rightTree
            elif root.data == '-':
                return leftTree - rightTree
            elif root.data == '*':
                return leftTree * rightTree
            else:
                return leftTree / rightTree
    

if __name__ == '__main__':
    root = Node('*')
    root.left = Node('+')
    root.left.left = Node('3')
    root.left.right = Node('2')
    root.right = Node('+')
    root.right.left = Node('4')
    root.right.right = Node('5')
    print('Result: %s'%(Node.evaluateExpression(root)))