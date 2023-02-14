'''
You are given a 0-indexed string s consisting of only lowercase English letters. In one operation, you can change any character of s to any other character.

Return true if you can make s a palindrome after performing exactly one or two operations, or return false otherwise.
'''

class Solution:
    def makePalindrome(self, s: str) -> bool:
        
        n = len(s)
        change = 0
        for x in range(n//2):
            if s[x]!=s[-1-x]:
                change+=1
                
        return change <= 2
        
-----------------------------------------
#one liner

class Solution:
    def makePalindrome(self, s: str) -> bool:
        
        return sum([s[x]!=s[-1-x] for x in range(len(s)//2)]) <= 2
      
------------------------------------------------------
class Solution:
    def makePalindrome(self, s: str) -> bool:

        diff = 0
        for i in range(len(s)//2):
            if s[i] != s[-1-i]:
                diff += 1
            
            if diff > 2:
                return False
        
        return True
      
-------------------------------------------------------------------------
class Solution:
    def makePalindrome(self, s: str) -> bool:
        i = c = 0
        j = len(s)-1

        while i<j:
            if s[i]!=s[j]: # counting the mismatches using two pointers
                c+=1
            i+=1
            j-=1

        return True if c<=2 else False

        
