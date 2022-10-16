'''
Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.

Return the positive integer k. If there is no such integer, return -1.
'''


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        a=sorted(set(nums))
        m=0
        for i in nums:
            if -i in a:
                m=max(m,i)
        return m  if m!=0 else -1
