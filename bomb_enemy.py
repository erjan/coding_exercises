'''
Given an m x n matrix grid where each cell is either a wall 'W', an enemy 'E' or empty '0', return the maximum enemies you can kill using one bomb. You can only place the bomb in an empty cell.

The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since it is too strong to be destroyed.
'''

class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        ## RC ##
		## APPROACH : DP ##
        ## LOGIC ##
        ## 1. For every "O" position, store enemies left to it, right to it, below it, above it
		## TIME COMPLEXICITY : O(5N) ##
		## SPACE COMPLEXICITY : O(N) ##
        
        if( not grid ): return 0
        n = len(grid)
        m = len(grid[0])
        # [0,0,0,0] => Number of enemies to ( Left, Right, Top, Bottom )
        dp = [ [[0,0,0,0] for __ in range(m)] for _ in range(n) ]
        
        # left to right
        for i in range(n):
            runningSum = 0
            for j in range(m):
                if( grid[i][j] == "E" ):
                    runningSum += 1
                elif( grid[i][j] == "W" ):
                    runningSum = 0
                else:
                    dp[i][j][0] = runningSum
        
        # right to left
        for i in range(n):
            runningSum = 0
            for j in range(m-1, -1, -1):
                if( grid[i][j] == "E" ):
                    runningSum += 1
                elif( grid[i][j] == "W" ):
                    runningSum = 0
                else:
                    dp[i][j][1] = runningSum
        
        # top to bottom
        for j in range(m):
            runningSum = 0
            for i in range(n):
                if( grid[i][j] == "E" ):
                    runningSum += 1
                elif( grid[i][j] == "W" ):
                    runningSum = 0
                else:
                    dp[i][j][2] = runningSum
        
        # bottom to top
        for j in range(m):
            runningSum = 0
            for i in range(n-1, -1, -1):
                if( grid[i][j] == "E" ):
                    runningSum += 1
                elif( grid[i][j] == "W" ):
                    runningSum = 0
                else:
                    dp[i][j][3] = runningSum
        
        ans = 0
        for i in range(n):
            for j in range(m):
                if(grid[i][j] == "0"):
                    ans = max( ans, sum(dp[i][j]) )
        return ans
        
        
-----------------------------------------------------------------------------------------
I really liked some of the solutions out there that were more creative, but here is a DFS solution that will also solve this problem.

Time Complexity: O(n^2).

"""
W - wall, E - Enemy, 0 - empty

Return max enemies you can kill using one bomb
- bomb kills ALL enemies in same row and col from planted point until it hits wall
** only put bomb in EMPTY Cell

[
["0","E","0","0"],
["E","0","W","E"],
["0","E","0","0"]]


Answer (1,1) -- kills 3 E's

-- We could DFS from each Enemy Cell and log all the O's it touches
--- dp cell with most Enemeny cells wins
"""

class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        
        if not grid: return 0
        
        dp = [[0] * len(grid[0]) for _ in range(len(grid))]
        
        def dfs(r,c,prevDirection):
            nonlocal visited, dp
            
            
            offsets = [(0,-1,'l'),(0,1,'r'),(-1,0,'u'),(1,0,'d')]
            
            if not prevDirection:
                for offset in offsets:
                    newR = r + offset[0]
                    newC = c + offset[1]

                    if newR >= 0 and newR < len(grid) and newC >=0 and newC < len(grid[0]) and (grid[newR][newC] == '0' or grid[newR][newC] == 'E') and (newR,newC) not in visited:
                        visited.add((newR,newC))
                        
                        if grid[newR][newC] == '0': dp[newR][newC] += 1
                        dfs(newR,newC,offset[2])
            else:
                if prevDirection == 'u':
                    newR = r + -1
                    newC = c
                elif prevDirection == 'd':
                    newR = r + 1
                    newC = c
                elif prevDirection == 'l':
                    newR = r
                    newC = c + -1
                elif prevDirection == 'r':
                    newR = r
                    newC = c+1
                if newR >= 0 and newR < len(grid) and newC >=0 and newC < len(grid[0]) and (grid[newR][newC] == '0' or grid[newR][newC] == 'E') and (newR,newC) not in visited:
                        visited.add((newR,newC))
                        if grid[newR][newC] == '0': dp[newR][newC] += 1
                        dfs(newR,newC,prevDirection)
        
        # iterate through and dfs into Enemy Cells
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 'E':
                    visited = set()
                    dfs(r,c,None)
        
        

        
        largestVal = 0
        # find the largest cell
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if dp[r][c] > largestVal:
                    largestVal = dp[r][c]
        
        return largestVal
-----------------------------------------------------------------------

