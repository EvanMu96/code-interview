# -*- coding:utf-8 -*-
class Solution:
     
    def Fibonacci(self, n):
        # write code here
        f, g = 1, 0
        while (n>0):
            g+=f
            f=g-f
            n = n-1
        return g