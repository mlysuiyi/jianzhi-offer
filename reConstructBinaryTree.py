#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 20:56:21 2019

@author: menglingyan
"""
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        else:
            root = pre[0]
            d = tin.index(root)
            print(d)
            tree = TreeNode(root)
            tree.left = self.reConstructBinaryTree(pre[1:d+1],tin[:d])
            tree.right = self.reConstructBinaryTree(pre[d+1:],tin[d+1:])
        return tree