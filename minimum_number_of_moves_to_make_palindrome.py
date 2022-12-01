'''
   You are given a string s consisting only of lowercase English letters.

In one move, you can select any two adjacent characters of s and swap them.

Return the minimum number of moves needed to make s a palindrome.

Note that the input will be generated such that s can always be converted to a palindrome.
'''
    
  
def minMovesToMakePalindrome(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return 0
        if s[0]==s[-1]:
            return self.minMovesToMakePalindrome(s[1:-1])
        
        ind_l, ind_r = s.find(s[-1]), s.rfind(s[0])
        if ind_l <= n-1-ind_r:
            return ind_l + self.minMovesToMakePalindrome(s[:ind_l] + s[ind_l+1:-1])
        else:
            return n-1-ind_r + self.minMovesToMakePalindrome(s[1:ind_r] + s[ind_r+1:])
-------------------------------------------------------------------------------------------------------
class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        s = list(s)
        n = len(s)
        left, right = 0, n-1
        res = 0
        while left < right:
            if s[left] != s[right]:
                lidx, ridx = left+1, right-1
                rdelta = 1
                while s[left] != s[ridx]:
                    ridx -= 1
                    rdelta += 1
                ldelta = 1
                while s[right] != s[lidx]:
                    lidx += 1
                    ldelta += 1
                if ldelta < rdelta:
                    for i in range(lidx,left,-1):
                        s[i-1],s[i] = s[i],s[i-1]
                    res += ldelta
                else:
                    for i in range(ridx,right):
                        s[i],s[i+1] = s[i+1],s[i]
                    res += rdelta
            left += 1
            right -= 1
        return res
