'''
Given a wooden stick of length n units. The stick is labelled from 0 to n. For example, a stick of length 6 is labelled as follows:


Given an integer array cuts where cuts[i] denotes a position you should perform a cut at.

You should perform the cuts in order, you can change the order of the cuts as you wish.

The cost of one cut is the length of the stick to be cut, the total cost is the sum of costs of all cuts. When you cut a stick, it will be split into two smaller sticks (i.e. the sum of their lengths is the length of the stick before the cut). Please refer to the first example for a better explanation.

Return the minimum total cost of the cuts.
'''

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        
        @lru_cache(None)
        def fn(lo, hi): 
            """Return cost of cutting [lo, hi]."""
            cc = [c for c in cuts if lo < c < hi] #collect cuts within this region 
            if not cc: return 0
            ans = inf
            for mid in cc: ans = min(ans, fn(lo, mid) + fn(mid, hi))
            return ans + hi - lo
        
        return fn(0, n)
      
--------------------------------------------------------------------------------------------
#bottom up

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.extend([0, n])
        cuts.sort()
        
        dp = [[0]*len(cuts) for _ in cuts] 
        for i in reversed(range(len(cuts))):
            for j in range(i+2, len(cuts)): 
                dp[i][j] = cuts[j] - cuts[i] + min(dp[i][k] + dp[k][j] for k in range(i+1, j))
        return dp[0][-1]
