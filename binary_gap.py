'''
Given a positive integer n, find and return the longest distance
between any two adjacent 1's in the binary representation of n. If there are no two adjacent 1's, return 0.

Two 1's are adjacent if there are only 0's separating them (possibly no 0's). The distance between two 1's is the absolute difference between their bit positions. For example, the two 1's in "1001" have a distance of 3.
'''

class Solution:
    def binaryGap(self, n: int) -> int:
        n = str(bin(n))[2:]
        c = 0
        for i in range(len(n)):
            if n[i] == '1':
                j = i+1
                while j < len(n):
                    if n[j] == '1':
                        c = max(j-i,c)
                        break
                    j += 1

        return c
