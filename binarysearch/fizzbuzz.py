'''

Given an integer n, return a list 
of integers from 1 to n as strings except 
for multiples of 3 use “Fizz” instead of the 
integer and for the multiples of 5 use “Buzz”. For integers 
which are multiples of both 3 and 5 use “FizzBuzz”.

'''


class Solution:
    def solve(self, n):

        res = list()
        for i in range(1, n+1):
        
            if i %3 == 0 and i %5 != 0:
                res.append('Fizz')

            elif i %5 == 0 and i %3 != 0:
                res.append('Buzz')

            elif i %3 == 0 and i % 5 ==0:
                res.append('FizzBuzz')

            else:
                res.append(str(i))

        return res
            

        
