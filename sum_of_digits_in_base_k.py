'''
Given an integer n (in base 10) and a base k, return the sum of the digits of n after converting n from base 10 to base k.

After converting, each digit should be interpreted as a base 10 number, and the sum should be returned in base 10.
'''

class Solution:
    def sumBase(self, n: int, k: int) -> int:
        output_sum = 0
        while (n > 0) :
            rem = n % k
            output_sum = output_sum + rem 
            n = int(n / k)
        return output_sum

    
class Solution:
def sumBase(self, n: int, k: int) -> int:

    res = 0

    while n > 0:

        rem = n%k
        res += rem 
        n = int(n/ k)
    return res

