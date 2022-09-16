'''
Given a palindromic string of lowercase English letters palindrome, replace exactly one character with any lowercase English letter so that the resulting string is not a palindrome and that it is the lexicographically smallest one possible.

Return the resulting string. If there is no way to replace a character to make it not a palindrome, return an empty string.

A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, a has a character strictly smaller than the corresponding character in b. For example, "abcc" is lexicographically smaller than "abcd" because the first position they differ is at the fourth character, and 'c' is smaller than 'd'.
'''

class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """ 
        p1 = 0
        p2 = len(palindrome)-1
        new_pal = list(palindrome)
        while p1 < p2:
            if new_pal[p1] != "a":
                new_pal[p1] = "a"
                return "".join(new_pal)
            p1+=1
            p2-=1
        if len(new_pal) == 1: return ""
        new_pal[-1] = "b"
        return "".join(new_pal)
        
--------------------------------------------------
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
         
        
        for i in range(len(palindrome)//2):
                if palindrome[i]!='a':
                    return palindrome[:i]+'a'+palindrome[i+1:]
                        
        return palindrome[:-1]+'b' if len(palindrome)>1 else ""
