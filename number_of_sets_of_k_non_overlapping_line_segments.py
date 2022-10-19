'''
Given n points on a 1-D plane, where the ith point (from 0 to n-1) is at x = i, find the 
number of ways we can draw exactly k non-overlapping line segments such that each segment covers 
two or more points. The endpoints of each segment must
have integral coordinates. The k line segments do not have to cover all n points, and they are allowed to share endpoints.

Return the number of ways we can draw k non-overlapping line segments. Since this number can be huge, return it modulo 109 + 7.
'''

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        @lru_cache(None)
        def dp(i, k, isStart):
            if k == 0: return 1 # Found a way to draw k valid segments
            if i == n: return 0 # Reach end of points
            ans = dp(i+1, k, isStart) # Skip ith point
            if isStart:
                ans += dp(i+1, k, False) # Take ith point as start
            else:
                ans += dp(i, k-1, True) # Take ith point as end
            return ans % MOD
        return dp(0, k, True)
      
------------------------------------------------------------------------------------------      
