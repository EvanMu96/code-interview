class Solution:
    """
    @param n: The number of digits
    @return: All narcissistic numbers with n digits
    """
    def getNarcissisticNumbers(self, n):
        # write your code here
        ans = []
        if len(n) == 0:
            return []
        for number in n:
            power = len(str(number))
            power_sum = 0
            for digit in list(str(number)):
                power_sum += int(digit)**power
            if power_sum == number:
                ans.append(number)
        return ans

sln = Solution()
print(sln.getNarcissisticNumbers([1,2,3,4,5,6,1634, 1635]))