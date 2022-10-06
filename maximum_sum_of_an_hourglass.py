'''
You are given an m x n integer matrix grid.

We define an hourglass as a part of the matrix with the following form:
'''


#my own solution!!!!!!!!!!!!!!!
class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        
        
        m = len(grid)
        n = len(grid[0])
        
        res = []
        
        for i in range(m-2):
            for j in range(n-2):
                
                top = grid[i][j] + grid[i][j+1] + grid[i][j+2]
                center = grid[i+1][j+1]
                bottom = grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]
                
                res.append(top+center+bottom)
        
        return max(res)
        
        
-----------------------------------------------------------------        
class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:

        ans = 0

        for i in range(1, len(grid)-1):
            for j in range(1, len(grid[0])-1):

                sm = ( grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1]
                                      + grid[i  ][j] +
                       grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1] )

                if sm > ans: ans = sm

        return ans
      
----------------------------------------------------------------------------------------------  
class Solution:
    def maxSum(self, x: List[List[int]]) -> int:
        
        # initialize max to 0
        mx = 0
        
        m = len(x)
        n = len(x[0])
        
        # traverse through 
        # rows: m-3 times
        # columns: n-3 times for each row
        for i in range(m-2):
            for j in range(n-2):
                
                # add top horizontal items
                mSum =0
                for k in range(j, j+3):
                    mSum +=x[i][k]
                
                # add bottom horizontal items
                for k in range(j, j+3):
                    mSum +=x[i+2][k]
                
                # add middle element of the hourglass
                mSum += x[i+1][j+1]
                
                # update max if we get new maximum
                if mx < mSum:
                    mx = mSum
        return mx
