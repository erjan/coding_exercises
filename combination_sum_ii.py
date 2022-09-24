'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
'''


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        
        candidates = sorted(candidates)
        
        res = []
        
        self.dfs(candidates, target,[],0, res)
        
        return res
    
    def dfs(self, nums, target,path, idx,res):
        
        if  target <=0:
            if target == 0:
                res.append(path)
            return
        
        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i-1]:
                continue

            self.dfs(nums, target - nums[i], path + [nums[i]], i+1, res)
