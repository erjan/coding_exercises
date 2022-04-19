'''
Given an m x n picture consisting of black 'B' and white 'W' pixels, return the number of black lonely pixels.

A black lonely pixel is a character 'B' that located at a specific position where the same row and same column don't have any other black pixels.

 

Example 1:


Input: picture = [["W","W","B"],["W","B","W"],["B","W","W"]]
Output: 3
Explanation: All the three 'B's are black lonely pixels.
Example 2:


Input: picture = [["B","B","B"],["B","B","W"],["B","B","B"]]
Output: 0
 

Constraints:

m == picture.length
n == picture[i].length
1 <= m, n <= 500
picture[i][j] is 'W' or 'B'.
'''

--------------------------------------------------------------
Go through the columns, count how many have exactly one black pixel and it's in a row that also has exactly one black pixel.

def findLonelyPixel(self, picture):
    return sum(col.count('B') == 1 == picture[col.index('B')].count('B') for col in zip(*picture))
    
----------------------------------------------------------------------------------



Union the row and column index, this way, points in same row or col must be grouped into the same group. Finally, groups that only contains one point will be the answer.

class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        n=len(picture)
        m=len(picture[0]) if n else 0
        uf={}
        def find(x):
            uf.setdefault(x,x)
            if uf[x]!=x:
                uf[x]=find(uf[x])
            return uf[x]
        def union(x,y):
            uf[find(x)]=uf[find(y)]
        for i in range(n):
            for j in range(m):
                if picture[i][j]=='B':
                    union(i,-(j+1))
        return list(collections.Counter(find(u) for u in uf).values()).count(2)
Row scanning way:
Scan row one by one, if find any 'B', then search its column, if only one 'B' in the column, then this 'B' might be the candidate. Keep scanning this row, if find no other 'B', then this 'B' is one result. This way only takes O(1) memory.

class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        n,m=len(picture),len(picture[0])
        res=0
        for j in range(m):
            found=False
            for i in range(n):
                if picture[i][j]=='B':
                    if found or picture[i].count('B')!=1:
                        found=False
                        break
                    found=True
            if found:
                res+=1
        return res
        
----------------------------------------------------------------------

class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        rows = [sum(c == 'B' for c in r) for r in picture]
        cols = [sum(c == 'B' for c in c) for c in zip(*picture)]
        return sum(picture[i][j] == 'B' and rows[i] == 1 and cols[j] == 1 for i in range(len(picture)) for j in range(len(picture[i])))
        
--------------------------------------------------------------------------------

row: set of column indices, where there exists at least 1 row that has only 1 B pixel at column i
col[i]: total number of B at column i
A valid lonely pixel is when col[i] == 1 (meaning only 1 row at ith column has B pixel) and i exists in row (meaning picture[r][i] is the only B pixel for some row r).
class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        m, n = len(picture), len(picture[0])
        col = [0] * n
        row = set()
        for i in range(m):
            cnt = 0
            for j in range(n):
                if picture[i][j] == 'B':
                    c = j
                    cnt += 1
                    col[j] += 1
            if cnt == 1: row.add(c)
        ans = 0        
        for i, c in enumerate(col):
            if c == 1 and i in row:
                ans += 1
        return ans       
-------------------------------------------------------------------------------------------------

        if not picture:
            return 0
        
        count = 0
        for row in picture:
            if row.count('B') == 1:  # if each row has lonely 'B'
                count += 1
        
        for col in zip(*picture):
            if col.count('B') > 1: # if coulmn has some 'B' not alone
                count -= col.count('B') # remove them from count
        
        return count if count > 0 else 0
        
        
        
        
    
