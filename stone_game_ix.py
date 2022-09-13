'''
Alice and Bob continue their games with stones. There is a row of n stones, and each stone has an associated value. You are given an integer array stones, where stones[i] is the value of the ith stone.

Alice and Bob take turns, with Alice starting first. On each turn, the player may remove any stone from stones. The player who removes a stone loses if the sum of the values of all removed stones is divisible by 3. Bob will win automatically if there are no remaining stones (even if it is Alice's turn).

Assuming both players play optimally, return true if Alice wins and false if Bob wins.
'''

class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        freq = defaultdict(int)
        for x in stones: freq[x % 3] += 1
        
        if freq[0]%2 == 0: return freq[1] and freq[2]
        return abs(freq[1] - freq[2]) >= 3
      
---------------------------------------------------------
class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        stones = [v % 3 for v in stones]
        
        d = defaultdict(int)
        for v in stones:
            d[v] += 1
        
        while d[1] >= 2 and d[2] >= 2:
            d[2] -= 1
            d[1] -= 1
        
        if d[0] % 2 == 0: # number of 0s will not influent the result
            if (d[1] == 1 and d[2] >= 1) or (d[2] == 1 and d[1] >= 1):
                return True
        else:
            if (d[1] == 0 and d[2] >= 3) or (d[2] == 0 and d[1] >= 3):
                return True
            if (d[1] == 1 and d[2] >= 4) or (d[2] == 1 and d[1] >= 4):
                return True

        return False
