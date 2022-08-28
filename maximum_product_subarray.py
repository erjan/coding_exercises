'''
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.
'''


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
            prevmin = nums[0]
            prevmax = nums[0]
            max_to_n = nums[0]
            min_to_n = nums[0]

            ans = nums[0]

            for i in nums[1:]:
                max_to_n = max(max(prevmax * i , prevmin*i),i)
                min_to_n = min(min(prevmin*i, prevmax*i),i)
                prevmax = max_to_n
                prevmin = min_to_n
                ans = max(ans, max_to_n)
            return ans
