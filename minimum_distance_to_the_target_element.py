'''
Given an integer array nums (0-indexed) and two integers target and start, find an index i such that nums[i] == target and abs(i - start) is minimized. Note that abs(x) is the absolute value of x.

Return abs(i - start).

It is guaranteed that target exists in nums.
'''

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        
        min_res = 100000000
        for i in range(len(nums)):
            
            if nums[i] == target:
                
                cur = abs(i - start)
                if cur < min_res:
                    min_res = cur
                        
        for i in range(len(nums)-1, -1,-1):
            
            if nums[i] == target:
                
                cur = abs(i - start)
                if cur < min_res:
                    min_res = cur
        return min_res
                
                
