'''
Given an m x n binary matrix mat, return the length of the longest line of consecutive one in the matrix.

The line could be horizontal, vertical, diagonal, or anti-diagonal.
'''

class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        """
        dp[i][j][0]: the number of continuous 1 found at M[i][j] so far horizontally
        dp[i][j][1]: the number of continuous 1 found at M[i][j] so far vertically
        dp[i][j][2]: the number of continuous 1 found at M[i][j] so far diagonally
        dp[i][j][3]: the number of continuous 1 found at M[i][j] so far anti-diagonally
          input:          horizontal dp     vertical dp     diagonal dp   anti-diagonal dp
		 [[0,1,1,0],      [[0,1,2,0],      [[0,1,1,0],    [[0,1,1,0]    [[0,1,1,0]
          [0,1,1,0],       [0,1,2,0],       [0,2,2,0],     [0,1,2,0]     [0,2,1,0]
          [0,0,0,1]]       [0,0,0,1]]       [0,0,0,1]]     [0,0,0,3]     [0,0,0,1]] 
		 while generating the above 4 dp table, we can keep updating the maximum value found so far.
        """
        if M == []:
            return 0
        nrow,ncol = len(M),len(M[0])
        dp = [[[0 for _ in range(ncol)] for _ in range(nrow)] for _ in range(4)]
                   
        res = 0
        for row in range(nrow):
            for col in range(ncol):
                if M[row][col] == 1:
                    # horizontal
                    if col == 0:
                        dp[0][row][col] = 1
                    else:
                        dp[0][row][col] = dp[0][row][col-1] + 1
                        
                    # vertical
                    if row == 0:
                        dp[1][row][col] = 1
                    else:
                        dp[1][row][col] = dp[1][row-1][col] + 1 
                    
                    # diagonal
                    if row == 0 or col == 0:
                        dp[2][row][col] = 1
                    else:
                        dp[2][row][col] = dp[2][row-1][col-1] + 1
                    # anti-diagonal
                    if row == 0 or col == ncol-1:
                        dp[3][row][col] = 1
                    else:
                        dp[3][row][col] = dp[3][row-1][col+1] + 1
                    res = max(res,dp[0][row][col],dp[1][row][col],dp[2][row][col],dp[3][row][col])
        return res
      
-------------------------------------------------------

Explanation
Do a DP and check previous 4 different states (upper-left, upper, upper-right, left)
You can make it more space effective by only keep the previous row's information
Implementation
class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        dp = [[[0] * 4 for j in range(n)] for i in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if not mat[i][j]: continue
                if i > 0:
                    dp[i][j][1] = dp[i-1][j][1] + 1
                    if j > 0:
                        dp[i][j][0] = dp[i-1][j-1][0] + 1
                    if j+1 < n:    
                        dp[i][j][2] = dp[i-1][j+1][2] + 1
                if j > 0:        
                    dp[i][j][3] = dp[i][j-1][3] + 1
                for k in range(4):    
                    dp[i][j][k] = max(dp[i][j][k], 1)    
                ans = max(ans, max([dp[i][j][k] for k in range(4)]))
        return ans
-------------------------------------------------------

from functools import lru_cache

class Solution:
    def longestLine(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        # valid positions
        def valid(i, j):
            if not 0 <= i < len(matrix) or not 0 <= j < len(matrix[0]):
                return False
            if matrix[i][j] != 1:
                return False
            return True
        # define dfs's
        @lru_cache(maxsize=None)
        def horizontal(i: int, j: int) -> int:
            # explore children
            if valid(i, j + 1): return horizontal(i, j + 1) + 1
            else: return 1
        @lru_cache(maxsize=None)
        def vertical(i: int, j: int) -> int:
            # explore children
            if valid(i + 1, j): return vertical(i + 1, j) + 1
            else: return 1
        @lru_cache(maxsize=None)
        def diagonal(i: int, j: int) -> int:
            # explore children
            if valid(i + 1, j + 1): return diagonal(i + 1, j+ 1) + 1
            else: return 1
        @lru_cache(maxsize=None)
        def antidiagonal(i: int, j: int) -> int:
            # explore children
            if valid(i + 1, j - 1): return antidiagonal(i + 1, j - 1) + 1
            else: return 1
        # keep track of the global max
        global_max = 0
        # explore the graph
        for i, row in enumerate(matrix):
            for j, e in enumerate(row):
                if e != 1:
                    continue
                global_max = max(global_max,
                                 horizontal(i, j),
                                 vertical(i, j),
                                 diagonal(i, j),
                                 antidiagonal(i, j),
                                )
        return global_max
------------------------------------------------------------

class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        if not M:
            return 0
        
        m, n = len(M), len(M[0])
        
        dp = {k:[0] * (n+2) for k in ['r', 'c', 'd', 'ad']} 
        out = 0 
        for i in range(m):
            dp1 = {k:[0] * (n+2) for k in ['r', 'c', 'd', 'ad']} 
            for j in range(n):
                if M[i][j]:
                    dp1['r'][j+1] = 1 + dp1['r'][j] 
                    dp1['c'][j+1] = 1 + dp['c'][j+1] 
                    dp1['d'][j+1] = 1 + dp['d'][j] 
                    dp1['ad'][j+1] = 1 + dp['ad'][j+2]
                    out = max(out,dp1['r'][j+1],dp1['c'][j+1],
                              dp1['d'][j+1],dp1['ad'][j+1])
            dp=dp1
        return out
--------------------------------------------------------

3D DP

class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        if len(M)==0:
            return 0
        m,n = len(M), len(M[0])
        dp = [[[0 for _ in range(4)] for _ in range(n)] for _ in range(m)]
        
        res = 0
        for i in range(m):
            for j in range(n):
                if M[i][j]==1:
                    dp[i][j][0] = dp[i][j-1][0]+1 if j>0 else 1
                    dp[i][j][1] = dp[i-1][j][1]+1 if i>0 else 1
                    dp[i][j][2] = dp[i-1][j-1][2]+1 if (i>0 and j>0) else 1
                    dp[i][j][3] = dp[i-1][j+1][3]+1 if (i>0 and j<n-1) else 1
                    
                    res = max([res, dp[i][j][0], dp[i][j][1], dp[i][j][2], dp[i][j][3]])
        
        return res
---------------------------------------------------------------------------------      
      
      
      
      
