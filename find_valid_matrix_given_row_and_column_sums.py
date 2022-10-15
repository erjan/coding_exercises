'''
You are given two arrays rowSum and colSum of non-negative integers where rowSum[i] is the sum of the elements in the ith row and colSum[j] is the sum of the elements of the jth column of a 2D matrix. In other words, you do not know the elements of the matrix, but you do know the sums of each row and column.

Find any matrix of non-negative integers of size rowSum.length x colSum.length that satisfies the rowSum and colSum requirements.

Return a 2D array representing any matrix that fulfills the requirements. It's guaranteed that at least one matrix that fulfills the requirements exists.
'''

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n, m = len(rowSum), len(colSum)
        matrix = [[0] * m for i in range(n)]
        for i in range(n):
            for j in range(m):
                matrix[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= matrix[i][j]
                colSum[j] -= matrix[i][j]
        return matrix
      
-----------------------------------------------------------------

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n = len(rowSum)
        m = len(colSum)
        
        ans = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                val = min(rowSum[i], colSum[j])
                rowSum[i] -= val
                colSum[j] -= val
                ans[i][j] = val
        
        return ans
