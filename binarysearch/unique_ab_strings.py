'''
You are given a string s of "a" and "b"s. "a"s can stay "a" or turn into "b", but "b"s can't change.

Return the number of unique strings that can be made.
'''

class Solution:
    def solve(self, s):
        a = s.count('a')

        return pow(2,a)
