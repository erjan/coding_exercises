'''
You are given nums, an array of positive integers of size 2 * n. You must perform n operations on this array.

In the ith operation (1-indexed), you will:

Choose two elements, x and y.
Receive a score of i * gcd(x, y).
Remove x and y from nums.
Return the maximum score you can receive after performing n operations.

The function gcd(x, y) is the greatest common divisor of x and y.
'''

class Solution:
    def maxScore(self, n: List[int]) -> int:
        @lru_cache(None)
        def dfs(i: int, mask: int) -> int:
            if i > len(n) // 2:
                return 0;
            res = 0
            for j in range(len(n)):
                for k in range(j + 1, len(n)):
                    new_mask = (1 << j) + (1 << k)
                    if not mask & new_mask:
                        res = max(res, i * gcd(n[j], n[k]) + dfs(i + 1, mask + new_mask))
            return res
        return dfs(1, 0)
      
----------------------------------------------------------------------------------------------------------------
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        
        @cache
        def fn(nums, k): 
            """Return max score from nums at kth step."""
            if not nums: return 0 # boundary condition 
            ans = 0 
            for i in range(len(nums)):
                for j in range(i+1, len(nums)): 
                    rest = nums[:i] + nums[i+1:j] + nums[j+1:]
                    ans = max(ans, k*gcd(nums[i], nums[j]) + fn(tuple(rest), k+1))
            return ans
        
        return fn(tuple(nums), 1)
