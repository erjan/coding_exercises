'''

In combinatorial mathematics, a derangement is a permutation of the elements of a set, such that no element appears in its original position.

You are given an integer n. There is originally an array consisting of n integers from 1 to n in ascending order, return the number of derangements it can generate. Since the answer may be huge, return it modulo 109 + 7.
'''

class Solution:
    def findDerangement(self, n: int) -> int:
        """
        O(n) time complexity
        O(n) array of size n
        """
        if n == 0: return 1
        if n == 1: return 0
        dp = [0]*(n + 1)
        dp[0] = 1
        dp[1] = 0
        for i in range(2, n + 1):
            dp[i] = (i - 1)*(dp[i - 1] + dp[i - 2]) % 1000000007
        return dp[n]
