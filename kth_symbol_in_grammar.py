'''
We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.
'''

def kthGrammar(self, N: int, K: int) -> int:
    
    def solver(N,K):
        if N==1 and K == 1 :
            return 0
        mid = 2**(N-2)
        if K <= mid:
            return solver(N-1,K)
        
        if K > mid:
            return 1-solver(N-1,K-mid)
    
    return solver(N,K)
  
-------------------------------------------------------------------------
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        
        if N == 1:
            # Base case:
            return 0
        
        else:
            # General case:
            if K % 2 == 0:
                
                # even index of current level is opposite of parent level's [(K+1)//2]
                return 0 if self.kthGrammar(N-1, (K+1)//2) else 1
            else:
                # odd index of current level is the same as parent level's [(K+1)//2]
                return 1 if self.kthGrammar(N-1, (K+1)//2) else 0
