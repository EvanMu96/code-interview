# Author: Komoriii
# Date: 2018/8/13

'''
Question:
在一个二维数组中（每个一维数组的长度相同），每一行都按照从
左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个
函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''

# Solution1: 不适用递增递减条件直接O(n^2)查找
class Solution1:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if not array:
            return False
        
        len_x = len(array)
        len_y = len(array[0])
        
        if (len_x<=0) or (len_y <=0 ):
            return False
        
        for cow in array:
            for i in range(len_y):
                if cow[i]== target:
                    return True

# Solution2: 从二位数组的(0,len_y-1)开始，每次与左下角的元素对比

class Solution2:
    def Find(self, target, array):
        # write your code
        if not array:
            return False
        
        len_x = len(array)
        len_y = len(array[0])

        cur_x = 0
        cur_y = len_y-1

        while((cur_x<len_x) and (cur_y>=0)):
            if target<array[cur_x][cur_y]:
                cur_y = cur_y - 1
            elif target>array[cur_x][cur_y]:
                cur_x = cur_x + 1
            elif array[cur_x][cur_y]==target:
                return True
        return False
            