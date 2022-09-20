
'''
Suppose you have n integers labeled 1 through n. A permutation of those n integers perm (1-indexed) is considered a beautiful arrangement if for every i (1 <= i <= n), either of the following is true:

perm[i] is divisible by i.
i is divisible by perm[i].
Given an integer n, return the number of the beautiful arrangements that you can construct.
'''

class Solution:
    def countArrangement(self, n: int) -> int:
        self.count = 0
        self.backtrack(n, 1, [])
        return self.count
        
    def backtrack(self, N, idx, temp):
        if len(temp) == N:
            self.count += 1
            return
        
        for i in range(1, N+1):
            if i not in temp and (i % idx == 0 or idx % i == 0):
                temp.append(i)
                self.backtrack(N, idx+1, temp)
                temp.pop()
                
----------------------------------------------------------------------------------------------------------
class Solution:
    def countArrangement(self, n: int) -> int:
        
        self.res = 0
        nums = [i for i in range(1, n+1)]
        
        def dfs(nums: list, i: int = 1):
            if i == n+1: 
                self.res += 1
                return
            
            for j, num in enumerate(nums):
                if not(num % i and i % num):
                    dfs(nums[:j] + nums[j+1:], i+1)
            
        dfs(nums)
        return self.res
      
-------------------------------------------------------------------------------------------------------------------
class Solution:
    def countArrangement(self, n: int) -> int:
        
        nums = [i for i in range(1, n + 1)]
        i = 1
		res = [0]
		 
        self.dfs(nums, res, 1, n)
        return res[0]
    
    def dfs(self, nums, res, i, n):
        
        if i == n + 1: 
            res[0] += 1
            return

        for index, num in enumerate(nums):
            if num % i == 0 or i % num == 0:
                self.dfs(nums[:index] + nums[index + 1:], res, i + 1, n)
                
-----------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def countArrangement(self, n: int) -> int:
        
        self.res = 0
        nums = [i for i in range(1, n+1)]
        
        def dfs(nums: list, i: int = 1):
            if i == n+1: 
                self.res += 1
                return
            
            for j, num in enumerate(nums):
                if not(num % i and i % num):
                    dfs(nums[:j] + nums[j+1:], i+1)
            
        dfs(nums)
        return self.res
