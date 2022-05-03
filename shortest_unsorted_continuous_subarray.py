'''
Given an integer array nums, you need to find one continuous subarray 
that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

Return the shortest such subarray and output its length.
'''


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        high = n-1

        while (low+1) < n and nums[low] <=nums[low+1]:
            low+=1

        while (high-1) >=0 and nums[high-1] <= nums[high]:
            high-=1

        if low == n-1:
            return 0

        wmin = float('inf')
        wmax = float('-inf')
        for i in range(low, high+1):
            wmin = min(wmin, nums[i])
            wmax = max(wmax,nums[i])

        while low-1 >=0 and nums[low-1] >wmin:
            low-=1

        while high+1 <=(n-1) and nums[high+1] < wmax:
            high+=1

        return high-low+1
