'''
You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.

A substring is a contiguous sequence of characters within a string.
'''

class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = num
        
        while len(n) > 0:

            if n[-1] in ('1', '3', '5', '7', '9'):
                return str(n)
            n = n[:-1]

        return ''
