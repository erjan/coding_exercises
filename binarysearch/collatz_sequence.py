'''
Given a positive integer n, find the length of its Collatz sequence. The Collatz sequence is generated sequentially where

n = n / 2 if n is even
n = 3 * n + 1 if n is odd
And the sequence ends if n = 1
'''

class Solution:
    def solve(self, n):

        l = list()
        l.append(n)

        while n !=1:

            if n %2 == 0:
                n = n/2
            
            else:
                n = 3 *n +1
            l.append(int(n))


        print(l)

        print(len(l))
        return len(l)
        
