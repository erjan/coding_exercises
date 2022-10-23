'''
Given an integer array nums, return the number of subarrays filled with 0.

A subarray is a contiguous non-empty sequence of elements within an array.
'''

def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans, count = 0, 0
        for num in nums:
            if num:
                count = 0
            else:
                count += 1
            ans += count
        
        return ans
      
---------------------------------------------------------------------------------------
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans, currentCountOF0 = 0, 0
        for num in nums:
            if num == 0:
                currentCountOF0 += 1
                ans += currentCountOF0
            else:
                currentCountOF0 = 0
        return ans
