'''
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.
'''


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        cc = int(c ** 0.5)
        left = 0
        right = cc
        while left <= right:
            res = left ** 2 + right ** 2
            if res == c:
                return True
            elif res < c:
                left += 1
            elif res > c:
                right -= 1
        return False
