'''
You are given a 0-indexed m x n binary matrix land where a 0 represents a hectare of forested land and a 1 represents a hectare of farmland.

To keep the land organized, there are designated rectangular areas of hectares that consist entirely of farmland. These rectangular areas are called groups. No two groups are adjacent, meaning farmland in one group is not four-directionally adjacent to another farmland in a different group.

land can be represented by a coordinate system where the top left corner of land is (0, 0) and the bottom right corner of land is (m-1, n-1). Find the coordinates of the top left and bottom right corner of each group of farmland. A group of farmland with a top left corner at (r1, c1) and a bottom right corner at (r2, c2) is represented by the 4-length array [r1, c1, r2, c2].

Return a 2D array containing the 4-length arrays described above for each group of farmland in land. If there are no groups of farmland, return an empty array. You may return the answer in any order.
'''


def findFarmland(self, grid):
        self.ans=[]
        row=len(grid)
        col=len(grid[0])
        
        def helper(i,j,grid):
            if i<0 or j<0 or j>=len(grid[0]) or i>=len(grid) or grid[i][j]==0:return (0,0)
            (nx,ny)=(i,j)
            grid[i][j]=0
            for x,y in [(1,0),(0,1)]:
                (nx,ny)=max((nx,ny),helper(i+x,j+y,grid))
            return (nx,ny)
                  
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    (x,y)=helper(i,j,grid)
                    self.ans.append([i,j,x,y])
        return self.ans
      
--------------------------------------------------------------------------------------------------------------
def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        group = []
        m, n = len(land), len(land[0])
        
        def dfs(row: int, col: int) -> (int, int):
            if row < 0 or row >= m or col < 0 or col >= n or land[row][col] == 0:
                return (0, 0)
            
            land[row][col] = 0
            
            h_r1, h_c1 = dfs(row + 1, col)
            h_r2, h_c2 = dfs(row, col + 1)
            
            h_r = max(h_r1, h_r2, row)
            h_c = max(h_c1, h_c2, col)
            
            return (h_r, h_c)
        
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    x, y = dfs(i, j)
                    group.append([i, j, x, y])
                    
        return group
