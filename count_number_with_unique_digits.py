'''
Given an integer n, return the count of all numbers with unique digits, x, where 0 <= x < 10n.
'''

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        ans, choices, k = 10, 9, 9

        for m in range(2, n + 1):
            choices *= k
            ans += choices
            k -= 1

        return ans
      
------------------------------------
def countNumbersWithUniqueDigits(self, n):
    if not n:
        return 1
    dp = [0]*(n)
    dp[0] = 9
    for i in range(1,n):
        dp[i] = dp[i-1]*(10-i)
    return sum(dp)+1
    """
    :type n: int
    :rtype: int
    """
