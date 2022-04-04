'''

Given a lowercase alphabet string s, determine whether it has all unique characters.
'''


class Solution:
    def solve(self, s):
        
        res = collections.Counter(s)

        res = list(res.values())

        for i in res:
            if i != 1:
                return False
        return True
