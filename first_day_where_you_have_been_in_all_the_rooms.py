'''
There are n rooms you need to visit, labeled from 0 to n - 1. Each day is labeled, starting from 0. You will go in and visit one room a day.

Initially on day 0, you visit room 0. The order you visit the rooms for the coming days is determined by the following rules and a given 0-indexed array nextVisit of length n:

Assuming that on a day, you visit room i,
if you have been in room i an odd number of times (including the current visit), on the next day you will visit a room with a lower or equal room number specified by nextVisit[i] where 0 <= nextVisit[i] <= i;
if you have been in room i an even number of times (including the current visit), on the next day you will visit room (i + 1) mod n.
Return the label of the first day where you have been in all the rooms. It can be shown that such a day exists. Since the answer may be very large, return it modulo 109 + 7.
'''

Fact, when you visit i, then other index less than i have already been visited even number of times. This is due to
if you have been in room i an odd number of times (including the current visit), on the next day you will visit a room with a lower or equal room number specified by nextVisit[i] where 0 <= nextVisit[i] <= i;

To reach i+1, you need visited i for an odd time, then even time + 1; say dp[i]: moves need to visited i
odd visit to i: dp[i]
back to nextVisit[i]: +1
from nextVisit[i] to i: dp[i] - dp[nextVisit[i]]
odd visit to i+1: +1
Now you have the transition function, see more explanation in below code comments
Implementation

class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        n = len(nextVisit)
        dp = [0] * n
        mod = int(1e9+7)
        for i in range(n-1):
            # dp[i]: moves need to visited `i`
            # dp[i] - dp[nextVisit[i]] + 1: odd visit at i, then back to nextVisited[i] (+1), then move back to i (dp[i] - dp[nextVisit[i]]) for even visit
            # dp[i] + 1: even visit at i, then from i to i+1
            dp[i+1] = (dp[i] - dp[nextVisit[i]] + 1 + dp[i] + 1) % mod
        return dp[n-1] 
