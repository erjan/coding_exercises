'''
You are given two positive integers n and k. A factor of an integer n is defined as an integer i where n % i == 0.

Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has less than k factors.
'''

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
                
        #get all factors        
        f = []              
        for i in range(1,n+1):
            
            if n%i == 0:
                f.append(i)                
        if k > len(f):
            return -1
        
        return f[k-1]
