'''
Design a Leaderboard class, which has 3 functions:

addScore(playerId, score): Update the leaderboard by adding score to the given player's score. If there is no player with such id in the leaderboard, add him to the leaderboard with the given score.
top(K): Return the score sum of the top K players.
reset(playerId): Reset the score of the player with the given id to 0 (in other words erase it from the leaderboard). It is guaranteed that the player was added to the leaderboard before calling this function.
Initially, the leaderboard is empty.
'''


class Leaderboard:

    def __init__(self):
        self.leaderboard = dict()
        

    def addScore(self, playerId: int, score: int) -> None:
        
        if playerId not in self.leaderboard:
            self.leaderboard[playerId] = score
        else:
            self.leaderboard[playerId] += score
        

    def top(self, K):
      
      val = list(self.leaderboard.values())
      val.sort(reverse=True)
      print('values are ', val)
      # topk = first k elements

      res = val[:K]
      print(res)

      res = sum(res)
      print('sum is', res)
      return res

    def top(self, K: int) -> int:
        
        values =  [v for _,v in sorted(self.leaderboard.items(), key = lambda item: item[1]) ]
        values.sort(reverse=True)
        
        res = 0
        i = 0
        while i < K:
            res+= values[i]
            i+=1
        return res

    def reset(self, playerId: int) -> None:
        self.leaderboard[playerId] = 0

        


------------------------------------------------------------------------
#using heap


'''
O(1) for addScore.
O(1)O(1) for reset.
O(K) + O(N \text{log}K)O(K)+O(NlogK) = O(N \text{log}K)O(NlogK). It takes O(K)O(K) to construct the initial heap and then for the rest of the N-KN−K elements, we perform the extractMin and add operations on the heap each of which take (\text{log}K)(logK) time.
Space Complexity:

O(N + K)O(N+K) where O(N)O(N) is used by the scores dictionary and O(K)O(K) is used by the heap.
'''

class Leaderboard:

    def __init__(self):
        self.scores = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.scores:
            self.scores[playerId] = 0
        self.scores[playerId] += score

    def top(self, K: int) -> int:
    
        # This is a min-heap by default in Python.
        heap = []
        for x in self.scores.values():
            heapq.heappush(heap, x)
            if len(heap) > K:
                heapq.heappop(heap)
        res = 0
        while heap:
            res += heapq.heappop(heap)
        return res

    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0
        
        
-------------------------------------------------------
from sortedcontainers import SortedDict

class Leaderboard:

    def __init__(self):
        self.scores = {}
        self.sortedScores = SortedDict()

    def addScore(self, playerId: int, score: int) -> None:

        # The scores dictionary simply contains the mapping from the
        # playerId to their score. The sortedScores contain a BST with 
        # key as the score and value as the number of players that have
        # that score.     
        if playerId not in self.scores:
            self.scores[playerId] = score
            self.sortedScores[-score] = self.sortedScores.get(-score, 0) + 1
        else:
            preScore = self.scores[playerId]
            val = self.sortedScores.get(-preScore)
            if val == 1:
                del self.sortedScores[-preScore]
            else:
                self.sortedScores[-preScore] = val - 1    
            
            newScore = preScore + score;
            self.scores[playerId] = newScore
            self.sortedScores[-newScore] = self.sortedScores.get(-newScore, 0) + 1
        
    def top(self, K: int) -> int:
        count, total = 0, 0;

        for key, value in self.sortedScores.items():
            times = self.sortedScores.get(key)
            for _ in range(times): 
                total += -key;
                count += 1;
                
                # Found top-K scores, break.
                if count == K:
                    break;
                
            # Found top-K scores, break.
            if count == K:
                break;
        
        return total;

    def reset(self, playerId: int) -> None:
        preScore = self.scores[playerId]
        if self.sortedScores[-preScore] == 1:
            del self.sortedScores[-preScore]
        else:
            self.sortedScores[-preScore] -= 1
        del self.scores[playerId];
