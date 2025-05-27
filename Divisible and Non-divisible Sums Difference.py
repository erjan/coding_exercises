'''
You are given positive integers n and m.

Define two integers as follows:

num1: The sum of all integers in the range [1, n] (both inclusive) that are not divisible by m.
num2: The sum of all integers in the range [1, n] (both inclusive) that are divisible by m.
Return the integer num1 - num2.
'''

-----------------------------------------------------------------------


class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        n1 = sum(i for i in range(1,n+1) if i%m !=0)
        n2 = sum(i for i in range(1,n+1) if i%m ==0)
        return n1-n2

-----------------------------------------------------------------------

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        return n*(n+1)//2-m*(n//m)*(n//m+1)
