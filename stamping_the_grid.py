'''
You are given an m x n binary matrix grid where each cell is either 0 (empty) or 1 (occupied).

You are then given stamps of size stampHeight x stampWidth. We want to fit the stamps such that they follow the given restrictions and requirements:

Cover all the empty cells.
Do not cover any of the occupied cells.
We can put as many stamps as we want.
Stamps can overlap with each other.
Stamps are not allowed to be rotated.
Stamps must stay completely inside the grid.
Return true if it is possible to fit the stamps while following the given restrictions and requirements. Otherwise, return false.
'''


class Solution(object):
    def possibleToStamp(self, G, H, W):
        m, n = len(G), len(G[0])

        # S[i][j] represents the sum of the rectangle from (0, 0) to (i - 1, j - 1) inclusively.
        S = [[0] * (n + 1) for i in range(m + 1)]
        for i in range(m):
            for j in range(n):
                S[i + 1][j + 1] = S[i][j + 1] + S[i + 1][j] - S[i][j] + G[i][j]

        # stamp[i][j] represents that weather a stamp can be put with the upper left position (i, j)
        # if and only if the sum of rectangle from (i, j) to (i + H - 1, j + H - 1) inclusively equals to 0
        stamp = [[False] * n for _ in G]
        for i in range(m - H + 1):
            for j in range(n - W + 1):
                ii, jj = i + H, j + W
                stamp[i][j] = S[i][j] + S[ii][jj] - S[i][jj] - S[ii][j] == 0

        for i in range(m):
            for j in range(n):
                # traverse each position (i, j) of grid, if it is 0, find out a stamp upper left position (ii, jj)
                # if not found, it cannot cover, so return False immediately
                # if found, modify every position that the stamp (ii, jj) can cover to 1 to skip them later
                # this trick seems inconspicuous, but it is very important
                if G[i][j] == 0:
                    flag = False
                    for ii in range(i, max(-1, i - H), -1):
                        if flag: break
                        for jj in range(j, max(-1, j - W), -1):
                            if stamp[ii][jj]:
                                for s in range(ii, ii + H):
                                    for t in range(jj, jj + W):
                                        G[s][t] = 1  # skip them later
                                flag = True
                                break
                    if not flag: return False
        return True
    
-------------------------------------------------------------------------------------------------------------------------------
    def possibleToStamp(self, M, h, w):
        m, n = len(M), len(M[0])
        A = [[0] * (n + 1) for _ in range(m + 1)]
        good = [[0] * n for _ in range(m)]
        for i in xrange(m):
            for j in xrange(n):
                A[i + 1][j + 1] = A[i + 1][j] + A[i][j + 1] - A[i][j] + (1 - M[i][j])
                if i + 1 >= h and j + 1 >= w:
                    x, y = i + 1 - h, j + 1 -w
                    if A[i + 1][j + 1] - A[x][j + 1] - A[i + 1][y] + A[x][y] == w * h:
                        good[i][j] += 1
        B = [[0] * (n + 1) for _ in range(m + 1)]
        for i in xrange(m):
            for j in xrange(n):
                B[i + 1][j + 1] = B[i + 1][j] + B[i][j + 1] - B[i][j] + good[i][j]
        for i in xrange(m):
            for j in xrange(n):
                x, y = min(i + h, m), min(j + w, n)
                if M[i][j] == 0 and B[x][y] - B[i][y] - B[x][j] + B[i][j] == 0:
                    return False
        return True
