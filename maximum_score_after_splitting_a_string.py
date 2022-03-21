'''
Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

'''

class Solution:
    def maxScore(self, s: str) -> int:
        res, co, cl = 0, 0, s.count("1")
        for i in range(len(s)-1):
            if s[i] == "0": co += 1
            else: cl -= 1
            res = max(co+cl, res)
        return res
