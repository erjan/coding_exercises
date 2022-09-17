'''
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there are n stones in a pile. On each player's turn, that player makes a move consisting of removing any non-zero square number of stones in the pile.

Also, if a player cannot make a move, he/she loses the game.

Given a positive integer n, return true if and only if Alice wins the game otherwise return false, assuming both players play optimally.
'''

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        squares = []
        curSquare = 1
        for i in range(1, n + 1):
            if i == curSquare * curSquare:
                squares.append(i)
                curSquare += 1
                dp[i] = True
            else:
                for square in squares:
                    if not dp[i - square]:
                        dp[i] = True
                        break
        return dp[n]
      
----------------------------------------------
class Solution:
		def winnerSquareGame(self, n: int) -> bool:
			dp = [False]*(n+1)
			for i in range(1,n+1):
				j = 1
				while j*j <= i:
					dp[i] |= not dp[i-j*j]
					j+=1
			return dp[n]
