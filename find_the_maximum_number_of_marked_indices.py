'''
You are given a 0-indexed integer array nums.

Initially, all of the indices are unmarked. You are allowed to make this operation any number of times:

Pick two different unmarked indices i and j such that 2 * nums[i] <= nums[j], then mark i and j.
Return the maximum possible number of marked indices in nums using the above operation any number of times.
'''



class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        i, n = 0, len(nums)
        nums.sort()
        for j in range(n - n // 2, n):
            i += 2 * nums[i] <= nums[j]
        return i * 2
      
---------------------------------------------------------------------------------------------------------------------------
class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        l,r=0,len(nums)//2
        while r<len(nums) and l<len(nums)//2:
            if 2*nums[l]<=nums[r]: l+=1
            r+=1
        return l*2
