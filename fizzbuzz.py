'''
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number 
and for the multiples of five output “Buzz”. For numbers which are 
multiples of both three and five output “FizzBuzz”.
'''

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                res.append('FizzBuzz')
                # print('FizzBuzz')
            elif i % 5 == 0:
                res.append('Buzz')
                # print('Buzz')
            elif i % 3 == 0:
                res.append('Fizz')
                # print('Fizz')
            else:
                res.append(str(i))
                # print(i)
        print(res)
        return res
