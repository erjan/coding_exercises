'''
Given an integer array nums, return all the different possible increasing subsequences of the given array with at least two elements. You may return the answer in any order.

The given array may contain duplicates, and two equal integers should also be considered a special case of increasing sequence.
'''


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        if not nums:
            return []
        res = []
        
        
        
        def dfs(start, path):
            
            if len(path) >=2:
                res.append(path)
            
            used = set()
                 
                
            for i in range(start, len(nums)):
                if not path or path[-1] <=nums[i]:
                    if nums[i] not in used:
                        used.add(nums[i])
                        dfs(i+1, path + [nums[i]])
        
        dfs(0, [])
        return res
