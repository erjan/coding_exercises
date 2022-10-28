'''
You are given an m x n integer matrix points (0-indexed). Starting with 0 points, you want to maximize the number of points you can get from the matrix.

To gain points, you must pick one cell in each row. Picking the cell at coordinates (r, c) will add points[r][c] to your score.

However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), picking cells at coordinates (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.

Return the maximum number of points you can achieve.

abs(x) is defined as:

x for x >= 0.
-x for x < 0.
 
 '''

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        M, N = len(points), len(points[0])
        left = [0] * N
        right = [0] * N
        dp = points[0]
        for i in range(1, M):
            # process from left to right
            for j in range(N):
                if j == 0:
                    left[0] = dp[0]
                else:
                    left[j] = max(dp[j], left[j-1]-1)
            # process from right to left
            for j in range(N-1,-1,-1):
                if j == N-1:
                    right[N-1] = dp[N-1]
                else:
                    right[j] = max(dp[j], right[j+1]-1)
            # set the new max points at each column based on the max of going
            # left to right vs right to left
            for j in range(N):
                dp[j] = points[i][j] + max(left[j], right[j])
        return max(dp)
      
-----------------------------------------------------------------------------------------------------------
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        current_points = [point for point in points[0]]
        
        for row in range(1, len(points)):
            # We traverse current_points left to right and store the maximum possible score that the next row can get,
            # taking into account only the elements with indexes [0, col]
            max_col_points = -float("inf")
            for col in range(0, len(current_points)):
                max_col_points = max(max_col_points - 1, current_points[col])
                current_points[col] = max_col_points
                
            # We traverse current_points right to left and store the maximum possible score that the next row can get,
            # taking into account only the elements with indexes [col, end]
            max_col_points = -float("inf")
            for col in range(len(current_points) - 1, -1, -1):
                max_col_points = max(max_col_points - 1, current_points[col])
                current_points[col] = max_col_points
                
            # We update current_points, adding the maximum value we can carry over from the previous row to the value
            # contained in the current column of the current row
            for col in range(len(current_points)):
                current_points[col] = points[row][col] + current_points[col]
                
        return max(current_points)
