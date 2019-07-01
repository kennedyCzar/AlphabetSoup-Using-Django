#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 17:52:43 2019

@author: kenneth
"""

class Stack(object):
    def __init__(self):
        self.value = []
        self.maximum = []
    
    def maxi(self):
        return self.maximum[-1]
    
    def push(self, value):
        self.value.append(value)
        self.maximum.append(max(value, self.maxi()) if self.maximum else value)
    
    def pop(self):
        self.maximum.pop()
        return self.value.pop()
    
    
