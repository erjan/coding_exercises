'''
Given a list of integers nums, return whether the largest number is bigger than the second-largest number by more than two times.

Constraints

2 ≤ n ≤ 100,000 where n is the length of nums
'''

class Solution:
    def solve(self, nums):
        
        m = max(nums)
        nums.remove(m)
        second_m = max(nums)

        return 2* second_m < m

    
#much better solution

class Solution:
    def solve(self, nums):
       nums = sorted(nums)

       return nums[-2] * 2 < nums[-1]
