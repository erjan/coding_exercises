'''
Given an integer array nums and an integer k, return the number of subarrays of nums where the least common multiple of the subarray's elements is k.

A subarray is a contiguous non-empty sequence of elements within an array.

The least common multiple of an array is the smallest positive integer that is divisible by all the array elements.
'''


class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        
        cnt = 0

        for i in range(0, len(nums)):       # [1] for every initial number, try extending
            l = nums[i]                     #     a continuous sequence of numbers
            for j in range(i, len(nums)):  
                l = lcm(l,nums[j])          # [2] once LCM becomes 'k', each subsequent number
                if l == k : cnt += 1        #     that don't increase this value will give one
                if l > k  : break           #     more valid subarray
            
        return cnt
