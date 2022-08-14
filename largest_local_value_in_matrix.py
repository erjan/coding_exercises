'''
You are given an n x n integer matrix grid.

Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:

maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.

Return the generated matrix.
'''


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        n = len(grid)
        n2 = n-2
        maxLocal = list()

        for i in range(n2):
            temp2 = list()
            for j in range(n2):
                x = i+1
                y = j+1

                temp = max(grid[x][y],
                           grid[x-1][y], grid[x+1][y],
                           grid[x-1][y-1],
                           grid[x+1][y+1],
                           grid[x][y-1], grid[x][y+1],
                           grid[x+1][y-1], grid[x-1][y+1])

                temp2.append(temp)
            maxLocal.append(temp2)

        return maxLocal
