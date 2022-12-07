'''
You are given an integer array nums and an integer goal.

You want to choose a subsequence of nums such that the sum of its elements is the closest possible to goal. That is, if the sum of the subsequence's elements is sum, then you want to minimize the absolute difference abs(sum - goal).

Return the minimum possible value of abs(sum - goal).

Note that a subsequence of an array is an array formed by removing some elements (possibly all or none) of the original array.
'''



class Solution:
    def solve(self, nums, i, val, sums):
        if i == len(nums):
            sums.append(val)
            return
        self.solve(nums, i+1, val+nums[i], sums)
        self.solve(nums, i+1, val, sums)
        
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        sum1, sum2 = [], []
        self.solve(nums[:n//2], 0, 0, sum1)
        self.solve(nums[n//2:], 0, 0, sum2)
        
        sum2 = sorted(sum2)
        #print(sum1, sum2)
        n2 = len(sum2)
        ans = float("inf")
        for s in sum1:
            rem = goal-s
            i = bisect_left(sum2, rem)
            if i < n2:
                ans = min(ans, abs(rem-sum2[i]))
            if i > 0:
                ans = min(ans, abs(rem-sum2[i-1]))
        return ans
      
---------------------------------------------------------------------------------
class Solution:
    def solve(self, nums, i, val, sums):
        if i == len(nums):
            sums.append(val)
            return
        self.solve(nums, i+1, val+nums[i], sums)
        self.solve(nums, i+1, val, sums)
        
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        sum1, sum2 = [], []
        self.solve(nums[:n//2], 0, 0, sum1)
        self.solve(nums[n//2:], 0, 0, sum2)
        
        sum2 = sorted(sum2)
        #print(sum1, sum2)
        n2 = len(sum2)
        ans = float("inf")
        for s in sum1:
            rem = goal-s
            i = bisect_left(sum2, rem)
            if i < n2:
                ans = min(ans, abs(rem-sum2[i]))
            if i > 0:
                ans = min(ans, abs(rem-sum2[i-1]))
        return ans
