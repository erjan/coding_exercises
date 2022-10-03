'''
You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.

Return the number of islands in grid2 that are considered sub-islands.
'''

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        def isIsland(i, j):
            flag = True
            if grid1[i][j]!=1:
                flag = False
            
            if i-1>=0 and grid2[i-1][j]==1:
                grid2[i-1][j] = 2
                flag = isIsland(i-1,j) and flag and grid1[i-1][j]
                    
            if i+1<n and grid2[i+1][j]==1:
                grid2[i+1][j] = 2
                flag = isIsland(i+1,j) and flag and grid1[i+1][j]
            
            if j-1>=0 and grid2[i][j-1]==1:
                grid2[i][j-1] = 2
                flag = isIsland(i,j-1) and flag and grid1[i][j-1]
            
            if j+1<m and grid2[i][j+1]==1:
                grid2[i][j+1]=2
                flag = isIsland(i,j+1) and flag and grid1[i][j+1]
            return flag
            
        
        count = 0
        n = len(grid2)
        m = len(grid2[0])
        for i in range(n):
            for j in range(m):
                if grid2[i][j]==1:
                    grid2[i][j] = 2
                    if isIsland(i, j):
                        count += 1
        return count
