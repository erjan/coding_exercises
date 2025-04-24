'''
You are given an array nums consisting of positive integers.

We call a subarray of an array complete if the following condition is satisfied:

The number of distinct elements in the subarray is equal to the number of distinct elements in the whole array.
Return the number of complete subarrays.

A subarray is a contiguous non-empty part of an array.
'''

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        
        nd = len(set(nums))
        res = 0
        n = len(nums)
        for i in range(n):
            curset = set()
            for j in range(i,n):
                curset.add(nums[j])
                if len(curset) == nd:
                    res+= n-j
                    break
        return res


              
