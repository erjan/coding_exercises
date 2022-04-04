'''

Given an integer n greater than or equal to 0, return whether it is a power of two.
'''


class Solution:
    def solve(self, n):        
        check = list()
        for i in range(0, 32):
            check.append(2**i)
        

        if n not in check:
            return False
        return True
      
#another

class Solution:
    def solve(self, n):
        if n == 0:
            return False
        return (n & (n - 1)) == 0

        
