'''
Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.
'''

#bottom up
class Solution:
    def combinationSum4(self, N: List[int], T: int) -> int:
        dp = [0] * (T + 1)
        dp[0] = 1
        for i in range(T):
            if not dp[i]: continue
            for num in N:
                if num + i <= T: dp[i+num] += dp[i]
        return dp[T]
      
----------------------------------------------------------------------------      
#top down 

class Solution:
    def combinationSum4(self, N: List[int], T: int) -> int:
        dp = [0] * (T + 1)
        dp[0] = 1
        for i in range(1, T+1):
            for num in N:
                if num <= i: dp[i] += dp[i-num]
        return dp[T]
