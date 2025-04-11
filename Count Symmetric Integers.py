'''
You are given two positive integers low and high.

An integer x consisting of 2 * n digits is symmetric if the sum of the first n digits of x is equal to the sum of the last n digits of x. Numbers with an odd number of digits are never symmetric.

Return the number of symmetric integers in the range [low, high].
'''

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        

        res = 0

        for i in range(low, high+1):
            if len(str(i)) %2 == 0:
                mid = len(str(i))//2
                ad = list(str(i))

                ad = list(map(int, ad))

                if sum(ad[:mid]) == sum(ad[mid:]):
                    res+=1
        return res



