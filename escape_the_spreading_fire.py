'''
You are given a 0-indexed 2D integer array grid of size m x n which represents a field. Each cell has one of three values:

0 represents grass,
1 represents fire,
2 represents a wall that you and fire cannot pass through.
You are situated in the top-left cell, (0, 0), and you want to travel to the safehouse at the bottom-right cell, (m - 1, n - 1). Every minute, you may move to an adjacent grass cell. After your move, every fire cell will spread to all adjacent cells that are not walls.

Return the maximum number of minutes that you can stay in your initial position before moving while still safely reaching the safehouse. If this is impossible, return -1. If you can always reach the safehouse regardless of the minutes stayed, return 109.

Note that even if the fire spreads to the safehouse immediately after you have reached it, it will be counted as safely reaching the safehouse.

A cell is adjacent to another cell if the former is directly north, east, south, or west of the latter (i.e., their sides are touching).
'''


class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
      
      #region growing to assign each grass with the time that it will catch fire
      
      m, n = len(grid), len(grid[0])
      
      start = []
      
      for i in range(m):
        for j in range(n):
          if grid[i][j] == 1:
            start.append([i,j])
            grid[i][j] = 'F'
          elif grid[i][j] == 2:
            grid[i][j] = 'W'
            
      visited = set()
      for element in start: visited.add(tuple(element))
        
      time = 1
      
      while start:
        new_start = []
        for x, y in start:
          if x >= 1:
            if grid[x-1][y] == 0 and (x-1, y) not in visited:
              new_start.append([x-1, y])
              visited.add((x-1, y))
              grid[x-1][y] = time
          if x < m-1:
            if grid[x+1][y] == 0 and (x+1, y) not in visited:
              new_start.append([x+1, y])
              visited.add((x+1, y))
              grid[x+1][y] = time
          if y >= 1:
            if grid[x][y-1] == 0 and (x, y-1) not in visited:
              new_start.append([x, y-1])
              visited.add((x, y-1))
              grid[x][y-1] = time
          if y < n-1:
            if grid[x][y+1] == 0 and (x, y+1) not in visited:
              new_start.append([x, y+1])
              visited.add((x, y+1))
              grid[x][y+1] = time
        time += 1
        start = new_start
        
        
      #memo variable will save time from search path that is already proved to be impossible
      memo = {}
      def search(x, y, time, visited):
        if (x,y) in memo and time >= memo[(x,y)]: return False
        if time > grid[-1][-1]: return False
        if x == m-1 and y == n-1:
          if grid[x][y] == 0:
            return True
          else: 
            if grid[x][y] >= time:
              return True
        else:
          if grid[x][y] == time: return False
          visited.add((x,y))
          if x >= 1:
            if grid[x-1][y] != 'W' and grid[x-1][y] != 'F' and grid[x-1][y] > time  and (x-1, y) not in visited:
              res = search(x-1, y, time+1, visited)
              if res: return True
          if x < m-1:
            if grid[x+1][y] != 'W' and grid[x+1][y] != 'F' and grid[x+1][y] > time  and (x+1, y) not in visited:
              res = search(x+1, y, time+1, visited)
              if res: return True
          if y >= 1:
            if grid[x][y-1] != 'W' and grid[x][y-1] != 'F' and grid[x][y-1] > time  and (x, y-1) not in visited:
              res = search(x, y-1, time+1, visited)
              if res: return True
          if y < n-1:
            if grid[x][y+1] != 'W' and grid[x][y+1] != 'F' and grid[x][y+1] > time  and (x, y+1) not in visited:
              res = search(x, y+1, time+1, visited)
              if res: return True
          visited.remove((x,y))
          if (x,y) not in memo: memo[(x,y)] = time
          else: memo[(x,y)] = min(time, memo[(x,y)])
          return False
        
      if grid[0][0] == 0:
        if search(0, 0, -sys.maxsize, set()): return 10**9
        else: return -1
      else:
        start, end = 0, grid[0][0]-1
        
        #binary search
 
        while start < end:
          mid = ceil((start + end)/2)
          if search(0, 0, mid, set()):
            start = mid
          else:
            end = mid - 1
        if start != 0: return start
        else:
          if search(0, 0, 0, set()): return 0
          else: return -1
      
-------------------------------------------------------------------------------------------------------------------------------
class Solution:
	def maximumMinutes(self, grid: List[List[int]]) -> int:
		mx = float('inf')
		m,n = len(grid), len(grid[0])
		arr = [[mx for i in range(n)] for j in range(m)]
		q = deque([(j,i) for i in range(n) for j in range(m) if grid[j][i] == 1])
		for i,j in q:
			arr[i][j] = 0
		visited = set(q)
		temp = 0
		while q:
			l = len(q)
			for j in range(l):
				x,y = q.popleft()
				visited.add((x,y))
				arr[x][y] = temp
				for i,j in (1,0),(0,1),(-1,0),(0,-1):
					xx = x+i
					yy = y+j
					if 0<=xx<m and 0<=yy<n and grid[xx][yy] == 0 and (xx,yy) not in visited:
						q.append((xx,yy))
			temp += 1
		def solve(x,y,temp):
			nonlocal visited
			val = arr[x][y]
			if x == m-1 and y == n-1:
				return temp <= val
			visited.add((x,y))
			if val <= temp:return False
			for i,j in (1,0),(0,1),(-1,0),(0,-1):
				xx = x+i
				yy = y+j
				if 0<=xx<m and 0<=yy<n and (xx,yy) not in visited and grid[xx][yy] != 2:
					if solve(xx,yy, temp+1):
						return True
			# visited.remove((x,y))
			return False

		# for row in arr:
		#     print(*row)
		visited = set()
		if not solve(0,0,0):return -1
		l,r = 0,10**9
		ans = None
		while l <= r:
			mid = (l+r)//2
			visited = set()
			if solve(0,0,mid):
				ans = mid
				l = mid+1
			else:
				r = mid-1
		return ans
  
------------------------------------------------------------------------------------------------------------------
class Solution:
	def maximumMinutes(self, grid: List[List[int]]) -> int:
		mx = float('inf')
		m,n = len(grid), len(grid[0])
		arr = [[mx for i in range(n)] for j in range(m)]
		q = deque([(j,i) for i in range(n) for j in range(m) if grid[j][i] == 1])
		for i,j in q:
			arr[i][j] = 0
		visited = set(q)
		temp = 0
		while q:
			l = len(q)
			for j in range(l):
				x,y = q.popleft()
				visited.add((x,y))
				arr[x][y] = temp
				for i,j in (1,0),(0,1),(-1,0),(0,-1):
					xx = x+i
					yy = y+j
					if 0<=xx<m and 0<=yy<n and grid[xx][yy] == 0 and (xx,yy) not in visited:
						q.append((xx,yy))
			temp += 1
		def solve(x,y,temp):
			nonlocal visited
			val = arr[x][y]
			if x == m-1 and y == n-1:
				return temp <= val
			visited.add((x,y))
			if val <= temp:return False
			for i,j in (1,0),(0,1),(-1,0),(0,-1):
				xx = x+i
				yy = y+j
				if 0<=xx<m and 0<=yy<n and (xx,yy) not in visited and grid[xx][yy] != 2:
					if solve(xx,yy, temp+1):
						return True
			# visited.remove((x,y))
			return False

		# for row in arr:
		#     print(*row)
		visited = set()
		if not solve(0,0,0):return -1
		l,r = 0,10**9
		ans = None
		while l <= r:
			mid = (l+r)//2
			visited = set()
			if solve(0,0,mid):
				ans = mid
				l = mid+1
			else:
				r = mid-1
		return ans
        
