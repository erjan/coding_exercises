'''
You are given an integer array nums where the largest integer is unique.

Determine whether the largest element in the array is at least twice as
much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.
'''

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
        m = max(nums)
        print('max %d' % m)
        for i in range(len(nums)):
            if nums[i] != m:
                if 2 * nums[i] > m:
                    return -1
        return nums.index(m)
