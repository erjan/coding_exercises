'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
'''


#gives TLE error

import math
def f(nums):
    local_sum = 0
    global_sum = float('-inf')
    print(nums)

    res = []
    for r in range(len(nums)):
        print('-------------------------------------')
        before = 0
        #print(nums[r:i])
        for i in range(r,len(nums)):
            #print('-------------------------------------------')
            print(nums[r:i])
            
            local_sum = nums[i] + before
            #print('local sum: %d = nums[i]: %d + %d' %( local_sum, nums[i], before))
            before = local_sum
            if local_sum > global_sum:
                global_sum = local_sum
        print('global sum %d ' % global_sum)
        res.append(global_sum)
        

a = [-2,1,-3,4,-1,2,1,-5,4]

f(a)

#optimal solution

'''
observation is that negative numbers dont add anything & since we need a contigous array, we have to reset the current sum!
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = max_sum

        for i in range(1, len(nums)):
            cur_sum = max( nums[i]+ cur_sum, nums[i])
            max_sum = max(cur_sum, max_sum)
        return max_sum        
    
#slightly different
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = max_sum

        for i in range(1, len(nums)):
            if nums[i] + cur_sum >= nums[i]:
                cur_sum = nums[i] + cur_sum
            else:
                cur_sum = nums[i]                         
            max_sum = max(cur_sum, max_sum)
        return max_sum    
