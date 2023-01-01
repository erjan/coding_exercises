'''
Given an integer num, return the number of digits in num that divide num.

An integer val divides nums if nums % val == 0.
'''


class Solution:
    def countDigits(self, num: int) -> int:
        res = 0

        s = list(str(num))
        s = list(map(lambda x: int(x),s))


        for el in s:
            if num % el == 0:
                res+=1
        return res
      
-------------------------------------------
class Solution(object):
    def countDigits(self, num):
        str_num, count = str(num), 0
        for digit in str_num:
            if num % int(digit) == 0:
                count += 1
        return count
