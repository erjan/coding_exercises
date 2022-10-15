'''
You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.
'''


class Solution:
    def nearestExit(self, maze: List[List[str]], entr: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        deq = deque()
        deq.append([entr[0], entr[1], -1])
        
        while deq:
            r, c, dist = deq.popleft()
            if not (0 <= r < rows and 0 <= c < cols):
                if dist > 0:
                    return dist
                continue
            if maze[r][c] == '+':
                continue
            
            maze[r][c] = '+'
            for _r, _c in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                deq.append([r + _r, c + _c, dist + 1])
        
        return -1
      
---------------------------------------------------------------------------------------------------------
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        q = collections.deque([(*entrance, 0)])
        m, n = len(maze), len(maze[0])
        maze[entrance[0]][entrance[1]] == '+'    
        while q:
            x, y, c = q.popleft()
            if (x == 0 or x == m-1 or y == 0 or y == n-1) and [x, y] != entrance:
                return c
            for i, j in [(x+_x, y+_y) for _x, _y in [(-1, 0), (1, 0), (0, -1), (0, 1)]]:
                if 0 <= i < m and 0 <= j < n and maze[i][j] == '.':
                    maze[i][j] = '+'
                    q.append((i, j, c + 1))
        return -1
      
----------------------------------------------------------------------------------------------------------------------------------
def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
	m, n = len(maze), len(maze[0])
	q = [entrance]
	vis = {(entrance[0], entrance[1])}
	ans = 0
	while(q):
		l = len(q)
		ans += 1
		for _ in range(l):
			[i, j] = q.pop(0)
			if((i == 0 or i == m-1 or j == 0 or j == n-1) and [i, j] != entrance):
				return ans-1
			for x, y in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
				if(0<=i+x<m and 0<=j+y<n and maze[i+x][j+y] == "." and (i+x, j+y) not in vis):
					vis.add((i+x, j+y))
					q.append([i+x, j+y])
	return -1
