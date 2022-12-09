'''
There is a tournament where n players are participating. The players are standing in a single row and are numbered from 1 to n based on their initial standing position (player 1 is the first player in the row, player 2 is the second player in the row, etc.).

The tournament consists of multiple rounds (starting from round number 1). In each round, the ith player from the front of the row competes against the ith player from the end of the row, and the winner advances to the next round. When the number of players is odd for the current round, the player in the middle automatically advances to the next round.

For example, if the row consists of players 1, 2, 4, 6, 7
Player 1 competes against player 7.
Player 2 competes against player 6.
Player 4 automatically advances to the next round.
After each round is over, the winners are lined back up in the row based on the original ordering assigned to them initially (ascending order).

The players numbered firstPlayer and secondPlayer are the best in the tournament. They can win against any other player before they compete against each other. If any two other players compete against each other, either of them might win, and thus you may choose the outcome of this round.

Given the integers n, firstPlayer, and secondPlayer, return an integer array containing two values, the earliest possible round number and the latest possible round number in which these two players will compete against each other, respectively.
'''

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        @lru_cache(None)
        def dp(left, right, curPlayers, numGamesAlreadyPlayed):
            if left > right:  
                dp(right, left, curPlayers, numGamesAlreadyPlayed)
            if left == right: 
                ans.add(numGamesAlreadyPlayed)
            for i in range(1, left + 1):
                for j in range(left - i + 1, right - i + 1):
                    if not (curPlayers + 1) // 2 >= i + j >= left + right - curPlayers // 2: 
                        continue
                    dp(i, j, (curPlayers + 1) // 2, numGamesAlreadyPlayed + 1)

        ans = set()
        dp(firstPlayer, n - secondPlayer + 1, n, 1)
        return [min(ans), max(ans)]
      
-------------------------------------------------------------------------------------------------

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        firstPlayer, secondPlayer = firstPlayer-1, secondPlayer-1 # 0-indexed
        
        @cache
        def fn(k, mask): 
            """Return earliest and latest rounds."""
            can = deque()
            for i in range(n): 
                if mask & (1 << i): can.append(i)
                    
            cand = [] # eliminated player
            while len(can) > 1: 
                p1, p2 = can.popleft(), can.pop()
                if p1 == firstPlayer and p2 == secondPlayer or p1 == secondPlayer and p2 == firstPlayer: return [k, k] # game of interest 
                if p1 in (firstPlayer, secondPlayer): cand.append([p2]) # p2 eliminated 
                elif p2 in (firstPlayer, secondPlayer): cand.append([p1]) # p1 eliminated 
                else: cand.append([p1, p2]) # both could be elimited 
            
            minn, maxx = inf, -inf
            for x in product(*cand): 
                mask0 = mask
                for i in x: mask0 ^= 1 << i
                mn, mx = fn(k+1, mask0)
                minn = min(minn, mn)
                maxx = max(maxx, mx)
            return minn, maxx
        
        return fn(1, (1<<n)-1)
