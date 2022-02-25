'''
You are given an integer array nums (0-indexed). In one operation, you can choose 
an element of the array and increment it by 1.

For example, if nums = [1,2,3], you can choose to increment nums[1] to make nums = [1,3,3].
Return the minimum number of operations needed to make nums strictly increasing.

An array nums is strictly increasing if nums[i] < nums[i+1] for all 0 <= i < nums.length - 1. An array of length 1 is trivially strictly increasing.
'''

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c = 0
        for i in range(len(nums)-1):

            cur = nums[i]
            next_cur = nums[i+1]
            if next_cur <= cur:  # strictly increasing! so 1,1 is not good enough
                print('not strictly increasing: %d < %d ' % (cur, next_cur))
                diff = abs(nums[i+1] - nums[i]) + 1
                nums[i+1] = nums[i+1] + diff  
                c += diff

        print(nums)
        print('moves %d' % c)
        return c
