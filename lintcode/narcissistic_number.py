'''

Narcissistic Number is a number that is the sum of its own digits each raised to the power of the number of digits. See wiki

For example the 3-digit decimal number 153 is a narcissistic number because 153 = 13 + 53 + 33.

And the 4-digit decimal number 1634 is a narcissistic number because 1634 = 14 + 64 + 34 + 44.

Given n, return all narcissistic numbers with n digits.

'''

from typing import (
    List,
)

class Solution:
    """
    @param n: The number of digits
    @return: All narcissistic numbers with n digits
    """
    def get_narcissistic_numbers(self, n: int) -> List[int]:
        # write your code here

        up = int(str(9)*n)
        res = list()
        for i in range(up+1):
            old_num = i
            s = str(i)
            numdigits = len(s)
            if numdigits == n:
                s = list(s)
                s = list(map(int, s))

                s_to_power = list(map(lambda x: x**numdigits, s))
                sum_pow = sum(s_to_power)
                # check

                if old_num == sum_pow:
                    #print(old_num)
                    res.append(old_num)
        return res
      
----------------------------

def get_num(n):
    ls = []
    if n == 1:
        ls.append(0)
    for i in range(10**(n-1),10**n):
        num = str(i)
        if sum([int(j)**n for j in num]) == int(num):
            ls.append(int(num))
    return ls
