'''
In the world of Dota2, there are two parties: the Radiant and the Dire.

The Dota2 senate consists of senators coming from two parties. Now the Senate wants to decide on a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise one of the two rights:

Ban one senator's right: A senator can make another senator lose all his rights in this and all the following rounds.
Announce the victory: If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and decide on the change in the game.
Given a string senate representing each senator's party belonging. The character 'R' and 'D' represent the Radiant party and the Dire party. Then if there are n senators, the size of the given string will be n.

The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.

Suppose every senator is smart enough and will play the best strategy for his own party. Predict which party will finally announce the victory and change the Dota2 game. The output should be "Radiant" or "Dire".
'''

Explanation
If there is a chance to ban the opponent, do it (greedy). Repeat this process until only R or D left in senate.
To ban someone, we start up 2 counters
ban_d: chances to ban D
ban_r: chances to bna R
You may wonder, what if someone want to ban person before him?
If we travel back, that will cause extra time and mess things up
But don't worries, if opponent is before you, it will get banned next round. e.g.
Round 0: RRDDDD
Round 1: RRXXDD first 2 Ds were banned by first 2 Rs, but last 2 D can still have 2 chances to ban R
Round 2: XXXXDD since we hold 2 chances to ban R, they will be banned at this round, so they won't have chance to ban D again.
banned: A list to check if current person is banned, if True skip this person
s: A set to check if everyone in the senate are same side
Implementation
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        s, banned = set(), [False] * n
        ban_d = ban_r = 0
        while len(s) != 1:
            s = set()
            for i, p in enumerate(senate):
                if banned[i]: continue
                if p == 'R':
                    if ban_r > 0:           # current R being banned
                        ban_r -= 1
                        banned[i] = True
                    else:                   # if current R is valid, it will ban D
                        ban_d += 1
                        s.add('R')
                else:        
                    if ban_d > 0:           # current D being banned
                        ban_d -= 1
                        banned[i] = True
                    else:                   # if current D is valid, it will ban R
                        ban_r += 1
                        s.add('D')
        return 'Radiant' if s.pop() == 'R' else 'Dire'
      
----------------------------------------------------
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R_idx = deque([i for i in range(len(senate)) if senate[i]=='R'])
        D_idx = deque([j for j in range(len(senate)) if senate[j]=='D'])
        n = len(senate)
        while R_idx and D_idx:
            r = R_idx.popleft()
            d = D_idx.popleft()
            if r < d:
                R_idx.append(n + r)
            else:
                D_idx.append(n + d)
        return 'Radiant' if R_idx else 'Dire'
      
------------------------------------------------------------------------------------------------
class Solution:
	def predictPartyVictory(self, s: str) -> str:
		qd = deque([i for i in range(len(s)) if s[i]=='D'])        
		qr = deque([i for i in range(len(s)) if s[i]=='R'])
		while qr and qd:
			r,d = qr.popleft(), qd.popleft()
			if r<d: qr.append(r+len(s))
			else: qd.append(d+len(s))

		return 'Dire' if qd else 'Radiant'
