'''
You are given an m x n grid grid where:

'.' is an empty cell.
'#' is a wall.
'@' is the starting point.
Lowercase letters represent keys.
Uppercase letters represent locks.
You start at the starting point and one move consists of walking one space in one of the four cardinal directions. You cannot walk outside the grid, or walk into a wall.

If you walk over a key, you can pick it up and you cannot walk over a lock unless you have its corresponding key.

For some 1 <= k <= 6, there is exactly one lowercase and one uppercase letter of the first k letters of the English alphabet in the grid. This means that there is exactly one key for each lock, and one lock for each key; and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.

Return the lowest number of moves to acquire all keys. If it is impossible, return -1.
'''


def shortestPathAllKeys(self, grid: List[str]) -> int:
	def bfs(x, y, k):
		q = [(x, y, 0)]
		cost = 0
		while(q):
			l = len(q)
			cost += 1
			for _ in range(l):
				i, j, mask = q.pop(0)
				for di, dj in dir:
					ni, nj = i+di, j+dj
					if(0<=ni<m and 0<=nj<n and mask not in vis[ni][nj]):
						char = grid[ni][nj]
						if(char == "#"): continue
						if(char in ".@"):
							vis[ni][nj].add(mask)
							q.append((ni, nj, mask))
						elif(char.islower()):
							n_mask = mask | (1<<(ord(char)-97))
							vis[ni][nj].add(n_mask)
							if(n_mask == 2**k - 1):
								return cost
							q.append((ni, nj, n_mask))
						elif(mask & 1<<(ord(char)-65)):
							vis[ni][nj].add(mask)
							q.append((ni, nj, mask))
		return -1
	m, n = len(grid), len(grid[0])
	dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
	k = 0
	for i in range(m):
		for j in range(n):
			if(grid[i][j].islower()):
				k += 1
			elif(grid[i][j] == "@"):
				si, sj = i, j
	vis = [[set() for _ in range(n)] for _ in range(m)]
	vis[si][sj].add(0)
	return bfs(si, sj, k)
