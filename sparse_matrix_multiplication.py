'''
Given two sparse matrices mat1 of size m x k and mat2 of size k x n, return the result of mat1 x mat2. You may assume that multiplication is always possible.
'''

class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ## RC ##
        ## BASIC SOLUTION  ##
        ## 1. For any matrix multiplication, solution is without IF condition. but its N^3
        ## 2. As this is sparse matrix, most of the elements are 0's. so we can make it effient to run the third loop only when we have element in A matrix.
        mA, nA, nB = len(A),len(A[0]),len(B[0])
        res = [[0]*len(B[0]) for _ in range(mA)]
        for i in range(mA):
            for j in range(nA):
                if A[i][j]:
                    for k in range(nB):
                        res[i][k] += A[i][j]*B[j][k]
        return res
    
        ## 3. But Even #2 is not efficient, so we store non-zero elements in a hashmap of hashmaps and checking those calculating ans is enough
        ## (m1 * n1) x (m2 * n2) = (m1 * n2) [ n1 = m2 always, we check the same here while looping through hashmaps ]
        m1, n1 = len(A), len(A[0])
        m2, n2 = len(B), len(B[0])
        res = [[0 for i in range(n2)] for j in range(m1)]
        X, Y = [dict() for i in range(m1)], [dict() for j in range(n2)]
        
        for i in range(m1):
            for j in range(n1):
                if A[i][j] != 0:
                    X[i][j] = A[i][j]
        
        for i in range(m2):
            for j in range(n2):
                if B[i][j] != 0:
                    # watchout (j,i)
                    Y[j][i] = B[i][j]
                    
        for i in range(m1):
            for j in range(n2):
                for r in X[i]:
                    if r in Y[j]:
                        res[i][j] += X[i][r] * Y[j][r]
        return res
---------------------------------------------------------------------------
class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        
        n,m,k=len(A), len(B), len(B[0])
        row_A=[{} for i in range(n)]
        col_B=[{} for j in range(k)]
        C=[[0 for i in range(k)] for j in range(n)]
        
        for i in range(n):
            for j in range(m):
                if A[i][j]!=0:
                    row_A[i][j]=A[i][j]
        
        for j in range(k):
            for i in range(m):
                if B[i][j]!=0:
                    col_B[j][i]=B[i][j]
        
        for i in range(n):
            for j in range(k):
                common_idx= row_A[i].keys() & col_B[j].keys()
                for idx in common_idx:
                    C[i][j]+=row_A[i][idx]*col_B[j][idx]
                    
        return C
---------------------------------------------------------------

class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        
        d = defaultdict(dict)
        for i, row in enumerate(B):
            for j, col in enumerate(row):
                if col!=0:
                    d[j][i]= col
                
        #print(d) // you may use this to get the idea
		row = len(A)
        col = len(B[0])
        res = [[0 for j in range(col)] for i in range(row)]
        
        for i,row in enumerate(A):
            for j in range(col):
                tmp = 0
                for ele in d[j]:
                    tmp+=(d[j][ele]*row[ele])
                res[i][j]=tmp
            
        return res
      
----------------------------------------------------------

import collections

class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not B or not A[0] or not B[0]:
            return 0
        
        hash_a = self.hash_a(A)
        hash_b = self.hash_b(B)
        n, m = len(A), len(B[0])
        ans = [[0] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                if i in hash_a and j in hash_b:
                    ans[i][j] = self.multi_vector(hash_a[i], hash_b[j])
        return ans
    
    def hash_a(self, A):
        hash_a = {}
        n, k = len(A), len(A[0])
        for i in range(n):
            local_hash = {}
            for j in range(k):
                if A[i][j] == 0:
                    continue
                local_hash[j] = A[i][j]
            hash_a[i] = local_hash
        return hash_a
    
    def hash_b(self, B):
        hash_b = {}
        k, m = len(B), len(B[0])
        for i in range(m):
            local_hash = {}
            for j in range(k):
                if B[j][i] == 0:
                    continue
                local_hash[j] = B[j][i]
            hash_b[i] = local_hash
        return hash_b
    
    def multi_vector(self, a, b):
        ans = 0
        for key in a:
            if key not in b:
                continue
            ans += a[key] * b[key]
        return ans
---------------------------------------------

Time: O(i * j* k)
Space: O(1)

 2*3 X 3*3 = 2*3
 1. len(A col) == len(B row)
 2. ans --> len(A row) * len(B col)
class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        res = [[0] * len(B[0]) for _ in range(len(A))]

        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    if A[i][k] and B[k][j]:
                        res[i][j] += A[i][k]*B[k][j]
        return res
---------------------------------------------

class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:

        n_row, n_k, n_col = len(A), len(A[0]), len(B[0])
        res = [[0]*n_col for _ in range(n_row)]
        for i in range(n_row):
            for j in range(n_col):
                s = 0
                for k in range(n_k): 
                    s += A[i][k]*B[k][j]
                res[i][j] = s
        
        return res
      
      
      
      
