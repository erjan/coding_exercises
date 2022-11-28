'''
You are given a 0-indexed m x n binary matrix grid.

A 0-indexed m x n difference matrix diff is created with the following procedure:

Let the number of ones in the ith row be onesRowi.
Let the number of ones in the jth column be onesColj.
Let the number of zeros in the ith row be zerosRowi.
Let the number of zeros in the jth column be zerosColj.
diff[i][j] = onesRowi + onesColj - zerosRowi - zerosColj
Return the difference matrix diff.

 
'''


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        R,C=len(grid),len(grid[0])
        onesR,onesC=[0]*R,[0]*C
        for r in range(R):
            for c in range(C):
                onesR[r]+=grid[r][c]
                onesC[c]+=grid[r][c]
        for r in range(R):
            for c in range(C):
                grid[r][c]=2*onesR[r] + 2*onesC[c] - R - C
        return grid    
