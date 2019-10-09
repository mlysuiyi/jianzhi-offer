#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 14:30:04 2019

@author: menglingyan
"""
##my edition
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        elif n < 0:
            return None
        elif n > 0 and n <= 2:
            return 1
        else:
            a = 1
            b = 1
            while n-2:
                a, b = b, a+b
                n -= 1
            return b

##edition1
    def Fibonacci(self, n):
        # write code here
        res=[0,1,1,2]
        while len(res)<=n:
            res.append(res[-1]+res[-2])
        return res[n]