# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        arr_length = len(rotateArray)
        if arr_length==0:
            return 0
        min_val = rotateArray[0]
        for i in range(arr_length)[::-1]:
            if rotateArray[i]<=min_val:
                min_val = rotateArray[i]
            else:
                return min_val
        return min_val