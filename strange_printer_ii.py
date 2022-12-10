'''
There is a strange printer with the following two special requirements:

On each turn, the printer will print a solid rectangular pattern of a single color on the grid. This will cover up the existing colors in the rectangle.
Once the printer has used a color for the above operation, the same color cannot be used again.
You are given a m x n matrix targetGrid, where targetGrid[row][col] is the color in the position (row, col) of the grid.

Return true if it is possible to print the matrix targetGrid, otherwise, return false.
'''



class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        m, n = len(targetGrid), len(targetGrid[0]) # dimensions 
        
        # build directed graph (adjacency list)
        digraph = {} 
        for c in range(1, 61): 
            imn = jmn = 60
            imx = jmx = 0
            for i in range(m): 
                for j in range(n): 
                    if targetGrid[i][j] == c: 
                        imn = min(imn, i)
                        imx = max(imx, i)
                        jmn = min(jmn, j)
                        jmx = max(jmx, j)
            for i in range(imn, imx+1):
                for j in range(jmn, jmx+1): 
                    if targetGrid[i][j] != c: 
                        digraph.setdefault(c, set()).add(targetGrid[i][j])
            
        # check for cycle in digraph (tri-color)
        def dfs(n): 
            """Return True if a cycle is detected."""
            if seen[n]: return seen[n] == 1 
            seen[n] = 1
            if any(dfs(nn) for nn in digraph.get(n, set())): return True 
            seen[n] = 2
            return False 
        
        seen = [0]*61
        return not any(dfs(i) for i in range(61)) # cycle, i.e. impossible to print 
      
------------------------------------------------------------------------------------------------------------------

class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        N, M, colors = len(targetGrid), len(targetGrid[0]) if len(targetGrid) else 0, max( max(r) for r in targetGrid )
        boundry = [(N, 0, M, 0)]*(colors+1) # boundry[i] = (a, b, c, d) if the color shows in rows [a:b+1] and colums [c:d+1]
        resolved = set()
        for x in range(N):
            for y in range(M):
                c = targetGrid[x][y]
                boundry[c] = min(x, boundry[c][0]), max(x, boundry[c][1]), min(y, boundry[c][2]), max(y, boundry[c][3])
        
        def cleanRectangle(color: int) -> bool: # if we can form a rectangle, remove this color (label 0)
            frX, toX, frY, toY = boundry[color]
            if color in resolved:
                return True
            for i in range(frX, toX+1):
                for j in range(frY, toY+1):
                    if targetGrid[i][j] == color:
                        targetGrid[i][j] = -1
                    elif targetGrid[i][j] == -1: # circle back to a unsolved color, detect a deadlock (circular dependency)
                        return False
                    elif targetGrid[i][j] > 0 and not cleanRectangle(targetGrid[i][j]):
                        return False
            for i in range(frX, toX+1):
                for j in range(frY, toY+1):
                    targetGrid[i][j] = 0
            resolved.add(color)
            return True
        
        for i in range(N):
            for j in range(M):
                if targetGrid[i][j] and not cleanRectangle(targetGrid[i][j]):
                    return False
        return True
