'''
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.
'''


class Solution(object):
    def combinationSum3(self, k, n):
        ret = []
        self.dfs(list(range(1, 10)), k, n, [], ret)
        return ret
    
    def dfs(self, nums, k, n, path, ret):
        if k < 0 or n < 0:
            return 
        if k == 0 and n == 0:
            ret.append(path)
        for i in range(len(nums)):
            self.dfs(nums[i+1:], k-1, n-nums[i], path+[nums[i]], ret)
            
--------------------------------------------------------------------------
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.result =[]
        self.helper([],1,k,n)
        return self.result
    
    def helper(self,path,start,k,target):
        
        if k ==0 and target==0:
            self.result.append(path)
            return 
        
        if k == 0 or target <= 0:
            return
        
        for i in range(start,10):
            self.helper(path+[i],i+1,k-1,target-i)
