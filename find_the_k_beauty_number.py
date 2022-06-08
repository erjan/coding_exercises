'''
The k-beauty of an integer num is defined as the number of substrings of num when it is read as a string that meet the following conditions:

It has a length of k.
It is a divisor of num.
Given integers num and k, return the k-beauty of num.
'''


class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        res = 0
        n = int(num)
        num = str(num)
        for i in range(len(num)-k+1):
            sub = num[i:i+k]

            sub = int(sub)
            if sub != 0 and n % sub == 0:
                res += 1
        return res
