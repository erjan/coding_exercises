'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.
'''


from string import ascii_uppercase as abc

class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ''
        while n:
            n = n-1
            res = abc[n%26]+res
            n = n //26
        return res
