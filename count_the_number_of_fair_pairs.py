'''
Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.

A pair (i, j) is fair if:

0 <= i < j < n, and
lower <= nums[i] + nums[j] <= upper
'''


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def countLess(val: int) -> int:
            res, j = 0, len(nums) - 1
            for i in range(len(nums)):
                while i < j and nums[i] + nums[j] > val:
                    j -= 1
                res += max(0, j - i)
            return res
        nums.sort()
        return countLess(upper) - countLess(lower - 1)
      
-------------------------------------------------------------------------------------------
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # First, note that the answer does not change if we sort the array
        nums.sort()
        fairCtr = 0
        for i in range(len(nums)):
            # For each index find the left and right elements for which the sums lie between lower and upper
            l = bisect_left(nums, lower - nums[i])
            r = bisect_right(nums, upper - nums[i])
            fairCtr += (r - l)
            # check if index i lies in the interval, subtract one (we don't want to double count index i)
            if l <= i < r:
                fairCtr -= 1
        return fairCtr // 2
      
------------------------------------------------------------------
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans = 0 
        lo = hi = len(nums)-1
        for i, x in enumerate(nums): 
            while 0 <= hi and x + nums[hi] > upper: hi -= 1
            while 0 <= lo and x + nums[lo] >= lower: lo -= 1
            ans += hi - lo 
            if lo < i <= hi: ans -= 1
        return ans//2
