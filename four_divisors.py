'''
Given an integer array nums, return 
the sum of divisors of the integers in that array that have exactly four divisors. If there 
is no such integer in the array, return 0. 
'''

class Solution:
    def sumFourDivisors(self, nums) -> int:
        sum_divs = 0
        for n in nums:
            divs = {1, n}
            for i in range(2, int(pow(n, 0.5)) + 1):
                if not n % i:
                    divs.add(i)
                    divs.add(n // i)
                if len(divs) > 4:
                    break
            else:
                if len(divs) == 4:
                    sum_divs += sum(divs)
        return sum_divs
