'''
You are given a string s. You can convert s to a 
palindrome
 by adding characters in front of it.

Return the shortest palindrome you can find by performing this transformation.
'''

class Solution:
    def shortestPalindrome(self, s: str) -> str:

        i = 0
        s_r = s[::-1]
        minimum = 0
        
        while i < len(s):
            if s_r[i:] == s[:len(s) - i]:
                minimum = i
                break
                
            i += 1

        return s_r[:minimum] + s
