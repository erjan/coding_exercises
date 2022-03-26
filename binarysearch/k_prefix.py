'''
Given a list of integers nums and an integer k, return the maximum 
possible i where nums[0] + nums[1] + ...  + nums[i] ≤ k. Return -1 if no valid i exists.

Constraints

0 ≤ n ≤ 1,000 where n is the length of nums.
-1,000 ≤ nums[i] ≤ 1,000
0 ≤ k ≤ 10 ** 9
'''


class Solution:
    def solve(self, nums, k):
        if len(nums) == 0:
            return -1
        
        pref = [0] * len(nums)
        pref[0] = nums[0]

        #calculate prefix sum for the entire nums
        for i in range(1, len(nums)):
            pref[i] += nums[i] + pref[i-1]            
        i = 0
        res = -1
        print('prefix array', pref)
            
        while i < len(pref):
            if pref[i] <= k:
                res = i                
            i+=1
        print('res', res)                
        
        return res
