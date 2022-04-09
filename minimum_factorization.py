'''
Given a positive integer num, return 
the smallest positive integer x whose multiplication of each digit equals num. If there is no answer or the answer is not fit in 32-bit signed integer, return 0.

'''


class Solution:
    def smallestFactorization(self, num: int) -> int:
        if num == 1: return 1 # edge case 
        ans, mult = 0, 1
        for x in range(9, 1, -1): 
            while num % x == 0: 
                num //= x
                ans = ans + mult * x
                mult *= 10
        return ans if num == 1 and ans < (1 << 31) else 0
