'''
Given a m x n matrix mat and an integer k, return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for:

i - k <= r <= i + k,
j - k <= c <= j + k, and
(r, c) is a valid position in the matrix.
'''
------------------------------------------------------------------------------------------

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        dp = [[mat[i][j] for j in range(m)] for i in range(n)]

        # Prefix Sums Left to Right
        for i in range(n):
            for j in range(m):
                dp[i][j] += (dp[i][j-1] if j > 0 else 0)
        
        # Prefix Sums of Sums Top to Bottom
        for j in range(m):
            for i in range(n):
                dp[i][j] += (dp[i-1][j] if i > 0 else 0)
                        
        # Update input Mat with sum per cell
        for i in range(n):
            for j in range(m):
                x1, x2 = max(0, j-k), min(j+k, m-1)
                y1, y2 = max(0, i-k), min(i+k, n-1)
                dy = dp[y1-1][x2] if y1 > 0 else 0
                dx = dp[y2][x1-1] if x1 > 0 else 0
                dz = dp[y1-1][x1-1] if (x1 > 0 and y1 > 0) else 0
                mat[i][j] = dp[y2][x2] - dy - dx + dz

        return mat
----------------------------------------------------------------------------------------------------------
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
		
		# Calculate the prefix sum
        prefix = mat[:][:]  # essentially copies the entire array
        for i in range(m):
            for j in range(n):
                prefix[i][j] += (prefix[i-1][j] if i > 0 else 0) + \          # add prefix sum of (i-1, j) if it exists
                                (prefix[i][j-1] if j > 0 else 0) - \          # add prefix sum of (i, j-1) if it exists
                                (prefix[i-1][j-1] if i > 0 and j > 0 else 0)  # subtract prefix sum of (i-1, j-1) if it exists
		
		# Calculate the block sum from the prefix sum
        result = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                result[i][j] = prefix[min(i+k, m-1)][min(j+k, n-1)] + \                  # S(D), bounded by m x n
                               (prefix[i-k-1][j-k-1] if i-k > 0 and j-k > 0 else 0) - \  # S(A), if it exists
                               (prefix[i-k-1][min(j+k, n-1)] if i-k > 0 else 0) - \      # S(B), if it exists
                               (prefix[min(i+k, m-1)][j-k-1] if j-k > 0 else 0)          # S(C), if it exists
        return result
		# we could technically shorten the block sum calculation into one line of code, but that is super unreadable
------------------------------------------------
fmax     = lambda x,y: x if x>y else y # 33% Faster than Python's Built-in MAX Function
fmin     = lambda x,y: x if x<y else y # Idem for MIN Function
inizero  = lambda r,c: [[0]*c for _ in range(r)]
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        r,c = len(mat), len(mat[0])
        #
        # -----------------------------------
        #         Range Sums Up to [i,j]
        # -----------------------------------
        #
        Sum    = inizero(r,c)
        #
        # First Row Initilization
        s = 0
        for j in range(c):
            s        += mat[0][j]
            Sum[0][j] = s
        #
        # First Column Initilization
        s = 0
        for i in range(r):
            s        += mat[i][0]
            Sum[i][0] = s
        #
        # Center Range
        for i in range(1,r):
            for j in range(1,c):
                Sum[i][j] = mat[i][j] + Sum[i-1][j] + Sum[i][j-1] - Sum[i-1][j-1]
        #
        # -----------------------------------
        #         Final Answer
        # -----------------------------------
        res = inizero(r,c)
        for i in range(r):
            for j in range(c):
                i1,j1 = fmax(0  ,i-K),fmax(0  ,j-K)
                i2,j2 = fmin(r-1,i+K),fmin(c-1,j+K)
                #
                a = Sum[i2][j2]
                if i1>0:
                    a -= Sum[i1-1][j2]
                    if j1>0:
                        a += Sum[i1-1][j1-1] # This was being subtracted twice
                if j1>0:
                    a -= Sum[i2][j1-1]
                res[i][j] = a
        #
        return res
      
