'''
You are given a 0-indexed integer array nums of length n.

nums contains a valid split at index i if the following are true:

The sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1 elements.
There is at least one element to the right of i. That is, 0 <= i < n - 1.
Return the number of valid splits in nums.
'''

A prefix sum array is an array that stores at ith index, the sum of all elements encountered from 0th index upto the ith index (inclusive). How can this help?

The prefix sum has a property that it avoids recomputation of sum.
The sum upto element i can be obtained by prefix_sum[i].
The sum from i + 1 to last element of array can be obtained by prefix_sum[n-1] - prefix_sum[i]
The full code (written during contest) is given below:

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix_sum = [nums[0]]
        n = len(nums)
        for i in range(1, n):
            prefix_sum.append(nums[i] + prefix_sum[-1]) 
        
        count = 0
        for i in range(n-1):
            if prefix_sum[i] >= prefix_sum[n-1] - prefix_sum[i]:
                count += 1
        return count
