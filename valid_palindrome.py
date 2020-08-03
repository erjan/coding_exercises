'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.
'''



class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join(list(filter(lambda ch: ch.isalnum(),s)))
        return s[::-1] == s
        
