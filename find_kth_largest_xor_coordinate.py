'''
You are given a 2D matrix of size m x n, consisting of non-negative integers. You are also given an integer k.

The value of coordinate (a, b) of the matrix is the XOR of all matrix[i][j] where 0 <= i <= a < m and 0 <= j <= b < n (0-indexed).

Find the kth largest value (1-indexed) of all the coordinates of matrix.
'''

class Solution:
  def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
    
    q = [matrix[0][0]]
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == j == 0:
                continue
            elif i == 0:
                matrix[i][j] ^= matrix[i][j-1]
            elif j == 0:
                matrix[i][j] ^= matrix[i-1][j]
            else:
                matrix[i][j] ^= matrix[i-1][j] ^ matrix[i][j-1] ^ matrix[i-1][j-1]
			if len(q) < k:
				heapq.heappush(q, matrix[i][j])
			else:
				heapq.heappushpop(q, matrix[i][j])
    
    return q[0]
  
-------------------------------------------------------------------------------------------------
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        temp=0
        pq= []
        n = len(matrix)
        m = len(matrix[0])
        
        prefix= [  [0]*m for i in range(n) ]
        
        
        for i in range(n):
            for j in range(m):
                if i==0 or j==0:
                    if i==0 and j==0:
                        prefix[i][j] = matrix[i][j]
                    elif i==0 and j!=0:
                        prefix[i][j] ^= prefix[i][j-1]^ matrix[i][j]
                    else:
                        prefix[i][j]^=prefix[i-1][j]^ matrix[i][j]
                else:
                    
                    prefix[i][j] ^= prefix[i-1][j] ^ prefix[i][j-1]^matrix[i][j]^prefix[i-1][j-1]
                if len(pq)<k:
                    heappush(pq,prefix[i][j])    
                else:
                    heappush(pq, prefix[i][j])
                    heappop(pq)                                  
        return heappop(pq)
