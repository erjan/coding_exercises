'''
You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:

answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.

Note:

You should only consider the players that have played at least one match.
The testcases will be generated such that no two matches will have the same outcome.
'''


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        
        winners = defaultdict(list)
        losers = defaultdict(list)

        for w, l in matches:
            winners[w].append(l)
            losers[l].append(w)

        for l in losers:
            losers[l] = len(losers[l])

        for w in winners:
            winners[w] = len(winners[w])


        onematch = list()
        for k, v in losers.items():
            if v == 1:
                onematch.append(k)

        onematch.sort()

        noloss = list()
        for k, v in winners.items():
            if k not in losers.keys():
                noloss.append(k)
        print(noloss)

        noloss.sort()

        res = list((noloss, onematch))
        print(res)
        return res
      
----------------------------------------
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners, losers, table = [], [], {}
        for winner, loser in matches:
            # map[key] = map.get(key, 0) + change . This format ensures that KEY NOT FOUND error is always prevented.
            # map.get(key, 0) returns map[key] if key exists and 0 if it does not.
            table[winner] = table.get(winner, 0)  # Winner
            table[loser] = table.get(loser, 0) + 1
        for k, v in table.items(): # Player k with losses v
            if v == 0:
                winners.append(k) # If player k has no loss ie v == 0
            if v == 1:
                losers.append(k) # If player k has one loss ie v == 1
        return [sorted(winners), sorted(losers)] # Problem asked to return sorted arrays.
      
--------------------------------------------------------
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        indegree = defaultdict(int) # To count the number of matches a player have lost
        players = set() #To hold the players who have played a match
        for match in matches:
            indegree[match[1]] += 1
            players.add(match[0])
            players.add(match[1])
            
        ans = [[], []]
        for i in players:
            if indegree[i] == 0:
                ans[0].append(i)
            if indegree[i] == 1:
                ans[1].append(i)
            
        return [sorted(ans[0]), sorted(ans[1])]




