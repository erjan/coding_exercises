'''
You are given four integers row, cols, rCenter, and cCenter. There is a rows x cols matrix and you are on the cell with the coordinates (rCenter, cCenter).

Return the coordinates of all cells in the matrix, sorted by their distance from (rCenter, cCenter) from the smallest distance to the largest distance. You may return the answer in any order that satisfies this condition.

The distance between two cells (r1, c1) and (r2, c2) is |r1 - r2| + |c1 - c2|.
'''

class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        res = list()
        rc = rCenter
        cc = cCenter
        
        for i in range(rows):

            for j in range(cols):

                temp = [i, j, abs(i - rc) + abs(j - cc)]
                res.append(temp)

        res.sort(key=lambda x: x[2])

        for i in range(len(res)):

            cur = res[i]

            res[i] = [cur[0], cur[1] ]

        print(res)

        return res 
