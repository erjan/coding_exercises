'''
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
'''

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # 1 0 1 2 3        
        # 0 1 0 1 0       
        # 1 2 0 1 2
        # 1 2 0 1 2
        # 0 1 2 3 4

        M, N = len(matrix), len(matrix[0])
        dp = [[0] * N for _  in range(M)]

        for i in range(M):
            dp[i][0] = 1 if matrix[i][0] == '1' else 0
        
        for i in range(M):
            for j in range(1, N):
                if matrix[i][j] == '1':
                    if dp[i][j - 1]:
                        dp[i][j] = dp[i][j - 1] + 1
                    else:
                        dp[i][j] = 1
        
        ret = 0
        for j in range(N):
            column = []
            for i in range(M):
                column.append(dp[i][j])
            
            for p in range(len(column)):
                left = right = p
                val = column[p]

                cnt = 1
                while left >= 0 and column[left] >= val:
                    if left != p:
                        cnt += 1
                    left -= 1
                
                while right < len(column) and column[right] >= val:
                    if right != p:
                        cnt += 1
                    right += 1
                
                ret = max(ret, val * cnt)
                        
        return ret
--------------------------------------------------------------------------------------------
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        ans = 0
        row = [0]*len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    row[j] += 1
                else:
                    row[j] = 0
            ans = max(ans, self.largestRectangleArea(row))
        return ans
    
	###### 84. Largest Rectangle in Histogram ###### 
    def largestRectangleArea(self, heights):
        n = len(heights)
        left = [-1] * n
        right = [n] * n
        
        # populate left and right
        stack = []
        for i,h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                pop = stack.pop()
                right[pop] = i
            stack.append(i)
        
        stack = []
        for i in range(n-1,-1,-1):
            while stack and heights[i] < heights[stack[-1]]:
                pop = stack.pop()
                left[pop] = i
            stack.append(i)
            
        # calculate ans
        area = 0
        for i,h in enumerate(heights):
            width = right[i] - left[i] - 1
            area = max(area, width * h)
        return area






      
