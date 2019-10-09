#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 10:34:14 2019

@author: menglingyan
"""

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        min = 1000000
        for i in rotateArray:
            if i < min:
                min = i
        return min
    
    
    
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return 0
        else:
            return min(rotateArray)    #返回给定参数的最小值，参数可以为序列
        
        

    def minNumberInRotateArray(self, rotateArray):

        # write code here
        if not rotateArray:
            return 0
        elif len(rotateArray) == 1:
            return rotateArray[0]
        low = 0
        high = len(rotateArray) - 1
            
        while high>low:
            mid = (low+high)//2
            if rotateArray[mid] > rotateArray[high]:
                low = mid + 1
            elif rotateArray[mid] < rotateArray[high]:
                high = mid
            else:    ####此题难点，要注意边界条件
                high = high - 1
        return rotateArray[low]
        
