'''

Given a string s, return its run-length encoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters.
'''


from itertools import groupby

class Solution:
    def solve(self, s):

        res = list()

        for c, g in groupby(s):
            res.append([len(list(g)), c])

        q = ''
        for k, v in res:
            q += str(k) + v
        del res
        return q
      
      
      
#another

class Solution:
    def solve(self, s):
        res = ""
        counter = 1
        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                counter += 1
            else:
                res = res + str(counter) + s[i - 1]
                counter = 1
        res = res + str(counter) + s[-1]
        return res
