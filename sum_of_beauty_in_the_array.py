'''
You are given a 0-indexed integer array nums. For each index i (1 <= i <= nums.length - 2) the beauty of nums[i] equals:

2, if nums[j] < nums[i] < nums[k], for all 0 <= j < i and for all i < k <= nums.length - 1.
1, if nums[i - 1] < nums[i] < nums[i + 1], and the previous condition is not satisfied.
0, if none of the previous conditions holds.
Return the sum of beauty of all nums[i] where 1 <= i <= nums.length - 2.
'''

class Solution:
    """
    approach: 
    create two arrays prefix and suffix array
    prefix[i] records the maximum value in range (0, i - 1) inclusive.
    suffix[i] records the minimum value in range (i + 1, n - 1) inclusive.
    """
    def sumOfBeauties(self, nums: List[int]) -> int:
        prefix = [float('-inf') for _ in range(len(nums))]
        suffix = [float('inf') for _ in range(len(nums))]
        for i in range(1, len(nums)):
            prefix[i] = max(nums[i-1], prefix[i-1])
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = min(nums[i+1], suffix[i+1])
        pts = 0
        for i in range(1, len(nums)-1):
            if prefix[i] < nums[i] < suffix[i]:
                pts += 2
            elif nums[i-1] < nums[i] < nums[i+1]:
                pts += 1
        return pts
      
---------------------------------------------------------------------------------------------------------------
Question: The beauty of nums[i] equals 2, if nums[j] < nums[i] < nums[k], for all 0 <= j < i and for all i < k <= nums.length - 1.

Explanation:

In simpler terms, for each index from 1 till n-2,

All the values left of ith index should be less than ith index's value.
All the values right of ith index should be greater than ith index's value.
We create two dp arrays

max_dp - computation starts from start of array (index 0) - to keep track of maximum value of array from index 0 till ith index
min_dp - computation starts from end of array (index n-1) - to keep track of minimum value of array from n-1 index till ith index
With max_dp, we can find if all values in left side are smaller - if max_dp[i] > max_dp[i-1]
With min_dp, we can find if all values in right side are greater - if nums[i] < min_dp[i+1]

The second condition nums[i-1] < nums[i] < nums[i+1] is self explanatory

Code:

class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        max_dp = [0] * n
        min_dp = [float(inf)] * n
        max_dp[0] = nums[0]
        min_dp[-1] = nums[-1]
        
        for i in range(1, n):
            max_dp[i] = max(nums[i], max_dp[i-1])
            
        for i in range(n-2, -1, -1):
            min_dp[i] = min(nums[i], min_dp[i+1])
        
        ans = 0
        for i in range(1, n-1):
            if max_dp[i-1] < max_dp[i] and nums[i] < min_dp[i+1]:
                ans += 2
            elif nums[i-1] < nums[i] < nums[i+1]:
                ans += 1
        return ans
