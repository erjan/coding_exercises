'''
In an n*n grid, there is a snake that spans 2 cells and starts moving from the top left corner at (0, 0) and (0, 1). The grid has empty cells represented by zeros and blocked cells represented by ones. The snake wants to reach the lower right corner at (n-1, n-2) and (n-1, n-1).

In one move the snake can:

Move one cell to the right if there are no blocked cells there. This move keeps the horizontal/vertical position of the snake as it is.
Move down one cell if there are no blocked cells there. This move keeps the horizontal/vertical position of the snake as it is.
Rotate clockwise if it's in a horizontal position and the two cells under it are both empty. In that case the snake moves from (r, c) and (r, c+1) to (r, c) and (r+1, c).
'''


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        queue , vis , n = [(0,1,0,0)] , {} , len(grid)
        while queue:
            x,y,pos,moves = queue.pop(0)
            if x == y == n-1 and pos == 0: return moves
            if pos == 0:
                if y + 1 < n and grid[x][y+1] == 0 and (x,y+1,0) not in vis:
                    vis[(x,y+1,0)] = True
                    queue.append((x,y+1,0,moves+1))
                
                if x + 1 < n and grid[x+1][y-1] == 0 and grid[x+1][y] == 0:
                    if (x+1,y-1,1) not in vis:
                        vis[(x+1,y-1,1)] = True
                        queue.append((x+1,y-1,1,moves+1))
                    if (x+1,y,0) not in vis:
                        vis[(x+1,y,0)] = True
                        queue.append((x+1,y,0,moves+1))
            else:
                if x + 1 < n and grid[x+1][y] == 0 and (x+1,y,1) not in vis:
                    vis[(x+1,y,1)] = True
                    queue.append((x+1,y,1,moves+1))
                if y + 1 < n and grid[x-1][y+1] == grid[x][y+1] == 0:
                    if (x-1,y+1,0) not in vis:
                        vis[(x-1,y+1,0)] = True
                        queue.append((x-1,y+1,0,moves+1))
                    if (x,y+1,1) not in vis:
                        vis[(x,y+1,1)] = True
                        queue.append((x,y+1,1,moves+1))
        return -1
      
----------------------------------------------------------------------------------------------
