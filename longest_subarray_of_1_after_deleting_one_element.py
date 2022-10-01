'''
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
'''

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """There should be no more than one zero in sliding window"""
        start = 0  # left pointer
        end = 0  # right pointer
        count_zeros = 0  # total count of zeros
        max_len = 0

        while end <= len(nums) - 1:  # python offset -1 for index
            if nums[end] == 0:
                count_zeros += 1

            while count_zeros > 1:
                if nums[start] == 0:
                    count_zeros -= 1
                start += 1

            max_len = max(max_len, end - start)
            end += 1

        return max_len
