'''
Given an integer array nums, return 
true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. 
If no such indices exists, return false.
'''

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        if len(nums) < 3:return False
        
        i = float('inf')
        j = float('inf')
        
        for ind in range(len(nums)):
            if nums[ind] <=i:
                i = nums[ind]
            elif nums[ind] <=j:
                j = nums[ind]
            else:
                return True
        return False
            
-----------------------------------------------------------
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # we can use two thresholds to divide the subsquence length
        # everything between threshold1 and threshold2 will form doublets
        # everything above threshold2 will form a triplet
        # dynamically change these two thresholds
        
        threshold1 = threshold2 = float("inf")
        for num in nums:
            # lower threshold1
            if num <= threshold1:
                threshold1 = num
            # lower threshold2
            elif num <= threshold2:
                threshold2 = num
            # if greater than both thresholds (note equal doesn't count)
            else:
                return True
        return False
