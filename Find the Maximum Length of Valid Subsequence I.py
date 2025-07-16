'''
You are given an integer array nums.
A subsequence sub of nums with length x is called valid if it satisfies:

(sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2.
Return the length of the longest valid subsequence of nums.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
'''

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count_even = 0
        count_odd = 0
        for num in nums:
            if num % 2 == 0:
                count_even += 1
            else:
                count_odd += 1
        
        even_dp = 0
        odd_dp = 0
        for num in nums:
            if num % 2 == 0:
                even_dp = max(even_dp, odd_dp + 1)
            else:
                odd_dp = max(odd_dp, even_dp + 1)
        
        return max(count_even, count_odd, even_dp, odd_dp)
