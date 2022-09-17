'''
Alice and Bob take turns playing a game, with Alice starting first.

There are n stones arranged in a row. On each player's turn, while the number of stones is more than one, they will do the following:

Choose an integer x > 1, and remove the leftmost x stones from the row.
Add the sum of the removed stones' values to the player's score.
Place a new stone, whose value is equal to that sum, on the left side of the row.
The game stops when only one stone is left in the row.

The score difference between Alice and Bob is (Alice's score - Bob's score). Alice's goal is to maximize the score difference, and Bob's goal is the minimize the score difference.

Given an integer array stones of length n where stones[i] represents the value of the ith stone from the left, return the score difference between Alice and Bob if they both play optimally.
'''

class Solution:
    def stoneGameVIII(self, s: List[int]) -> int:
        s, res = list(accumulate(s)), 0
        for i in range(len(s) - 1, 0, -1):
            res = s[i] if i == len(s) - 1 else max(res, s[i] - res)
        return res
      
----------------------------------------------------------------------------------------
class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:        
        s = sum(stones)  
        dp = s
        for i in range(len(stones)-2, 0, -1):
            s -= stones[i+1]
            dp = max(dp, s - dp)    
        return dp
-----------------------------------------
class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        prefix = [0]
        for x in stones: prefix.append(prefix[-1] + x)
        
        @cache
        def fn(i): 
            """Return max score difference."""
            if i+1 == len(stones): return prefix[-1]
            return max(fn(i+1), prefix[i+1] - fn(i+1))
        
        return fn(1)
