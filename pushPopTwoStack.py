#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 09:57:09 2019

@author: menglingyan
"""
#my edition
class Solution:
    def __init__(self):
        self.Astack = []
        self.Bstack = []
        
    def push(self, node):
        # write code here
        self.Astack.append(node)    #append后面括号内要加元素
        
    def pop(self):
        # return xx
        if not self.Bstack:    #要多种情况分析，不能只符合编译通过
            while self.Astack:
                self.Bstack.append(self.Astack.pop())
        return self.Bstack.pop()
    
    
#edition1
class Solution:
    def __init__(self):
        self.stackA = []
        self.stackB = []
         
    def push(self, node):
        # write code here
        self.stackA.append(node)
         
    def pop(self):
        # return xx
        if self.stackB:
            return self.stackB.pop()
        elif not self.stackA:
            return None
        else:
            while self.stackA:
                self.stackB.append(self.stackA.pop())
            return self.stackB.pop()