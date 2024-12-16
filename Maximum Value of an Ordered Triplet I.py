
'''
You are given a 0-indexed integer array nums.

Return the maximum value over all triplets of indices (i, j, k) such that i < j < k. If all such triplets have a negative value, return 0.

The value of a triplet of indices (i, j, k) is equal to (nums[i] - nums[j]) * nums[k].
'''


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0

        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1,n):
                    res = max(res, (nums[i]-nums[j])*nums[k])
        return res
------------------------------------------------------------------------
class Solution:
    def maximumTripletValue(self, A: List[int]) -> int:
        res = maxa = maxab = 0
        for a in A:
            res = max(res, maxab * a)
            maxab = max(maxab, maxa - a)
            maxa = max(maxa, a)
        return res        
