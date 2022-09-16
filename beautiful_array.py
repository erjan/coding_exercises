'''
An array nums of length n is beautiful if:

nums is a permutation of the integers in the range [1, n].
For every 0 <= i < j < n, there is no index k with i < k < j where 2 * nums[k] == nums[i] + nums[j].
Given the integer n, return any beautiful array nums of length n. There will be at least one valid answer for the given n.
'''

from itertools import permutations
class Solution:
    def invalid(self, x):
        n = len(x)
        flag = False
        for i in range(n):
            if flag: break
            for j in range(i+2, n):
                if flag: break
                for k in range(i+1, j):
                    if 2*x[k] == x[i]+x[j]: flag = True; break
        return flag
        
    def beautifulArray(self, n: int) -> List[int]:
        for perm in permutations(range(1, n+1)):
            if not self.invalid(perm):
                return perm
              
-----------------------------------------------------------

class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        nums = list(range(1, N+1))
        
        def helper(nums) -> List[int]:
            if len(nums) < 3:
                return nums
            even = nums[::2]
            odd = nums[1::2]
            return helper(even) + helper(odd)
        return helper(nums)  
