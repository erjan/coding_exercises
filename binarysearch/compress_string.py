'''

Given a string lowercase alphabet s, eliminate consecutive duplicate characters from the string and return it.

That is, if a list contains repeated characters, they should be replaced with a single copy of the character. The order of the elements should not be changed.

'''


from itertools import groupby
class Solution:
    def solve(self, s):

        res = [ c  for c, g in groupby(s)]
        print(res)

        res = ''.join(res)
        print(res)
        return res
      
      
#another

class Solution:
    def solve(self, s):
        l = [s[0]]
        for c in s[1:]:
            if c == l[-1]:
                continue
            else:
                l.append(c)
        return "".join(l)
      
#another

class Solution:
    def solve(self, s):
        if not s:
            return ""
        res = [s[0]] + [s[i] for i in range(1, len(s)) if s[i] != s[i - 1]]
        return "".join(res)

        



        
