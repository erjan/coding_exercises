'''
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.
'''


class Solution:
    def numSubarraysWithSum(self, nums: List[int], k: int) -> int:
        
        
        n = len(nums)
        
        pre = [0]*n
        
        pre[0] = nums[0]
        
        for i in range(1,n):
            
            pre[i] = pre[i-1] + nums[i]
        
        
        seen = defaultdict(int)
        
        seen[0] = 1 
        ans = 0 
        
        for i in range(0,n):
            
            val = pre[i] - k 
            
            if(val in seen):
                
                ans += seen[val]
            
            seen[pre[i]] += 1 
        
        
        return ans 
