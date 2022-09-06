
'''
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.
'''

class Solution:
    def jump(self, nums: List[int]) -> int:
        
        
        res = 0
        
        l = 0
        r = 0
        
        while r < len(nums)-1:
            
            farthest = 0
            for i in range(l,r+1):
                
                farthest = max(farthest, i + nums[i])
            
            l = r+1
            r = farthest
            res+=1
        return res
-------------------------------------------------------------------------
def jump(nums):
	x = 0
	F = [len(nums)+1]*len(nums)
	F[0] = 0
	for i in range(1, len(nums)):
		while x + nums[x] < i:
			x += 1
		F[i] = min(F[i], F[x]+1)
	return F[-1]
-----------------------------------------------------------------------------------
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        dp= [0] * n        
        j=0
        for i in range(1,len(dp)):
            while j + nums[j] < i:
                j += 1
            dp[i] = dp[j] + 1
        return dp[-1] 
