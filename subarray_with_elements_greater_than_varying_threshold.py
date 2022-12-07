'''
You are given an integer array nums and an integer threshold.

Find any subarray of nums of length k such that every element in the subarray is greater than threshold / k.

Return the size of any such subarray. If there is no such subarray, return -1.

A subarray is a contiguous non-empty sequence of elements within an array.
'''

class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:

        nums.append(0)
        nums.insert(0,0)
        stack = []

        for i in range(len(nums)):

            while stack and nums[stack[-1]] > nums[i]:
                h = nums[stack.pop()]
                if not stack:
                    continue
                k = i-stack[-1]-1
                if h > threshold//k:
                    return k
            stack.append(i)
        return -1
