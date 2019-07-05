#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 17:41:29 2019

@author: kenneth
"""

def maxProfit(x):
    '''Docstring
    This problem was asked by Facebook.
    
    Given a array of numbers representing 
    the stock prices of a company in chronological order, 
    write a function that calculates the maximum profit 
    you could have made from buying and selling 
    that stock once. You must buy before you can sell it.
    
    :param: x: list of stock prices from day 0...n
    :return type: maxprofit with buy/sell price
    
    Time: O(N**2). Can be better than O(N**2). 
                    In linear time maybe.
        
    ex:
    >> x =  [100, 180, 260, 310, 40, 535, 695]
    >> maxProfit(x)
    >> 'buy @40USD :: profit :655USD'
    >>  x =  [695, 180, 260, 310, 40, 535, 100]
    >> 'sell @695USD :: profit :655USD'
    '''
    maxprofit = 0
    buy = 0
    endBuy = 0
    sell = 0
    for ii in range(len(x)):
        for ij in range(ii+1, len(x)):
            if (x[ij] - x[ii]) > maxprofit:
                maxprofit = x[ij] - x[ii]
                buy = x[ii]
                endBuy = x[ij]
            elif abs(x[ii] - x[ij]) > maxprofit:
                maxprofit = abs(x[ii] - x[ij])
                sell = x[ii]
    if abs(buy - endBuy) == maxprofit:
        return 'buy @{}USD :: profit :{}USD'.format(buy, maxprofit)
    else:
        return 'sell @{}USD :: profit :{}USD'.format(sell, maxprofit)

       
        
        
        
        
        
        
        
        
        
        
        
        
        
