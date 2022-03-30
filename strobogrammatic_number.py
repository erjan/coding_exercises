'''
Given a string num which represents an integer, return true if num is a strobogrammatic number.

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
'''


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
           
        old_n = num

        n = str(num)

        if '2' in n or '3' in n or '4' in n or '5' in n or '7' in n:
            return False

        n = list(n)
        res = [0] * len(n)

        for i in range(len(n)):
            if n[i] == '9':
                res[i] = '6'

            elif n[i] == '8':
                res[i] = '8'

            elif n[i] == '1':
                res[i] = '1'

            elif n[i] == '0':
                res[i] = '0'

            elif n[i] == '6':
                res[i] = '9'

        res = ''.join(res)

        res = res[::-1]
        res = int(res)
        old_n = int(old_n)

        if old_n == res:
            return True
        return False
