'''
Given an integer n, return true if and only if it is an Armstrong number.

The k-digit number n is an Armstrong number if and only if the kth power of each digit sums to n.
'''

class Solution:
    def isArmstrong(self, n: int) -> bool:
        
        nlen = len(str(n))
        
        res = 0
        n = str(n)
        
        for i in range(len(n)):
            res += int(n[i])**nlen
        n = int(n)
        return res == n
            
