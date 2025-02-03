You are given an array of integers nums. Return the length of the longest  subarray of nums which is either strictly increasing or strictly decreasing.

-----------------------------------------
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        inc = 1
        dec = 1
        if n == 1:
            return 1

        for i in range(1,n):
            if nums[i]>nums[i-1]:
                inc+=1
                dec = 1
            elif nums[i]<nums[i-1]:
                inc = 1
                dec +=1
            else:
                inc = 1
                dec = 1

            res =max(res, dec,inc)
        return res
