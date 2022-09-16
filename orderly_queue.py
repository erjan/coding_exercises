'''
You are given a string s and an integer k. You can choose one of the first k letters of s and append it at the end of the string..

Return the lexicographically smallest string you could have after applying the mentioned step any number of moves.
'''

class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            return "".join(sorted(s))
        else:
            res = s
            for i in range(0,len(s)):
                s = s[1:] + s[0]
                res = min(res,s)
                
            return res
          
-----------------------------------
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            return min([s[i:] + s[:i] for i in range(len(s))])
        return ''.join(sorted(s))
      
-------------------------------
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 0:
            return s
        if k > 1:
            return "".join(sorted(list(s)))
        else:
            answer = s
            for i in range(len(s)):
                s = s[1:] + s[0]
                answer = min(answer, s)
            return answer
        return s
