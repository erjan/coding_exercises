'''
On an n x n chessboard, a knight starts at the cell (row, column) and attempts to make exactly k moves. The rows and columns are 0-indexed, so the top-left cell is (0, 0), and the bottom-right cell is (n - 1, n - 1).

A chess knight has eight possible moves it can make, as illustrated below. Each move is two cells in a cardinal direction, then one cell in an orthogonal direction.


Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

The knight continues moving until it has made exactly k moves or has moved off the chessboard.

Return the probability that the knight remains on the board after it has stopped moving.

 
'''


--------------------------------------------------------------------------------------------------------------------------------------
We set 2 super simple base cases: if we're already outside the grid, the probability of staying inside is 0. If we're inside the grid and have no moves left to make, the probability of staying inside is 1. Otherwise, we make 8 recursive calls and average them. We use Python's built-in lru_cache for memoization.

Final code:

def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
	@functools.lru_cache(None)
	def travels(xcurr, ycurr, k):
		if xcurr < 0 or xcurr >= N or ycurr < 0 or ycurr >= N: 
			# We're already outside the grid, so probability of staying inside is 0
			return 0
		elif k == 0:
			# We're inside the grid and have no more moves to make
			return 1
		else:
			# Otherwise, we make one of 8 possible moves and find the probability of staying inside after 
			# k - 1 more moves. Because each move is equally likely, we average all of these probabilities.
			return (travels(xcurr + 2, ycurr + 1, k - 1) + 
					travels(xcurr + 1, ycurr + 2, k - 1) + 
					travels(xcurr - 1, ycurr + 2, k - 1) + 
					travels(xcurr - 2, ycurr + 1, k - 1) + 
					travels(xcurr - 2, ycurr - 1, k - 1) + 
					travels(xcurr - 1, ycurr - 2, k - 1) + 
					travels(xcurr + 1, ycurr - 2, k - 1) +   
					travels(xcurr + 2, ycurr - 1, k - 1)) / 8

	return travels(r, c, K)
------------------------------------------------------------------------------------------------------------------------------
The possibility that the knight remains on board on the K-th move can be calculated as:
p = (count of all K-th moves ending up within board) / (8 ^ K)

def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
	"""
	BFS, use a set to track the nodes in a tree remaining in the board in each step
	Time: O(8 * N ^ 2 * K)
	Space: O(N ^ 2)
	"""
	q = {(r, c): 1}
	level = 0
	directions = {(dx, dy) for dx in (-2, -1, 1, 2) for dy in (-2, -1, 1, 2) if abs(dx) + abs(dy) == 3}
	is_in_board = lambda r, c: 0 <= r < N and 0 <= c < N
	while level < K and q:
		next_q = collections.defaultdict(int)
		for coord, count in q.items():
			x, y = coord
			for dx, dy in directions:
				if is_in_board(x + dx, y + dy):
					next_q[(x + dx, y + dy)] += count
		q = next_q
		level += 1
		# print(f'Level {level}: {q}')

	return sum(q.values()) / 8 ** K
DFS Solution
def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
	"""
	dfs with memo
	Time: O(K*N^2)
	Space: O(K*N^2)
	"""
	is_in_board = lambda r, c: 0 <= r < N and  0 <= c < N
	directions = {(dx, dy) for dx in (-2, -1, 1, 2) for dy in (-2, -1, 1, 2) if abs(dx) + abs(dy) == 3}
	memo = {}
	def dfs(K, r, c):
		nonlocal memo
		if K == 0:
			return 1
		if (K, r, c) in memo:
			return memo[(K, r, c)]

		p = 0
		for dx, dy in directions:
			x, y = r + dx, c + dy
			if is_in_board(x, y):
				p += dfs(K - 1, x, y) / 8
		memo[(K, r, c)] = p
		return p

	return dfs(K, r, c)
