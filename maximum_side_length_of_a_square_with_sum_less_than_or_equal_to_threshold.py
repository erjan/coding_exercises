'''
Given a m x n matrix mat and an integer threshold, return 
the maximum side-length of a square with a sum less than or equal to
threshold or return 0 if there is no such square.
'''

class Solution(object):
    def maxSideLength(self, mat, threshold):
        """
        :type mat: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        if not mat:
            return 0
        max_square = 0
        dp = [[0] * (len(mat[0]) + 1) for _ in range(len(mat) + 1)]
        for i in range(1, len(mat) + 1):
            for j in range(1, len(mat[0]) + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + mat[i - 1][j - 1]
                l = 1
                r = min(i, j)
                while l <= r:
                    k = (l + r) / 2
                    cur_sum = dp[i][j] - dp[i - k][j] - dp[i][j - k] + dp[i - k][j - k]
                    if cur_sum <= threshold:
                        max_square = max(max_square, k)
                        l = k + 1
                    else:
                        r = k - 1
        return max_square
      
---------------------------------------------------------------------------------------------------------------
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        t = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                t[i][j] = t[i][j-1] + t[i-1][j] - t[i-1][j-1] + mat[i-1][j-1]
        
        ans = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                start = 1
                end = min(i, j)
                while start <= end:
                    mid = (start+end) // 2
                    sums = t[i][j] - t[i-mid][j] - t[i][j-mid] + t[i-mid][j-mid]
                    if sums <= threshold:
                        ans = max(ans, mid)
                        start = mid+1
                    else:
                        end = mid-1
        
        return ans
