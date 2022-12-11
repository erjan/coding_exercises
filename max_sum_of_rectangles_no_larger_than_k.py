'''
Given an m x n matrix matrix and an integer k, return the max sum of a rectangle in the matrix such that its sum is no larger than k.

It is guaranteed that there will be a rectangle with a sum no larger than k.
'''

TLE

from typing import List

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])

        # Step #1:
        # - Time: O(m*n)
        # - Space: O(m*n)
        # Note: To simplify the logic (i.e. applying the same formula without corner cases), we add a top row and a left column of 0s; but it introduces an index offset of 1 compared to `matrix`
        rectangleSumsRow = [0] * (n + 1)
        rectangleSums = [rectangleSumsRow]
        for matrixRow in matrix:
            previousRectangleSumsRow, rectangleSumsRow, colIdx = rectangleSumsRow, [0], 0
            for value in matrixRow:
                colIdx += 1
                rectangleSum = value + rectangleSumsRow[colIdx - 1] + previousRectangleSumsRow[colIdx] - previousRectangleSumsRow[colIdx - 1]
                rectangleSumsRow.append(rectangleSum)
            rectangleSums.append(rectangleSumsRow)

        # Step #2:
        # - Time: O((m*n)^2)
        # - Space: O(1)
        res = -(2 ** 31)
        for startRowIdx in range(1, m + 1):
            for startColIdx in range(1, n + 1):
                for endRowIdx in range(startRowIdx, m + 1):
                    for endColIdx in range(startColIdx, n + 1):
                        subRectangleSum = (
                            rectangleSums[endRowIdx][endColIdx]
                            - rectangleSums[endRowIdx][startColIdx - 1]
                            - rectangleSums[startRowIdx - 1][endColIdx]
                            + rectangleSums[startRowIdx - 1][startColIdx - 1]
                        )
                        if subRectangleSum == k:
                            return k
                        elif res < subRectangleSum < k:
                            res = subRectangleSum

        return res
      
----------------------------------------------------------------------------------------------------
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        ans = float("-inf")
        m, n = len(matrix), len(matrix[0])
        for i in range(n):
            lstSum = [0] * m
            for j in range(i, n):
                currSum = 0
                curlstSum = [0]
                for t in range(m):
                    lstSum[t] += matrix[t][j]
                    currSum += lstSum[t]
                    pos = bisect_left(curlstSum, currSum - k)
                    if pos < len(curlstSum):
                        if curlstSum[pos] == currSum - k:
                            return k
                        else:
                            ans = max(ans, currSum - curlstSum[pos])
                    insort(curlstSum, currSum)
        return ans
---------------------------------------------------------------------------------------------------------------------
from sortedcontainers import SortedList

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0]) # dimensions 
        
        ans = -inf 
        rsum = [[0]*(n+1) for _ in range(m)] # row prefix sum 
        for j in range(n): 
            for i in range(m): rsum[i][j+1] = matrix[i][j] + rsum[i][j]
            for jj in range(j+1):
                prefix = 0 
                vals = SortedList()
                for i in range(m): 
                    vals.add(prefix)
                    prefix += rsum[i][j+1] - rsum[i][jj]
                    x = vals.bisect_left(prefix - k)
                    if x < len(vals): ans = max(ans, prefix - vals[x])
        return ans
