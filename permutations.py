'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
'''


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = list(permutations(nums))

        res = list(map(tuple, res))
        return res
      
---------------------------------------------------------------------------------
def permute(self, nums):
    res = []
    self.dfs(nums, [], res)
    return res
    
def dfs(self, nums, path, res):
    if not nums:
        res.append(path)
        # return # backtracking
    for i in xrange(len(nums)):
        self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
        
-------------------------------
def recursive(nums):
	from collections import deque
	q = deque()
	q.append((nums, []))  # -- nums, path (or perms)
	res = []
	while q:
		nums, path = q.popleft()
		if not nums:
			res.append(path)
		for i in range(len(nums)):
			newNums = nums[:i] + nums[i+1:]
			q.append((newNums, path+[nums[i]]))
	return res
----------------------------------------------------------------
def recursive(nums):
	 stack = [(nums, [])]   # -- nums, path (or perms)
	 res = []
	 while stack:
		 nums, path = stack.pop()
		 if not nums:
			 res.append(path)
		 for i in range(len(nums)):   # -- NOTE [4]
			 newNums = nums[:i] + nums[i+1:]
			 stack.append((newNums, path+[nums[i]]))  # --  just like we used to do (path + [node.val]) in tree traversal
	 return res

---------------------------------------------------------------
 def permute(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        res = []
        self.backtracking(res,visited,[],nums)
        return res
    def backtracking(self,res,visited,subset,nums):
        if len(subset) == len(nums):
            res.append(subset)
        for i in range(len(nums)):
            if i not in visited:
                visited.add(i)
                self.backtracking(res,visited,subset+[nums[i]],nums)
                visited.remove(i)
