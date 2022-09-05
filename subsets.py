'''
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
'''


from itertools import combinations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        for i in range(len(nums)):
            res.extend(list(combinations(nums,i)))
            
        res.append(nums)
        return res
    
----------------------------------------------------------------------
class Solution(object):
    def subsets(self, nums):
        nums.sort()
        result = [[]]
        for num in nums:
            result += [i + [num] for i in result]
        return result
        
-----------------------------------------------------------------------------------
def subsets1(self, nums):
    res = []
    self.dfs(sorted(nums), 0, [], res)
    return res
    
def dfs(self, nums, index, path, res):
    res.append(path)
    for i in xrange(index, len(nums)):
        self.dfs(nums, i+1, path+[nums[i]], res)
