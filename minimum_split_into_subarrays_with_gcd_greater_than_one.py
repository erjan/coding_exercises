'''
You are given an array nums consisting of positive integers.

Split the array into one or more disjoint subarrays such that:

Each element of the array belongs to exactly one subarray, and
The GCD of the elements of each subarray is strictly greater than 1.
Return the minimum number of subarrays that can be obtained after the split.

Note that:

The GCD of a subarray is the largest positive integer that evenly divides all the elements of the subarray.
A subarray is a contiguous part of the array.
'''


from math import gcd
class Solution:
    def minimumSplits(self, nums: List[int]) -> int:
        cur = nums[0]
        res = 0
        for num in nums:
            if gcd(cur, num) == 1:
                cur = num 
                res += 1
            else:
                cur = gcd(cur, num)
        return res + 1
-----------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def minimumSplits(self, nums: List[int]) -> int:

        i = 0
        split = 0
        while i < len(nums):
            j = i
            cur_gcd = nums[j]
            while j<len(nums):
                cur_gcd = gcd(cur_gcd, nums[j])
                if cur_gcd == 1:
                    break
                j+=1
            
            i = j
            split += 1

        return split
    
