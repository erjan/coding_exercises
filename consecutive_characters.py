'''
The power of the string is the maximum length of a non-empty substring that contains only one unique character.

Given a string s, return the power of s.

 '''

class Solution:
    def maxPower(self, s: str) -> int:
        def f(x): return [list(group) for c, group in itertools.groupby(x)]

        s = f(s)

        maxi = 0
        for i in range(len(s)):

            if len(s[i]) > maxi:
                maxi = len(s[i])
        print(maxi)
        return maxi
