'''
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m-1][n-1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.
'''


class Solution:
    def uniquePathsWithObstacles(self, OG: List[List[int]]) -> int:
        if OG[0][0]: return 0
        m, n = len(OG), len(OG[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if OG[i][j] or (i == 0 and j == 0): continue
                dp[i][j] = (dp[i-1][j] if i else 0) + (dp[i][j-1] if j else 0)
        return dp[m-1][n-1]
      
------------------------------------------------------------------------------------------
#my bad code

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        g = obstacleGrid
        m = len(g)
        n = len(g[0])
        
        dp = [[0] * n ]*m
        
        for i in range(m):
            dp[0][i] = 1
            
          
        for j in range(n):
            dp[j][0] = 1
        
        for i in range(m):
            for j in range(n):
                
                if g[i][j] == 1:
                    dp[i][j] = 0
        
        
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        
        return dp[-1][-1]
        
-------------------------------------------------------------------
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:              
        if obstacleGrid[0][0] == 1:
            return 0
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])        
        
        obstacleGrid[0][0] = 1
        for i in range(1,m):
            obstacleGrid[i][0] = 1 if obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1 else 0
        
        for i in range(1,n):
            obstacleGrid[0][i] = 1 if obstacleGrid[0][i] == 0 and obstacleGrid[0][i-1] == 1 else 0
            
        
        for row in range(1, m):
            for col in range(1, n):                
                obstacleGrid[row][col] = obstacleGrid[row-1][col] + obstacleGrid[row][col-1] if obstacleGrid[row][col] == 0 else 0
         
        return obstacleGrid[-1][-1]
--------------------------------------------------------------------------------------      
      
