'''
You are given k identical eggs and you have access to a building with n floors labeled from 1 to n.

You know that there exists a floor f where 0 <= f <= n such that any egg dropped at a floor higher than f will break, and any egg dropped at or below floor f will not break.

Each move, you may take an unbroken egg and drop it from any floor x (where 1 <= x <= n). If the egg breaks, you can no longer use it. However, if the egg does not break, you may reuse it in future moves.

Return the minimum number of moves that you need to determine with certainty what the value of f is.
'''

class Solution:
    def superEggDrop(self, egg: int, floor: int) -> int:
        dp = [[0]*(egg+1) for i in range(floor+1)]
        for i in range(1 , floor+1):
            for j in range(1 , egg + 1):
                dp[i][j] =  1 + dp[i-1][j] + dp[i-1][j-1]
                if dp[i][j] >= floor:
                    return i
--------------------------------------------------------------------
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        
        @cache
        def fn(m, k): 
            """Return max floor reachable with m moves and k eggs."""
            if m == 0 or k == 0: return 0 
            return 1 + fn(m-1, k-1) + fn(m-1, k)
        
        return next(m for m in range(1, n+1) if fn(m, k) >= n)
------------------------------------------------------------------------------------
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        dp = [[0]*(k+1) for _ in range(n+1) ] # (n+1) x (k+1)
        for i in range(n+1): dp[i][1] = i
        for j in range(k+1): dp[0][j] = 0

        for j in range(2, k+1): # j eggs
            x = 1
            for i in range(1, n+1): # i floors
                while x <= i and dp[i-x][j] > dp[x-1][j-1]: x += 1
                dp[i][j] = 1 + dp[x-1][j-1]
        return dp[n][k]
