'''
You are given a m x n matrix grid. Initially, you are located at the top-left corner (0, 0), and in each step, you can only move right or down in the matrix.

Among all possible paths starting from the top-left corner (0, 0) and ending in the bottom-right corner (m - 1, n - 1), find the path with the maximum non-negative product. The product of a path is the product of all integers in the grid cells visited along the path.

Return the maximum non-negative product modulo 109 + 7. If the maximum product is negative, return -1.

Notice that the modulo is performed after getting the maximum product.
'''

class Solution(object):
    def maxProductPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        MOD = 1e9+7
        row = len(grid)
        col = len(grid[0])
        
        # Make a dp that contains [max, min]
        dp = [[0 for _ in range(col)] for _ in range(row)]
        
        for i in range(row):
            for j in range(col):
                if i == 0 and j == 0:
                    dp[i][j] = [grid[i][j], grid[i][j]]
                
                elif i == 0:
                    ans1 = dp[i][j-1][0] * grid[i][j]
                    dp[i][j] = [ans1, ans1]
                
                elif j == 0:
                    ans1 = dp[i-1][j][0] * grid[i][j]
                    dp[i][j] = [ans1, ans1]
                
                else:
                    # Find all the combination of multiplication.
                    # For example if grid[i][j] < 0 i.e -2 and dp[i-1][j] = [2,-2] and dp[i][j-1] = [1,2] 
                    # then dp[i][j] = [max(-2*2, -2*-2, -2*1, -2*2), min(-2*2, -2*-2, -2*1, -2*2)]
                    # Only one thing you have to focus here is that if the multiplication is negative you have to store it because 
                    # it may happen that if we find a negative number later on that can make a big positve number. 
                     
                    ans1 = dp[i-1][j][0] * grid[i][j]
                    ans2 = dp[i-1][j][1] * grid[i][j]
                    ans3 = dp[i][j-1][0] * grid[i][j]
                    ans4 = dp[i][j-1][1] * grid[i][j]
                    maximum = max(ans1, ans2, ans3, ans4)
                    minimum = min(ans1, ans2, ans3 ,ans4)
                    if maximum < 0:
                        dp[i][j] = [minimum, minimum]
                    elif minimum > 0 :
                        dp[i][j] = [maximum, maximum]
                    else:
                        dp[i][j] = [maximum, minimum]
        
        if dp[row-1][col-1][0] < 0:
            return -1
        else:
            return int(dp[row-1][col-1][0] % MOD) 
        
        
-------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        numRows, numCols = len(grid), len(grid[0])
        maxProduct, minProduct = [[0] * numCols for _ in range(numRows)], [[0] * numCols for _ in range(numRows)]
        maxProduct[0][0], minProduct[0][0] = grid[0][0], grid[0][0]
        for row in range(1, numRows):
            minProduct[row][0] = minProduct[row - 1][0] * grid[row][0]
            maxProduct[row][0] = maxProduct[row - 1][0] * grid[row][0]
        for col in range(1, numCols):
            minProduct[0][col] = minProduct[0][col - 1] * grid[0][col]
            maxProduct[0][col] = maxProduct[0][col - 1] * grid[0][col]
        for row in range(1, numRows):
            for col in range(1, numCols):
                if grid[row][col] < 0:
                    maxProduct[row][col] = min(minProduct[row - 1][col], minProduct[row][col - 1]) * grid[row][col]
                    minProduct[row][col] = max(maxProduct[row - 1][col], maxProduct[row][col - 1]) * grid[row][col]
                else:
                    maxProduct[row][col] = max(maxProduct[row - 1][col], maxProduct[row][col - 1]) * grid[row][col]
                    minProduct[row][col] = min(minProduct[row - 1][col], minProduct[row][col - 1]) * grid[row][col]
        res = maxProduct[numRows - 1][numCols - 1]
        return res % 1000000007 if res >= 0 else -1
      
