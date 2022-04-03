'''

The Fibonacci sequence goes like this: 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

The next number can be found by adding up the two numbers before it, and the first two numbers are always 1.

Write a function that takes an integer n and returns the nth Fibonacci number in the sequence.

'''


class Solution:
    def solve(self, n):
        if n == 0 or n == 1:
            return 1
        res = [1,1]
        
        for i in range(2, n):
                
            res.append(res[i-1] + res[i-2])
            
        return res[-1]
