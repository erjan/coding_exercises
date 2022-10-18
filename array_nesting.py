'''
You are given an integer array nums of length n where nums is a permutation of the numbers in the range [0, n - 1].

You should build a set s[k] = {nums[k], nums[nums[k]], nums[nums[nums[k]]], ... } subjected to the following rule:

The first element in s[k] starts with the selection of the element nums[k] of index = k.
The next element in s[k] should be nums[nums[k]], and then nums[nums[nums[k]]], and so on.
We stop adding right before a duplicate element occurs in s[k].
Return the longest length of a set s[k].
'''

class Solution(object):
    def arrayNesting(self, nums):
        vis = set()

        def dfs(i):
            if i in vis: return 0;
            vis.add(i)
            return 1 + dfs(nums[i])
        
        ans = 0
        for i in range(len(nums)):
            if i not in vis: ans = max(ans, dfs(i))
        
        return ans
      
-----------------------------------------------------------------

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        max_len = 0
        visited = set()
        def dfs(nums, index, dfs_visited):
            if index in dfs_visited:
                return len(dfs_visited)
            
            # add the index to dfs_visited and visited
            visited.add(index)
            dfs_visited.add(index)
            return dfs(nums, nums[index], dfs_visited)
            
        for i in range(len(nums)):
            if i not in visited:
                max_len = max(max_len, dfs(nums, i, set()))
        return max_len
      
-------------------------------------------------------------------------      
