'''
Alice and Bob continue their games with piles of stones. There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.

Alice and Bob take turns, with Alice starting first. On each player's turn, that player can take 1, 2, or 3 stones from the first remaining stones in the row.

The score of each player is the sum of the values of the stones taken. The score of each player is 0 initially.

The objective of the game is to end with the highest score, and the winner is the player with the highest score and there could be a tie. The game continues until all the stones have been taken.

Assume Alice and Bob play optimally.

Return "Alice" if Alice will win, "Bob" if Bob will win, or "Tie" if they will end the game with the same score.
'''

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        seen = {}

        def maxWin(idx):
            if idx == len(stoneValue):
                return 0
            if idx in seen:
                return seen[idx]
            
            myStone = 0
            res = float('-inf')
            for i in range(idx, min(idx + 3, len(stoneValue))):
                myStone += stoneValue[i]
                res = max(res, myStone - maxWin(i+1))
            seen[idx] = res
            return res
        
        res = maxWin(0)
        if res > 0:
            return 'Alice'
        elif res < 0:
            return 'Bob'
        else:
            return 'Tie'
          
---------------------------------------------------------------------------------------
It's an optimal substructure problem so we can use dp to solve it.
And the intuition for this problem is our highest score at i = sum(score[i:j]) - opponent's highest score at j as both sides play optimally.
Suppose dp[i] indicates the highest score we can achieve from stone[i:]. There are three possible index for next move (i+1, i+2, i+3).
Thus the highest score opponent can achieve is dp[i+k] where k in {1,2,3}. And our highest score would be max(stone[i:i+k] - dp[i+k]) where k in {1,2,3}

Finally we just need to check whether dp[0] >=< 0.

def stoneGameIII(stoneValue):
    n = len(stoneValue)
    dp = [0] * (n + 3)
    for i in range(n-1, -1, -1):
        dp[i] = max(sum(stoneValue[i:i+k]) - dp[i+k] for k in range(1, 4))
    return "Alice" if dp[0] > 0 else "Bob" if dp[0] < 0 else "Tie"-
  
--------------------------------------------------------------------  
