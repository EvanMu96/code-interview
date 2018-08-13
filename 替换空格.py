# Author: Komoriii
# Date: 2018/8/13

# 请实现一个函数，将一个字符串中的每个空格替换成“%20”。
# 例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy

# Solution: 直接用Python字符串的split方法，然后再join
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        result = s.split(' ')
        return '%20'.join(result)