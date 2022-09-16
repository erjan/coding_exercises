'''
You are given an m x n integer matrix grid​​​.

A rhombus sum is the sum of the elements that form the border of a regular rhombus shape in grid​​​. The rhombus must have the shape of a square rotated 45 degrees with each of the corners centered in a grid cell. Below is an image of four valid rhombus shapes with the corresponding colored cells that should be included in each rhombus sum:
'''

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        dp = [[[0, 0]] * (n+2) for _ in range(m+2)]
        ans = []
        for i in range(1, m+1):
            for j in range(1, n+1):                            # [i, j] will be the bottom vertex
                ans.append(grid[i-1][j-1])
                dp[i][j] = [grid[i-1][j-1], grid[i-1][j-1]]
                dp[i][j][0] += dp[i-1][j-1][0]                 # dp: major diagonal
                dp[i][j][1] += dp[i-1][j+1][1]                 # dp: minor diagonal
                for win in range(1, min(m, n)):
                    x1, y1 = i-win, j-win                      # left vertex
                    x2, y2 = i-win, j+win                      # right vertex
                    x3, y3 = i-win-win, j                      # top vertex
                    if not (all(1 <= x < m+1 for x in [x1, x2, x3]) and all(1 <= y < n+1 for y in [y1, y2, y3])):
                        break
                    b2l = dp[i][j][0] - dp[x1-1][y1-1][0]      # bottom node to left node (node sum), major diagonal
                    b2r = dp[i][j][1] - dp[x2-1][y2+1][1]      # bottom node to right node (node sum), minor diagonal
                    l2t = dp[x1][y1][1] - dp[x3-1][y3+1][1]    # left node to top node (node sum), minor diagonal
                    r2t = dp[x2][y2][0] - dp[x3-1][y3-1][0]    # right node to top node (node sum), major diagonal
                    vertices_sum = grid[i-1][j-1] + grid[x1-1][y1-1] + grid[x2-1][y2-1] + grid[x3-1][y3-1]
                    cur = b2l + b2r + l2t + r2t - vertices_sum # sum(edges) - sum(4 vertices)
                    ans.append(cur)
        return sorted(set(ans), reverse=True)[:3]              # unique + sort reverse + keep only first 3        
      
------------------------------------------------------------------------------------------------------------
class Solution:
def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
    
    def calc(l,r,u,d):
        sc=0
        c1=c2=(l+r)//2
        expand=True
        for row in range(u,d+1):
            if c1==c2:
                sc+=grid[row][c1]
            else:
                sc+=grid[row][c1]+grid[row][c2]
            
            if c1==l:
                expand=False
            
            if expand:
                c1-=1
                c2+=1
            else:
                c1+=1
                c2-=1
        return sc
        
    
    m=len(grid)
    n=len(grid[0])
    heap=[]
    for i in range(m):
        for j in range(n):
            l=r=j
            d=i
            while l>=0 and r<=n-1 and d<=m-1:
                sc=calc(l,r,i,d)
                l-=1
                r+=1
                d+=2
                if len(heap)<3:
                    if sc not in heap:
                        heapq.heappush(heap,sc)
                else:
                    if sc not in heap and sc>heap[0]:
                        heapq.heappop(heap)
                        heapq.heappush(heap,sc)
    
    heap.sort(reverse=True)
    return heap
