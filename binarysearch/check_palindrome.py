#Given a string s, return whether it is a palindrome.


class Solution:
    def solve(self, s):

        l = 0
        r = len(s)-1

        while l < r:

            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True
        
