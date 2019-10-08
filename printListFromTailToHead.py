#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 19:59:47 2019

@author: menglingyan
"""
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None  ###链表的结构要熟

#my edition  先遍历列表元素到栈，栈再弹出
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        lst, lst_back = [], []
        if not listNode:
            return lst
        while listNode:
            lst.append(listNode.val)
            listNode = listNode.next
        while lst:
            lst_back.append(lst.pop())
        return lst_back
    
#edition 1
    def printListFromTailToHead1(self, listNode):
        # write code here
        l = list()
        while listNode:
            l.append(listNode.val)
            listNode = listNode.next
        return l[::-1]     #列表切片和倒序
    
#edition 2 递归
    def printListFromTailToHead(self, listNode): 
    # write code here 
    if listNode is None: 
        return [] 
    return self.printListFromTailToHead(listNode.next) + [listNode.val]  #列表可以直接+