class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        v1 = [[0]*n for _ in range(m)] # left to right
        v2 = [[0]*n for _ in range(m)] # right to left
        v3 = [[0]*n for _ in range(m)] # top to bottom 
        v4 = [[0]*n for _ in range(m)] # bottom to top
        
        for i in range(m):
            for j in range(n):
                enemy = 0 if j == 0 or grid[i][j] == 'W' else v1[i][j-1]
                v1[i][j] = enemy +1 if grid[i][j] == 'E' else enemy
            for j in range(n-1,-1,-1):
                enemy = 0 if j == n-1 or grid[i][j] == 'W' else v2[i][j+1]
                v2[i][j] = enemy +1 if grid[i][j] == 'E' else enemy
        for j in range(n):
            for i in range(m):
                enemy = 0 if i == 0 or grid[i][j] == 'W' else v3[i-1][j]
                v3[i][j] = enemy +1 if grid[i][j] == 'E' else enemy
            for i in range(m-1,-1,-1):
                enemy = 0 if i == m-1 or grid[i][j] == 'W' else v4[i+1][j]
                v4[i][j] = enemy +1 if grid[i][j] == 'E' else enemy
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    res = max(res, v1[i][j] + v2[i][j] + v3[i][j] + v4[i][j])
        return res
------------------------------------------------------------------

class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid or grid[0] == []:
            return 0
        m = len(grid)
        n = len(grid[0])
        
        dic1 = [[0]*n for _ in range(m)]
        dic2 = [[0]*n for _ in range(m)]
        dic3 = [[0]*n for _ in range(m)]
        dic4 = [[0]*n for _ in range(m)]
        
        for i in range(n):
            if grid[0][i] == "E":
                dic1[0][i] = 1
        for i in range(m):
            if grid[i][0] == "E":
                dic2[i][0] = 1
        for i in range(n):
            if grid[m-1][i] == "E":
                dic3[m-1][i] = 1
        for i in range(m):
            if grid[i][n-1] == "E":
                dic4[i][n-1] = 1
        for i in range(1,m):
            for j in range(n):
                if grid[i][j] == "0":
                    dic1[i][j] = dic1[i-1][j]
                if grid[i][j] == "E":
                    dic1[i][j] = dic1[i-1][j]+1
                if grid[i][j] == "W":
                    dic1[i][j] = 0
        for i in range(m):
            for j in range(1,n):
                if grid[i][j] == "0":
                    dic2[i][j] = dic2[i][j-1]
                if grid[i][j] == "E":
                    dic2[i][j] = dic2[i][j-1]+1
                if grid[i][j] == "W":
                    dic2[i][j] = 0
        for i in range(m-2,-1,-1):
            for j in range(n):
                if grid[i][j] == "0":
                    dic3[i][j] = dic3[i+1][j]
                if grid[i][j] == "E":
                    dic3[i][j] = dic3[i+1][j]+1
                if grid[i][j] == "W":
                    dic3[i][j] = 0
        for i in range(m):
            for j in range(n-2,-1,-1):
                if grid[i][j] == "0":
                    dic4[i][j] = dic4[i][j+1]
                if grid[i][j] == "E":
                    dic4[i][j] = dic4[i][j+1]+1
                if grid[i][j] == "W":
                    dic4[i][j] = 0        
        sol = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    temp = sum([dic1[i][j],dic2[i][j],dic3[i][j],dic4[i][j]])
                    sol = max(sol,temp)
        return sol
      
      
-------------------------------------------------------------------------------------------
The brute force solution is very intuitive.. just count 'E's in rows and cols for each 0 in the matrix and return the maximum. This takes O((mn)*(m+n)) as you have to traverse up, down, left, and right for every i,j.

We can optimize on this by doing 4 passes and adding the number of E's seen so far, and reset if we see a 'W'.
From left to right then right to left for E's seen in each row. And then from up to down and down to up for each E seen so far in column.

Total time -> O(4*mn) --> O(mn)

class Solution(object):
    def maxKilledEnemies(self, grid):
        if len(grid) == 0:
            return 0
        max_hits = 0
        nums = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        
        #From Left
        for i in range(len(grid)):
            row_hits = 0
            for j in range(len(grid[0])):
                if grid[i][j] == 'E':
                    row_hits += 1
                elif grid[i][j] == 'W':
                    row_hits = 0
                else:
                    nums[i][j] = row_hits
                
        #From Right
        for i in range(len(grid)):
            row_hits = 0
            for j in range(len(grid[0])-1, -1, -1):
                if grid[i][j] == 'W':
                    row_hits = 0
                elif grid[i][j] == 'E':
                    row_hits +=1
                else:
                    nums[i][j] += row_hits

        for i in range(len(nums[0])):
            col_hits = 0
            for col in range(len(nums)):
                if grid[col][i] == 'E':
                    col_hits += 1
                elif grid[col][i] == 'W':
                    col_hits = 0
                else:
                    nums[col][i] += col_hits

        for i in range(len(nums[0])):
            col_hits = 0
            for col in range(len(nums)-1, -1, -1):
                if grid[col][i] == 'E':
                    col_hits +=1
                elif grid[col][i] == 'W':
                    col_hits = 0
                else:
                    nums[col][i] += col_hits
                    max_hits = max(max_hits, nums[col][i])


        return max_hits

      
      
