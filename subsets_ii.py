'''
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
'''

class Solution(object):
    def subsetsWithDup(self, nums):
        ret = []
        self.dfs(sorted(nums), [], ret)
        return ret
    
    def dfs(self, nums, path, ret):
        ret.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.dfs(nums[i+1:], path+[nums[i]], ret)
