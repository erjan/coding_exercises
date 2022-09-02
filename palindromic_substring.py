'''
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.
'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        
        res = 0
        
        
        for i in range(len(s)):
            
            l = i
            r = i
            
            while l >=0 and r < len(s) and s[l] == s[r]:
                res+=1
                l -=1
                r+=1
            l = i
            r = i+1
            
            while l >=0 and r < len(s) and s[l] == s[r]:
                res+=1
                l-=1
                r+=1
        return res
----------------------------------------------------------------------------------

   def countSubstrings(self, s: str) -> int:
        pal = [[None]*len(s) for _ in range(len(s))]
        ans = 0
		
		# Setting single-character palindromes:
        for i in range(len(s)):
            pal[i][i] = True
            ans += 1
		
		# Checking for other palindromes:
        for i in range(len(s)-1, -1, -1):
            for j in range(len(s)-1, i, -1):
                if s[i] == s[j] and pal[i+1][j-1] != False:
                    pal[i][j] = True
                    ans += 1
                else:
                    pal[i][j] = False
					
		# Print all found palindromes:
        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         if pal[i][j]:
        #             print(s[i:j+1])
        return ans
                
