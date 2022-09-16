'''
You start at the cell (rStart, cStart) of an rows x cols grid facing east. The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.

You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later.). Eventually, we reach all rows * cols spaces of the grid.

Return an array of coordinates representing the positions of the grid in the order you visited them.

 
 '''

Explanation
Starting with a step length of 1, move one time to right, then turn; move one time to below
Increase step length, 1 + 1 = 2, move 2 times to left, then turn; move 2 times to above
So, for each step length, we will move step for 2 directions, then increase step by one; and repeat
To summarize:
Step == 1, move*step, turn, move*step, turn
Step += 1, move*step, turn, move*step, turn
Step += 1, move*step, turn, move*step, turn
... ... repeat
Implementation
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        total, cnt, step, i = rows * cols, 1, 1, 0
        ans = [[rStart, cStart]]
        direction = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)} # setup direction movements
        while cnt < total:
            for k in range(step):
                rStart, cStart = rStart+direction[i][0], cStart + direction[i][1]
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    ans.append([rStart, cStart])
                    cnt += 1       # count visited 
            i = (i + 1) % 4        # changing direction
            step += not i % 2      # increase step every 2 directions
        return ans
      
-------------------------------------------------

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        ans = [[rStart, cStart]]
        val = 1
        i, j = rStart, cStart
        def is_valid(i, j):
            if 0 <= i < rows and 0 <= j < cols:
                return True
            return False
        
        while True:
            if len(ans) == rows * cols:
                return ans
            
            # go right val times
            for _ in range(val):
                j+=1
                if is_valid(i,j):
                    ans.append([i,j])
            # go bottom val times
            for _ in range(val):
                i+=1
                if is_valid(i,j):
                    ans.append([i,j])
            # go left val+1 times
            for _ in range(val+1):
                j-=1
                if is_valid(i,j):
                    ans.append([i,j])
            # go up val+1 times
            for _ in range(val+1):
                i-=1
                if is_valid(i,j):
                    ans.append([i,j])
            val+=2
