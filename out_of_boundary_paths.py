'''
There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.
'''


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

        def solve(i, j, maxMove):
            if maxMove < 0:
                return 0
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1
            
            a = solve(i-1, j, maxMove - 1)
            b = solve(i+1, j, maxMove - 1)
            c = solve(i, j-1, maxMove - 1)
            d = solve(i, j+1, maxMove - 1)
            
            return a + b + c + d
        
        return solve(startRow, startColumn, maxMove) % 1000000007
---------------------------------------------------------------------------------------------------------------------------
	class Solution:
		def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

			@lru_cache(None)
			def moves(move,row,col):
				if row==m or row<0 or col<0 or col==n:
					return 1
				if move==0:
					return 0
				move-=1

				return (moves(move,row+1,col)+moves(move,row,col+1)+moves(move,row-1,col)+moves(move,row,col-1))%((10**9)+7)


			return moves(maxMove,startRow,startColumn)
--------------------------------------------------------------------------------------------------------
class Solution:
		def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
			dp = [[0] * n for _ in range(m)]
			dp[startRow][startColumn] = 1
			MOD = 10**9 + 7
			answer = 0
			for _ in range(maxMove):
				next_dp = [[0] * n for _ in range(m)]
				for r in range(m):
					for c in range(n):
						for nx, ny in ((r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)):
							if 0 <= nx < m and 0 <= ny < n:
								next_dp[nx][ny] = (next_dp[nx][ny] + dp[r][c]) %  MOD
							else:
								answer = (answer + dp[r][c]) % MOD
				dp = next_dp                 
			return answer
