'''
We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
'''

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <=0:
            return False
        res = 0
        limit = int(math.sqrt(num))+1
        for i in range(1, limit):
            if num % i == 0:
                res+=i
                if i * i  != num:
                    res+=num/i
                    
        return num == (res - num)
