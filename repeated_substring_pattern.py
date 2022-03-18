'''
Given a string s, check if it can be constructed by taking a substring of it and 
appending multiple copies of the substring together.'''

#must know a trick solution/ observation
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        return s in s[1:] + s[:-1]

 #another iterative solution   
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:        
        rep = ''        
        length_s = len(s)
        
        for i in range(len(s)//2):
            rep += s[i]
            if length_s % len(rep) == 0:
                if rep * (length_s // len(rep)) == s:
                    return True
        return False    
