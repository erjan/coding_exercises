'''


Given a lowercase alphabet string s, return the index of the first recurring character in it. If there are no recurring characters, return -1.


'''


class Solution:
    def solve(self, s):

        if len(s) <=1:
            return -1

        d = dict()

        for i in range(len(s)):

            if s[i] not in d:
                d[s[i]] = [i,1]
            else:
                return i
        return -1
        

        
#another

class Solution:
    def solve(self, s):
        a = set()
        n = min(len(s), 27)
        for i in range(n):
            if s[i] in a:
                return i
            else:
                a.add(s[i])
        return -1
        
        
