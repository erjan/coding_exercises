'''
You are given a 0-indexed array of positive integers nums. Find the number of triplets (i, j, k) that meet the following conditions:

0 <= i < j < k < nums.length
nums[i], nums[j], and nums[k] are pairwise distinct.
In other words, nums[i] != nums[j], nums[i] != nums[k], and nums[j] != nums[k].
Return the number of triplets that meet the conditions.
'''


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:

        res = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):

                for k in range(j+1, n):

                    if nums[i]!= nums[j] and nums[i]!=nums[k]and nums[j]!=nums[k]:
                        res+=1
        return res
