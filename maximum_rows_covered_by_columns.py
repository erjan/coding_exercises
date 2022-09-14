'''
You are given a 0-indexed m x n binary matrix matrix and an integer numSelect, which denotes the number of distinct columns you must select from matrix.

Let us consider s = {c1, c2, ...., cnumSelect} as the set of columns selected by you. A row row is covered by s if:

For each cell matrix[row][col] (0 <= col <= n - 1) where matrix[row][col] == 1, col is present in s or,
No cell in row has a value of 1.
You need to choose numSelect columns such that the number of rows that are covered is maximized.

Return the maximum number of rows that can be covered by a set of numSelect columns.
'''

class Solution:
    def maximumRows(self, mat: List[List[int]], cols: int) -> int:
        m, n = len(mat), len(mat[0])
        maxRows = 0
        
        colToChoose = list(combinations(list(range(n)), cols))
        
        for col in colToChoose:
            col = set(col)
            rowHidden = 0
            for row in mat:
                canHide = True
                for i in range(n):
                    if(row[i] and i not in col):
                        canHide = False
                        break
                if(canHide):
                    rowHidden += 1
            maxRows = max(maxRows, rowHidden)
        return maxRows
      
-------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def maximumRows(self, mat: List[List[int]], cols: int) -> int:
        n,m = len(mat),len(mat[0])
        ans = 0

        def check(state,row,rowIncludedCount):
            nonlocal ans
            if row==n:
                if sum(state)<=cols:
                    ans = max(ans,rowIncludedCount)
                return
            
            check(state[::],row+1,rowIncludedCount)
            for j in range(m):
                if mat[row][j]==1:
                    state[j] = 1
            check(state,row+1,rowIncludedCount+1)
        
        check([0]*m,0,0)
        return ans
