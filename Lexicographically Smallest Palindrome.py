'''
You are given a string s consisting of lowercase English letters, and you are allowed to perform operations on it. In one operation, you can replace a character in s with another lowercase English letter.

Your task is to make s a palindrome with the minimum number of operations possible. If there are multiple palindromes that can be made using the minimum number of operations, make the lexicographically smallest one.

A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears earlier in the alphabet than the corresponding letter in b.

Return the resulting palindrome string.
'''

class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:

        i = 0
        s = list(s)
        j = len(s)-1
        while i < j:
            if s[i]!=s[j]:
                if s[i]<s[j]:
                    s[j]=s[i]
                else:
                    s[i]=s[j]
            i+=1
            j-=1
        
        return "".join(s)
        
-------------------------------------------
class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:    #  Example: s = 'sdnvnfe'

        ans, n = list(s), len(s)                        # n = 7 ,  n//2 = 3
                                                        #         ans = [s, d, n, v, n, f, e]
        for i in range((n+1)//2): 
                                                        #  i = 0: ans = [|e| ,d,n,v,n,f, |e|]
            ans[i]=ans[n-i-1] = min(ans[i],ans[n-i-1])  #  i = 1: ans = [e,|d|, n,v,n, |d|,e] 
                                                        #  i = 2: ans = [e,d,|n|, v, |n|,d,e]
     
        return ''.join(ans)                             #  return ().join([e,d,n,v,n,d,e]) = 'ednvnde'
