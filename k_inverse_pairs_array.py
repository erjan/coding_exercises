'''
For an integer array nums, an inverse pair is a pair of integers [i, j] where 0 <= i < j < nums.length and nums[i] > nums[j].

Given two integers n and k, return the number of different arrays consist of numbers from 1 to n such that there are exactly k inverse pairs. Since the answer can be huge, return it modulo 109 + 7.
'''


class Solution(object):
    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        dp = [[0] * (k+1) for _ in range(n+1)]
        dp[0][0] = 1
        
        for i in range(1, n+1):
            cumsum = 0
            for j in range(k+1):
                if j == 0:
                    dp[i][j] = 1
                    cumsum += 1
                else:
                    cumsum += dp[i-1][j]
                    if j-i >= 0:    # basically sliding window
                        cumsum -= dp[i-1][j-i]
                    dp[i][j] = cumsum % 1000000007
    
        return dp[n][k]
