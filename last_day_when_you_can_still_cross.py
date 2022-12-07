'''
There is a 1-based binary matrix where 0 represents land and 1 represents water. You are given integers row and col representing the number of rows and columns in the matrix, respectively.

Initially on day 0, the entire matrix is land. However, each day a new cell becomes flooded with water. You are given a 1-based 2D array cells, where cells[i] = [ri, ci] represents that on the ith day, the cell on the rith row and cith column (1-based coordinates) will be covered with water (i.e., changed to 1).

You want to find the last day that it is possible to walk from the top to the bottom by only walking on land cells. You can start from any cell in the top row and end at any cell in the bottom row. You can only travel in the four cardinal directions (left, right, up, and down).

Return the last day where it is possible to walk from the top to the bottom by only walking on land cells.
'''


class Solution(object):
    def latestDayToCross(self, row, col, cells):
        l,h=0,len(cells)-1
        ans=-1
        while l<=h:
            m=(l+h)>>1
            if self.isPath(cells,m,row,col):
                l=m+1
                ans=m+1
            else:
                h=m-1
        return ans
    def isPath(self,cells,ind,row,col):
        grid=[[0 for i in range(col)] for j in range(row)]
        for i in range(ind+1):
            x,y=cells[i]
            grid[x-1][y-1]=1
        vis=set()
        for i in range(col):
            if grid[0][i]!=1:
                dq=deque()
                dq.append((0,i))
                dr=[(-1,0),(0,-1),(1,0),(0,1)]
                while dq:
                    x,y=dq.popleft()
                    if x==row-1:
                        return True
                    for d in dr:
                        dx,dy=d
                        if 0<=x+dx<row and 0<=y+dy<col and grid[x+dx][y+dy]!=1 and (x+dx,y+dy) not in vis:
                            vis.add((x+dx,y+dy))
                            dq.append((x+dx,y+dy))
        return False
        
-------------------------------------------------------------------------------------------------------------------
def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        grid = [[0]*col for i in range(row)]
        for i in range(len(cells)):
            grid[cells[i][0]-1][cells[i][1]-1] = i+1
			
		# use binary search to find the max time
        lower = 0
        upper = row*col
        
        while lower<upper:
            i = (lower+upper)//2
            if self.canCross(i, grid):
                lower = i
            else:
                upper = i-1
            if i==(lower+upper)//2:
                if self.canCross(i+1, grid):
                    return i+1
                else:
                    return i
        return lower
        
	# given time t, check if it's able to cross using BFS
    def canCross(self, t: int, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        cur = set()
        for j in range(n):
            cur.add((0,j))
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        visited = set()
        
        while len(cur)>0:
            next_pos = set()
            for pos in cur:
                if pos in visited:
                    continue
                x,y = pos
                visited.add(pos)
                if (0<=x<m) & (0<=y<n):
                    if (x==m-1):
                        if grid[x][y] > t:
                            return True
                    if grid[x][y] > t:
                        # can safely pass this point
                        next_pos.add((x+1,y))
                        next_pos.add((x-1,y))
                        next_pos.add((x,y+1))
                        next_pos.add((x,y-1))
            cur = next_pos
                    
        return False

--------------------------------------------------------------------------------------------------------------------
class UF:
    def __init__(self, m, n):
        self.n, self.loc_id, c_id = n, dict(), 0
        self.col_set = [set() for _ in range(m*n)]
        for i in range(m):                       # Assign id for each location (i ,j)
            for j in range(n):
                self.loc_id[(i, j)] = c_id
                self.col_set[c_id].add(j)
                c_id += 1
        self.p = [i for i in range(m*n)]         # Initialize parents array `p`
        
    def find(self, i):
        if self.p[i] != i:
            self.p[i] = self.find(self.p[i])
        return self.p[i]    
    
    def union(self, i, j):
        pi, pj = self.find(i), self.find(j)
        if pi != pj:
            self.p[pj] = pi                      # Update `pi`
            self.col_set[pi] = self.col_set[pi] | self.col_set[pj]  # Take union of two sets (union all occupied columns)
        return len(self.col_set[pi]) == self.n   # if length of col_set[pi] == self.n, meaning this piece occupied all columns from 1 to `col` inclusive, meaning we are blocked
            
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        uf, visited = UF(row, col), set()
        for i, (x, y) in enumerate(cells):
            x, y = x-1, y-1
            visited.add((x, y))
            for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1), (0, 1), (0, -1)]:
                _x, _y = x+dx, y+dy              # Check if neighbor is flooded
                if 0 <= _x < row and 0 <= _y < col and (_x, _y) in visited:
                    id1, id2 = uf.loc_id[(_x, _y)], uf.loc_id[(x, y)]
                    if uf.union(id1, id2): return i # Union two flooded piece and return index if union return True
        return -1
