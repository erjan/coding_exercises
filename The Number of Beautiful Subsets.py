'''
You are given an array nums of positive integers and a positive integer k.

A subset of nums is beautiful if it does not contain two integers with an absolute difference equal to k.

Return the number of non-empty beautiful subsets of the array nums.

A subset of nums is an array that can be obtained by deleting some (possibly none) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.
'''


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        q = deque( [([], -1)] )
        res = 0
        
        while q:
            cur, idx = q.popleft()
            res += 1
            
            for i in range(idx + 1, len(nums)):
                if nums[i] - k in cur or nums[i] + k in cur:
                    continue
                q.append( (cur + [nums[i]], i) )
        
        return res - 1
      
-------------------------------------------------------------------------------------------
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        n = len(nums)
        output = 0
        
        def dfs(i, ctr):
            nonlocal output
            if i == n:
                if ctr:
                    output += 1
                return
            
            if nums[i] - k not in ctr and nums[i] + k not in ctr:
                ctr[nums[i]] += 1
                dfs(i + 1, ctr)
                ctr[nums[i]] -= 1
                if not ctr[nums[i]]:
                    del ctr[nums[i]]
            dfs(i + 1, ctr)
        
        dfs(0, Counter())
        return output
            
