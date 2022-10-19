'''
Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

Return the maximum product you can get.
'''

class Solution(object):
    def integerBreak(self, n):
        if n == 2 or n == 3:
            return n - 1
        if n % 3 == 0:
            return 3**(n/3)
        if n % 3 == 1:
            return 3**(n/3 - 1)*4
        if n % 3 == 2:
            return 3**(n/3)*2
          
---------------------------------------------------------------
class Solution(object):
    def integerBreak(self, n):
        dp = [None, 1]
        for m in range (2, n + 1):
            j = m - 1
            i = 1
            max_product = 0
            while i <= j:
                max_product = max(max_product, max(i, dp[i]) * max(j, dp[j]))
                j -= 1
                i += 1
            dp.append(max_product)
        return dp[n]
