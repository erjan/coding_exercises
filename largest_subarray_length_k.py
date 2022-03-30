'''
An array A is larger than some array B if for the first index i where A[i] != B[i], A[i] > B[i].

For example, consider 0-indexing:

[1,3,2,4] > [1,2,2,4], since at index 1, 3 > 2.
[1,4,4,4] < [2,1,1,1], since at index 0, 1 < 2.
A subarray is a contiguous subsequence of the array.

Given an integer array nums of distinct integers, return the largest subarray of nums of length k.
'''


class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
           
        nums_trunc = nums[: len(nums)-k+1]
        largest = max(nums_trunc)

        ind_large = nums.index(largest)
        return nums[ind_large: ind_large+k]
