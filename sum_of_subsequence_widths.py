'''
The width of a sequence is the difference between the maximum and minimum elements in the sequence.

Given an array of integers nums, return the sum of the widths of all the non-empty subsequences of nums. Since the answer may be very large, return it modulo 109 + 7.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
'''

class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        n = len(nums)
        
        for i in range(n):
            mx = (2**i)*nums[i]
            mn = (2**(n-1-i))*nums[i]
            ans += (mx-mn)
        
        return ans%(10**9+7)
      
------------------------------------------------------------------------------------------
class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        MOD = 1_000_000_007
        nums.sort()
        ans = val = 0 
        p = 1
        for i in range(1, len(nums)): 
            p = p * 2 % MOD
            val = (2*val + (nums[i]-nums[i-1])*(p-1)) % MOD 
            ans = (ans + val) % MOD 
        return ans 
      
------------------------------------------------------------------------------------------------------------
class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        nums.sort()

        dp = [0] * n

        p = 2
        temp = nums[0]

        for i in range(1, n):
            dp[i] = ((dp[i-1] + ((p-1)*nums[i])%MOD)%MOD - temp)%MOD
            p = (2*p)%MOD
            temp = ((2*temp)%MOD + nums[i])%MOD
        
        return dp[n-1]
