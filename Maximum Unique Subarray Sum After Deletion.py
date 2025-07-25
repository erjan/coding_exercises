'''
You are given an integer array nums.

You are allowed to delete any number of elements from nums without making it empty. After performing the deletions, select a subarray of nums such that:

All elements in the subarray are unique.
The sum of the elements in the subarray is maximized.
Return the maximum sum of such a subarray.
'''

---------------------------
#my own solution:
class Solution:
    def maxSum(self, nums: List[int]) -> int:


        negs = [x for x in nums if x <0]

        if len(negs) == len(nums):
            return max(negs)
        if len(nums) == 1:
            return sum(nums)

        n = len(nums)


        nums = list(set(nums))

        res = sum([x for x in nums if x > 0])
        return res

---------------------------------------------------------------  
