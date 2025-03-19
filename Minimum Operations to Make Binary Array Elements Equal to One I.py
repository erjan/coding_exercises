'''
You are given a binary array nums.

You can do the following operation on the array any number of times (possibly zero):

Choose any 3 consecutive elements from the array and flip all of them.
Flipping an element means changing its value from 0 to 1, and from 1 to 0.

Return the minimum number of operations required to make all elements in nums equal to 1. If it is impossible, return -1.
'''

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        
        for i in range(n - 2):
            if nums[i] == 0:
                nums[i] ^= 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
                count += 1
        
        return count if (nums[n - 2] == 1 and nums[n - 1] == 1) else -1
