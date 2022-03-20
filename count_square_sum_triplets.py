'''
A square triple (a,b,c) is a triple where a, b, and c are integers and a2 + b2 = c2.

Given an integer n, return the number of square triples such that 1 <= a, b, c <= n.
'''

class Solution:
    def countTriples(self, n: int) -> int:
        
        c = 0
        for i in range(1,n):
            for j in range(i+1, n):

                sq = (i*i + j*j)
                r = int(sq**0.5)
                if r*r == sq and r <=n:
                    c+=2
        return c
