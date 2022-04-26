'''
You are given two strings s and t of equal 
length only consisting of lowercase letters. Assuming that you can 
first rearrange s into any order, return the minimum number of changes needed to turn s into t.
'''


class Solution:
    def solve(self, s, t):
        diff = Counter(t) - Counter(s)
        return sum(diff.values())
      
      
-----------------------------------------------------------------------------
class Solution:
    def solve(self, s, t):

        count = 0

        s_d = dict(Counter(s))
        t_d = dict(Counter(t))

        res = list(set(s+t))

        for i in range(len(res)):
            key = res[i]

            if key in s_d and key in t_d:
                count += abs(s_d[key] - t_d[key])
            elif key in s_d and key not in t_d:
                count += s_d[key]
            elif key in t_d and key not in s_d:
                count += t_d[key]
        return count//2

        
