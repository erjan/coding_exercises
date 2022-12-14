'''
Given an integer array nums, return the sum of floor(nums[i] / nums[j]) for all pairs of indices 0 <= i, j < nums.length in the array. Since the answer may be too large, return it modulo 109 + 7.

The floor() function returns the integer part of the division.
'''


class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        nums.sort()
        res, mod, cache = 0, 1000000007, {}
        for idx, num in enumerate(nums):
            if num in cache:
                res += cache[num]
            else:
                currentRes, j = 0, idx
                while j < len(nums):
                    multiplier = nums[j] // num
                    lastPosition = bisect_left(nums, num * (multiplier + 1), j)
                    currentRes += (lastPosition - j) * multiplier
                    j = lastPosition
                cache[num] = currentRes
                res += currentRes
            res %= mod
        return res
      
      
-------------------------------------------------------------------------------------------
class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        ans, hi, n, c = 0, max(nums)+1, len(nums), Counter(nums)
        pre = [0] * hi
        for i in range(1, hi):
            pre[i] = pre[i-1] + c[i]
        for num in set(nums):
            for i in range(num, hi, num):
                ans += c[num] * (pre[-1] - pre[i-1])
        return ans % (10**9 + 7)
