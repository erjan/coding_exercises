'''
Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.
'''

class Solution(object):
    def trailingZeroes(self, n):
        k, tot = 5, 0
        while k <= n:
            tot += n // k
            k = k * 5
        return tot
