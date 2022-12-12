'''
There are n people and 40 types of hats labeled from 1 to 40.

Given a 2D integer array hats, where hats[i] is a list of all hats preferred by the ith person.

Return the number of ways that the n people wear different hats to each other.

Since the answer may be too large, return it modulo 109 + 7
'''

class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        N = len(hats) # number of people
        h2p = collections.defaultdict(list) # hat -> people
        for person in range(N):
            for hat in hats[person]:
                h2p[hat].append(person)
                
        if len(h2p) < N: # when the number of hats < the number of people
            return 0
        
		# For each hat, dp stores the status of the people has been matched by a hat.
        # e.g. 0b0000000000 means no one wears a hat
        # 0b0010000000 means only person No.2 wears a hat
        # There are totally 2 ^ N different possible status.
        MASK = [1 << p for p in range(N)]
        dp = [[0] * (2 ** N) for _ in range(len(h2p) + 1)]
        dp[0][0] = 1
        
        i, MOD = 1, 1000000007
        while h2p: # O(H)
            _, people = h2p.popitem()
            for j, n in enumerate(dp[i - 1]): #O(2^P)
                if not n:
                    continue
                
                dp[i][j] += n # when mask = 0
                for p in people: #O(P)
                    if not (MASK[p] & j):
                        dp[i][MASK[p] + j] += n
            i += 1
        
        return dp[-1][-1] % MOD
