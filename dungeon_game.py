'''
The demons had captured the princess and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of m x n rooms laid out in a 2D grid. Our valiant knight was initially positioned in the top-left room and must fight his way through dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons (represented by negative integers), so the knight loses health upon entering these rooms; other rooms are either empty (represented as 0) or contain magic orbs that increase the knight's health (represented by positive integers).

To reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

Return the knight's minimum initial health so that he can rescue the princess.

Note that any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.
'''


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n, m = len(dungeon), len(dungeon[0])
        BIG = 10**9
        dp = [[BIG] * (m + 1) for _ in range(n + 1)]
        dp[n][m - 1] = dp[n - 1][m] = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                minn = min(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(minn - dungeon[i][j], 1)

        return dp[0][0]
      
------------------------------------------------------------------------------------------
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n = len(dungeon)
        m = len(dungeon[0])
        memo = [[-1] * m for _ in range(n)]

        # From (i, j) to bottom right corner what is the min HP needed
        def dp(grid, i, j):
            # Base case
            if i == n - 1 and j == m - 1:
                return 1 if grid[i][j] >= 0 else -grid[i][j] + 1
            if i >= n or j >= m:
                return math.inf
            # Memoization
            if memo[i][j] != -1:
                return memo[i][j]
            # State transfer
            res = grid[i][j] - min(
                dp(grid, i + 1, j),
                dp(grid, i, j + 1)
            )

            memo[i][j] = 1 if res >= 0 else -res 
            return memo[i][j]

        return dp(dungeon, 0, 0)
        
