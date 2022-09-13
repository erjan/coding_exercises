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
class Solution:
    def stoneGameIII(self, num: List[int]) -> str:
        dp=[0]*(len(num)+1)
        i=len(num)-1
        
        while i>=0:
            ans=-1001
            ans=max(ans,num[i]-dp[i+1])
            
            if i+1<len(num):
                ans=max(ans,num[i]+num[i+1]-dp[i+2])
            
            if i+2<len(num):
                ans=max(ans,num[i]+num[i+1]+num[i+2]-dp[i+3])
            dp[i]=ans
            i-=1
            
            
        alice=dp[0]
        if alice>0:
            return "Alice"
        elif alice<0:
            return "Bob"
        else:
            return "Tie"
-------------------------------------------------------------------------
Use dp[i] to represent for a player (could be Alice or Bob) who is about to play with the first stone in the row is the ith in the array, the maximum value he/she can get throughout the game.

With this definition, the state transition formula is clear:
starting from the ith stone, there are a total of sum(stoneValue[i:]) in the game.
There are 3 options of this player to play, pick 1, 2, or 3 stones. Let's use 2 as an example, since this player picked 2 stones in this turn, the next player starts at ith+2 stone, and the maximum the next player can get is dp[i+2] (according to the definition of our dp). So consider all 3 opitons:

dp[i] = sum(stoneValue[i:]) - min(dp[i+1], dp[i+2], dp[i+3])

def stoneGameIII(self, stoneValue):


    dp = [0 for i in range(len(stoneValue) + 3)]
    
    arrsum = 0 # arrsum aggreagtion from the end to avoid repetitive sumation
    for i in range(len(stoneValue)-1,-1,-1):
        arrsum += stoneValue[i]
        dp[i] = arrsum - min(dp[i+1], dp[i+2], dp[i+3]) # we want to maximize the value for current player so we need to minimize the gain for next player
    
    score = dp[0] # dp[0] is the maximum gain for player who plays first
    s = score*2 - arrsum
    if s > 0: return 'Alice'
    if s == 0: return 'Tie'
    if s < 0: return 'Bob'
    
--------------------------------------------------------------------------------------
class Solution:
    def stoneGameIII(self, sv: List[int]) -> str:
        s=0
        dp=[0 for _ in range(50003)]
        for i in range(len(sv)-1,-1,-1):
            dp[i]=-float('inf')
            s+=sv[i]
            for j in range(1,4):
                dp[i]=max(dp[i],s-dp[i+j])
        if s-dp[0]==dp[0]:
            return 'Tie'
        elif s-dp[0]>dp[0]:
            return 'Bob'
        else:
            return 'Alice'
        
