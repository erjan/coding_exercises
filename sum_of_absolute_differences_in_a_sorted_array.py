'''
You are given an integer array nums sorted in non-decreasing order.

Build and return an integer array result with the same length as nums such that result[i] is equal to the summation of absolute differences between nums[i] and all the other elements in the array.

In other words, result[i] is equal to sum(|nums[i]-nums[j]|) where 0 <= j < nums.length and j != i (0-indexed).
'''


My solution below is based on the fact the the sum of absolute differences of particular index i can be calculated using,
(prefix[i-1] - array[i]* i) + (suffix[i] - array[i]*(n-i))

To get rid of O(n) auxillary space needed for storing suffix sum, we can calculate the suffix sum from prefix sum in O(1) using,
suffix[i] = sum(array)-prefix[i-1] #(sum(array[i:-1]) = total-(sum(array[1:i]))

from itertools import accumulate 

class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        total, n = sum(nums), len(nums) #for i, ri in zip(nums, reversed(nums)): pref.append(pref[-1] + i)
        return [(((i+1) * num) - pref) + ((total-pref) - ((n-i-1) * num)) for (i, num), pref in zip(enumerate(nums), list(accumulate(nums)))]

