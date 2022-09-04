'''
Given a 0-indexed integer array nums, determine whether 
there exist two subarrays of length 2 with equal sum. Note that the two subarrays must begin at different indices.

Return true if these subarrays exist, and false otherwise.

A subarray is a contiguous non-empty sequence of elements within an array.
'''


class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        
        for i in range(len(nums)-2):
            first = nums[i] + nums[i+1]

            for j in range(i+1, len(nums)-1):
                second = nums[j] + nums[j+1]
                if first == second:
                    return True
        return False
-----------------------------------------------------------------------------

class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        sums = set()
        
        for i in range(len(nums)-1):
            t = nums[i]+nums[i+1]
            if t in sums:
                return True
            else:
                sums.add(t)
            
        return False
