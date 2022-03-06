'''
Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums.

A subarray is defined as a contiguous sequence of numbers in an array.

A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i where l <= i < r, numsi < numsi+1. Note that a subarray of size 1 is ascending.
'''

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:

        s = 0
        n = nums
        best = max(n)
        
        for i in range(len(n)):

            temp_sum = 0

            current = n[i]
            for j in range(i+1, len(n)):
                if n[j] <= n[j-1]:
                    break
                current += n[j]
                best = max(best, current)

        print('------')
        print(best)
        return best
