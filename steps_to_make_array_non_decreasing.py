'''
You are given a 0-indexed integer array nums. In one step, remove all elements nums[i] where nums[i - 1] > nums[i] for all 0 < i < nums.length.

Return the number of steps performed until nums becomes a non-decreasing array.
'''

class Solution(object):
    def totalSteps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s, a, r = [], [0] * len(nums), 0
        for i in range(len(nums) - 1, -1, -1):
            while s and nums[i] > nums[s[-1]]:
                a[i] = max(a[i] + 1, a[s.pop()])
            s.append(i)
            r = max(r, a[i])
        return r
