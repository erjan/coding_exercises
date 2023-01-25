'''
You are given a positive integer n. Each digit of n has a sign according to the following rules:

The most significant digit is assigned a positive sign.
Each other digit has an opposite sign to its adjacent digits.
Return the sum of all digits with their corresponding sign.
'''



class Solution:
    def alternateDigitSum(self, n: int) -> int:

        res = 0

        positive = True
        s = str(n)

        for el in s:
            if positive:
                res += int(el)
                positive = False
            elif not positive:
                res -= int(el)
                positive = True
        return res
