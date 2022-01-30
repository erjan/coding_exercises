'''
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        k = len(s)
        
        if len(s) % 2 == 0:
            #do the even case
            mid = len(s)//2
            rev = s[mid:]
            rev = rev[::-1]
            if rev == s[:mid]:
                return True
            return False
            
            
        elif len(s) % 2 != 0:
            #do the odd case
            mid = len(s)//2
            first_part = s[:mid]
            second_part = s[(mid+1):]
            second_part = second_part[::-1]
            if first_part == second_part:
                return True
            return False
            
