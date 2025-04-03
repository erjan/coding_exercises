'''
You are given a 0-indexed integer array nums.

Return the maximum value over all triplets of indices (i, j, k) such that i < j < k. If all such triplets have a negative value, return 0.

The value of a triplet of indices (i, j, k) is equal to (nums[i] - nums[j]) * nums[k].
'''

-----------------------------
#same solution but TLE if you do bruteforce - i did it yesterday, on 2 april 2025 , easy version with easy constraints
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)

        bestdiff = 0
        max_i = 0
        res = 0

        for i in range(n):

            res = max(res, bestdiff * nums[i] )

            bestdiff = max(bestdiff, max_i -nums[i])

            max_i = max(max_i,  nums[i])
        
        return res
