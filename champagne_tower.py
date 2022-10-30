'''
We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses, and so on until the 100th row.  Each glass holds one cup of champagne.

Then, some champagne is poured into the first glass at the top.  When the topmost glass is full, any excess liquid poured will fall equally to the glass immediately to the left and right of it.  When those glasses become full, any excess champagne will fall equally to the left and right of those glasses, and so on.  (A glass at the bottom row has its excess champagne fall on the floor.)

For example, after one cup of champagne is poured, the top most glass is full.  After two cups of champagne are poured, the two glasses on the second row are half full.  After three cups of champagne are poured, those two cups become full - there are 3 full glasses total now.  After four cups of champagne are poured, the third row has the middle glass half full, and the two outside glasses are a quarter full, as pictured below.
'''




'''
poured = 6, query_row = 3, query_glass = 1

row 0:                                                     1 (fills in 1, remains 5)
to next row:                             5/2=2.5                           5/2=2.5
row 1:                                   1(fills in 1, remains 1.5)      1(fills in 1, remains 1.5)
to next row:                   1.5/2=0.75                    1.5/2+1.5/2=1.5                          1.5/2=0.75 
row 3:                    0.75(fills in 0.75, remains 0)   1(fills in 1, remains 0.5)       0.75(fills in 0.75, remains 0) 
to next row:     0                                     0+0.5/2=0.25                   0+0.5/2=0.25                                   0
row 4:           0                                        0.25                              0.25                                     0
The Formula:
for query_glass = 0: poured[query_row][0] = (poured[query_row-1][0]-1)/2 if (poured[query_row-1][0]-1)>0 else 0
for query_glass = query_row-1: poured[query_row][query_glass] = (poured[query_glass][query_glass]-1)/2 if (poured[query_glass][query_glass]-1)>0 else 0
for others:
a1 = (poured[query_row-1][query_glass]-1)/2 if (poured[query_glass-1][query_glass]-1)>0 else 0
a2 = (poured[query_row-1][query_glass+1]-1)/2 if (poured[query_glass-1][query_glass+1]-1)>0 else 0
poured[query_row][query_glass] = a1 + a2
'''



class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        pyramid = {k-1:[0] * k for k in range(1, 101)}
        pyramid[0][0] = poured
        for row in range(1, query_row+1):
            T = True
            for c in range(row):
                val = (pyramid[row-1][c] - 1.0) / 2.0
                if val>0:
                    T = False
                    pyramid[row][c] += val
                    pyramid[row][c+1] += val
            if T:
                return min(1, pyramid[query_row][query_glass])
        return min(1, pyramid[query_row][query_glass])
      
      
-----------------------------------------------------------------------------------------------------------------------
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0 for _ in range(x)] for x in range(1, query_row + 2)]
        dp[0][0] = poured
        
        for i in range(query_row):
            for j in range(len(dp[i])):
                temp = (dp[i][j] - 1) / 2.0
                if temp>0:
                    dp[i+1][j] += temp
                    dp[i+1][j+1] += temp
        
        return dp[query_row][query_glass] if dp[query_row][query_glass] <= 1 else 1
