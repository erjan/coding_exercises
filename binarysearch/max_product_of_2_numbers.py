'''

Given a list of integers nums, find the largest product of two distinct elements.

'''


class Solution:
    def solve(self, nums):
        
        nums.sort()
        case1 = nums[-1] * nums[-2]
        case2 = nums[0] * nums[1]

        return max(case1,case2)

      
        
