'''
You have a 2-D grid of size m x n representing a box, and you have n balls. The box is open on the top and bottom sides.

Each cell in the box has a diagonal board spanning two corners of the cell that can redirect a ball to the right or to the left.

A board that redirects the ball to the right spans the top-left corner to the bottom-right corner and is represented in the grid as 1.
A board that redirects the ball to the left spans the top-right corner to the bottom-left corner and is represented in the grid as -1.
We drop one ball at the top of each column of the box. Each ball can get stuck in the box or fall out of the bottom. A ball gets stuck if it hits a "V" shaped pattern between two boards or if a board redirects the ball into either wall of the box.

Return an array answer of size n where answer[i] is the column that the ball falls out of at the bottom after dropping the ball from the ith column at the top, or -1 if the ball gets stuck in the box.



Let the ball be in j column and i row., then at next row :

If grid[i][j] == 1 , then ball will move to right column only if grid[i][j+1] == 1. Otherwise it gets struck.
If grid[i][j] == -1 , then ball will move to left column only if grid[i][j-1] == -1. Otherwise it gets struck.
'''

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        
        m,n=len(grid),len(grid[0])
        for i in range(m):
            grid[i].insert(0,1)
            grid[i].append(-1)
        res=[]
        
        for k in range(1,n+1):
            i , j = 0 , k
            struck = False
            while i<m:
                if grid[i][j]==1:
                    if grid[i][j+1]==1:
                        j+=1
                    else:
                        struck=True
                        break
                else:
                    if grid[i][j-1]==-1:
                        j-=1
                    else:
                        struck=True
                        break
                i+=1
            if struck:
                res.append(-1)
            else:
                res.append(j-1)
                
        return res
