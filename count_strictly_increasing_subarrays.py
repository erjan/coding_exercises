'''
You are given an array nums consisting of positive integers.

Return the number of subarrays of nums that are in strictly increasing order.

A subarray is a contiguous part of an array.
'''


Intuition
The idea is that the if the current nums[i] > nums[i - 1] so the number of increasing sub-array end at i will be equal to number of increasing sub-array end at i - 1 plus 1

Solution 1: DP Top-down Memoization
Approach
Complexity
Time complexity: O(N)O(N)O(N)
Space complexity: O(N)O(N)O(N)
Code
class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dp(i: int) -> int:
            if i == 0:
                return 1

            if nums[i] > nums[i - 1]:
                return dp(i - 1) + 1
            return 1
        return sum(dp(i) for i in range(1, n)) + 1
Solution 2: DP Bottom-up
Approach
Complexity
Time complexity: O(N)O(N)O(N)
Space complexity: O(N)O(N)O(N)
Code
class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1 for _ in range(n)]
        
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1] + 1
                
        return sum(dp)
Solution 3: DP Bottom-up Optimized Space
Approach
Complexity
Time complexity: O(N)O(N)O(N)
Space complexity: O(1)O(1)O(1)
Code
class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        dp, res = 1, 1
        
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                dp += 1
            else:
                dp = 1
            res += dp
                
        return res
Solution 4: Two-Pointers
Approach
Complexity
Time complexity: O(N)O(N)O(N)
Space complexity: O(1)O(1)O(1)
Code
class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        res, j = 1, 0
        for i in range(1, n):
            if nums[i - 1] >= nums[i]:
                j = i
            res += i - j + 1
        return res
