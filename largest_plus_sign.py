'''
You are given an integer n. You have an n x n binary grid grid with all values initially 1's except for some indices given in the array mines. The ith element of the array mines is defined as mines[i] = [xi, yi] where grid[xi][yi] == 0.

Return the order of the largest axis-aligned plus sign of 1's contained in grid. If there is none, return 0.

An axis-aligned plus sign of 1's of order k has some center grid[r][c] == 1 along with four arms of length k - 1 going up, down, left, and right, and made of 1's. Note that there could be 0's or 1's beyond the arms of the plus sign, only the relevant area of the plus sign is checked for 1's.
'''

Intuition
Brutal force will definitely fail given N can be up to 500 and brutal force is a O(N^3) solution; need to think of something else
For a + sign, there are 4 directions, up/down/left/right
If we just check 1 direction in each iteration, and store the value somewhere, then we can reuse the value since it's a matrix (we can have previous/next row or column's values).
So we check 4 directions separately, then the time complexity is O(N^2) * constant = O(N^2)
A + should have 4 directions same number of 1s
meaning we need to take the minimum of 4 directions
Finally, iterate over one more time to find the max
Explanation
class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        mat = [[1]*N for _ in range(N)]
        for x, y in mines: mat[x][y] = 0                   # create matrix with mine
            
        up = [[0]*N for _ in range(N)]                     # count 1s above mat[i][j] if mat[i][j] is 1
        for i in range(N):
            for j in range(N):
                if mat[i][j]: 
                    up[i][j] = 1
                    if i > 0: up[i][j] += up[i-1][j] 
                
        down = [[0]*N for _ in range(N)]                   # count 1s below mat[i][j] if mat[i][j] is 1
        for i in range(N-1, -1, -1):
            for j in range(N):
                if mat[i][j]: 
                    down[i][j] = 1
                    if i < N-1: down[i][j] += down[i+1][j] 
                    
        left = [[0]*N for _ in range(N)]                   # count 1s on the left side of mat[i][j] if mat[i][j] is 1
        for i in range(N):
            for j in range(N):
                if mat[i][j]:
                    left[i][j] = 1
                    if j > 0: left[i][j] += left[i][j-1]
                    
        right = [[0]*N for _ in range(N)]                  # count 1s on the right side of mat[i][j] if mat[i][j] is 1
        for i in range(N):
            for j in range(N-1, -1, -1):
                if mat[i][j]:
                    right[i][j] = 1
                    if j < N-1: right[i][j] += right[i][j+1]
         
		# find the largest + sign by using cached directions information
        return max(min([up[i][j], down[i][j], left[i][j], right[i][j]]) for i in range(N) for j in range(N))
    
    
--------------------------------------------------------------------------------------------------------------------------------
Just keep a check of nos of consecutive 1s in left and top in first loop
Right and down in second loop,and take min of all 4 directions,thats it !!!!

class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        m=len(mines)
        if m==n*n: return 0
        seen=set()
        for i,j in mines:
            seen.add((i,j))
        ans=1
        #(left,up,right,down)
        dp=[[[0,0,0,0] for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if (i,j) not in seen:
                    dp[i][j][0]=(dp[i][j-1][0]+1) if j-1>=0 else 1
                    dp[i][j][1]=(dp[i-1][j][1]+1) if i-1>=0 else 1
        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                if (i,j) not in seen:
                    dp[i][j][2]=(dp[i][j+1][2]+1) if j+1<n else 1
                    dp[i][j][3]=(dp[i+1][j][3]+1) if i+1<n else 1
                ans=max(ans,min(dp[i][j]))
        return ans
                    
    
