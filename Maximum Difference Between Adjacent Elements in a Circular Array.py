
Given a circular array nums, find the maximum absolute difference between adjacent elements.

Note: In a circular array, the first and last elements are adjacent.



class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        nums.append(nums[0])

        res = 0

        for i in range(len(nums)-1):
            cur = nums[i]
            c = nums[i+1]
            res = max(res, abs(cur-c))
        return res
