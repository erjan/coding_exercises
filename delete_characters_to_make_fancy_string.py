'''
A fancy string is a string where no three consecutive characters are equal.

Given a string s, delete the minimum possible number of characters from s to make it fancy.

Return the final string after the deletion. It can be shown that the answer will always be unique.
'''
class Solution:
    def makeFancyString(self, s: str) -> str:
        
        
        
        if len(s) <3:
            return s
        
        s = list(s)
        res = ''

        res += s[0]
        res += s[1]
        for i in range(2,len(s)):
            if s[i] != res[-1] or s[i] != res[-2]:
                res += s[i]
        print(res)
        return res
    
