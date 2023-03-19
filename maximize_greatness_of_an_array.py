'''
You are given a 0-indexed integer array nums. You are allowed to permute nums into a new array perm of your choosing.

We define the greatness of nums be the number of indices 0 <= i < nums.length for which perm[i] > nums[i].

Return the maximum possible greatness you can achieve after permuting nums.
'''

class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int: 
        nums.sort() 
        count = 0
        j = i = 0  
        while j < len(nums):
            if nums[i] < nums[j]:
                count+=1 
                i+=1
            j+=1 
        return count
        
-----------------------------------------------------------------------------
class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        ans=0
        for num in nums:
            if num>nums[ans]:
                ans+=1

        return ans
        
