'''
Given an integer n, return the number of 1 bits in n.
'''


class Solution:
    def solve(self, n):
        return bin(n).count('1')
        
