'''
Given a string s and a character letter, return the percentage of characters in s that equal letter rounded down to the nearest whole percent.
'''

import math
class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        total = len(s)

        match = s.count(letter)

        e = math.floor(100 * (match/total))
        print(e)
        return e
