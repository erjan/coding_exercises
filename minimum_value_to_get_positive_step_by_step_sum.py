'''
Given an array of integers nums, you start with an initial positive value startValue.

In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

Return the minimum positive value of startValue such that the step by step sum is never less than 1.
'''

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        pref_sum = [0 for i in range(len(nums))]
        pref_sum[0] = nums[0]

        for i in range(1, len(nums)):

            pref_sum[i] = pref_sum[i-1] + nums[i]
            
        min_pref_sum = min(pref_sum)
        x = 1 - min_pref_sum
        if x <= 0:
            x = 1
            return x
        print(x)
        return x
