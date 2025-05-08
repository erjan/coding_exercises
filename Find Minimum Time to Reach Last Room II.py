'''
There is a dungeon with n x m rooms arranged as a grid.

You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time in seconds when you can start moving to that room. You start from the room (0, 0) at time t = 0 and can move to an adjacent room. Moving between adjacent rooms takes one second for one move and two seconds for the next, alternating between the two.

Return the minimum time to reach the room (n - 1, m - 1).

Two rooms are adjacent if they share a common wall, either horizontally or vertically.
'''

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        R, C = len(moveTime), len(moveTime[0])

        def isOutside(i, j):
            return i < 0 or i >= R or j < 0 or j >= C

        def idx(i, j):
            return i * C + j

        N = R * C
        time = [2**31] * N
        pq = [(0, 0, 1)] # (time, ij, adjust)

        time[0] = 0
        while len(pq):
            t, ij, adj = heappop(pq)
            i, j = divmod(ij, C)
            if i == R - 1 and j == C - 1:
                return t

            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                r, s = i + di, j + dj
                if isOutside(r, s):
                    continue

                nextTime=max(t, moveTime[r][s])+1+(1-adj)

                rs = idx(r, s)
                if nextTime < time[rs]:
                    time[rs] = nextTime
                    heappush(pq, (nextTime, rs, 1-adj))
        return -1
