'''

You are given a string s containing digits from "0" to "9" and lowercase alphabet characters. Return the sum of the numbers found in s.

'''


class Solution:
    def solve(self, s):

            s = list(s)

            for i in range(len(s)):
                if not s[i].isdigit():
                    s[i] = ' '

            s = ''.join(s)
            s = s.split(' ')
            s = list(filter(lambda x: x.isdigit(), s))
            s = list(map(lambda y: int(y), s))
            s = sum(s)
            return s
