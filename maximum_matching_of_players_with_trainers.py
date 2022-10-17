'''
You are given a 0-indexed integer array players, where players[i] represents the ability of the ith player. You are also given a 0-indexed integer array trainers, where trainers[j] represents the training capacity of the jth trainer.

The ith player can match with the jth trainer if the player's ability is less than or equal to the trainer's training capacity. Additionally, the ith player can be matched with at most one trainer, and the jth trainer can be matched with at most one player.

Return the maximum number of matchings between players and trainers that satisfy these conditions
'''

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        
        
        players.sort()
        trainers.sort()
        
        
        i = 0
        j = 0
        res = 0
        
        while i < len(players) and j < len(trainers):
            
   
            if players[i] <= trainers[j]:
                res+=1
                i+=1
                j+=1
            else:
                j+=1
            
            
        return res
      
-------------------------------------------------------------------
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        ans = 0
        trainers.sort()
        heapify(players)

        for t in trainers:
            if players and players[0] <= t:
                heappop(players)
                ans+= 1

        return ans
      
-------------------------------------------------------------------------------------------------
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        result = 0
        for i in range(len(players)):
            if len(players)==0 or len(trainers)==0:
                break;
            if players[-1]<=trainers[-1]:
                players.pop()
                trainers.pop()
                result+=1
            else:
                players.pop()
        return result
