'''
There is a 2D grid of size n x n where each cell of this grid has a lamp that is initially turned off.

You are given a 2D array of lamp positions lamps, where lamps[i] = [rowi, coli] indicates that the lamp at grid[rowi][coli] is turned on. Even if the same lamp is listed more than once, it is turned on.

When a lamp is turned on, it illuminates its cell and all other cells in the same row, column, or diagonal.

You are also given another 2D array queries, where queries[j] = [rowj, colj]. For the jth query, determine whether grid[rowj][colj] is illuminated or not. After answering the jth query, turn off the lamp at grid[rowj][colj] and its 8 adjacent lamps if they exist. A lamp is adjacent if its cell shares either a side or corner with grid[rowj][colj].

Return an array of integers ans, where ans[j] should be 1 if the cell in the jth query was illuminated, or 0 if the lamp was not.
'''

class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        lamps = {(r, c) for r, c in lamps}
        
        row, col, left, right = dict(), dict(), dict(), dict()
        for r, c in lamps:
            row[r] = row.get(r, 0) + 1
            col[c] = col.get(c, 0) + 1
            left[r - c] = left.get(r - c, 0) + 1
            right[r + c] = right.get(r + c, 0) + 1

        res = list()
        for qr, qc in queries:
            if row.get(qr, 0) or col.get(qc, 0) or left.get(qr - qc, 0) or right.get(qr + qc, 0):
                res.append(1)
            else:
                res.append(0)

            for r, c in product(range(qr - 1, qr + 2), range(qc - 1, qc + 2)):
                if (r, c) in lamps:
                    lamps.remove((r, c))
                    row[r] -= 1
                    col[c] -= 1
                    left[r - c] -= 1
                    right[r + c] -= 1

        return res
      
      
