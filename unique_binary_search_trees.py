'''
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.
'''

class Solution:
    def h(self,n):
        
        if (n == 0 or n == 1):
            return 1
        
        catalan = [0  for i in range(n+1)]
        
        catalan[0] =1
        catalan[1] =1
        
        for i in range(2,n+1):
            catalan[i] = 0
            for j in range(i):
                catalan[i] += catalan[j] * catalan[i-j-1]
        
        return catalan[n]
                
    def numTrees(self, n: int) -> int:
            
    
        return self.h(n)
        
        
