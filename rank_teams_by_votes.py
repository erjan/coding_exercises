'''
In a special ranking system, each voter gives a rank from highest to lowest to all teams participated in the competition.

The ordering of teams is decided by who received the most position-one votes. If two or more teams tie in the first position, we consider the second position to resolve the conflict, if they tie again, we continue this process until the ties are resolved. If two or more teams are still tied after considering all positions, we rank them alphabetically based on their team letter.

Given an array of strings votes which is the votes of all voters in the ranking systems. Sort all teams according to the ranking system described above.

Return a string of all teams sorted by the ranking system.
'''

class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        voteslen, wordlen = len(votes), len(votes[0])
        votes_by_team = dict()
        for i in range(wordlen):
            votes_by_team[votes[0][i]] = [0] * wordlen
        for pos in range(wordlen):
            for vote in range(voteslen):
                votes_by_team[votes[vote][pos]][pos] -= 1
        list_to_cmp = [ v + [k] for k, v in votes_by_team.items() ]
        list_to_cmp.sort()
        return ''.join([x[-1] for x in list_to_cmp])
      
----------------------------------------------------------------------
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
	# dict init
        d = {}
        for sym in votes[0]:
            d[sym] = [len(votes) for _ in range(len(votes[0]))]
	# dict filling
        for vote in votes:
            for sym in vote:
                d[sym][vote.index(sym)] -= 1
	# sorting
        sort_votes = sorted(d.items(), key=lambda x: (x[1], x[0]))
		
        return "".join(vote[0] for vote in sort_votes)
