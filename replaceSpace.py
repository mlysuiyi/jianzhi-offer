# -*- coding:utf-8 -*-
#my edition
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        new_s = []
        for each in s:
            if each != ' ':
                new_s.append(each)
            else:
                new_s.append('%20')
        return ''.join(new_s)  #join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串 str.join(sequence)
    
#edition 1
    def replaceSpace1(self, s):
        # write code here
        s = list(s)
        count=len(s)
        for i in range(0,count):
            if s[i]==' ':
                s[i]='%20'
        return ''.join(s)
    
#edtion 2
    def replaceSpace2(self, s):
        # write code here
        res = ''
        for ele in s:
            if ele.strip():    #.strip()去掉收尾空格字符，当if后面为''中什么也没有时，为false
                res += ele
            else:
                res += '%20'
        return res
    
#edition 3
    def replaceSpace3(self, s):
        return s.replace(" ", "%20") #返回字符串中的 old（旧字符串） 替
    #换成 new(新字符串)后生成的新字符串，如果指定第三个参数max，则替换不超过 max 次。
    #str.replace(old, new[, max])