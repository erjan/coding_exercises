'''
Given two strings s and t, find the number of ways you can choose a non-empty substring of s and replace a single character by a different character such that the resulting substring is a substring of t. In other words, find the number of substrings in s that differ from some substring in t by exactly one character.

For example, the underlined substrings in "computer" and "computation" only differ by the 'e'/'a', so this is a valid way.

Return the number of substrings that satisfy the condition above.

A substring is a contiguous sequence of characters within a string.
'''


class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        ans=0
        arr=[]
        for i in range(len(s)):#Get All Substrings
            for j in range(i+1,len(s)+1):
                arr.append(s[i:j])
        
        for w in arr:
            i=0
            j=len(w)
            while j<=len(t):
                wrd=t[i:j]
                k=1#Only one difference allowed
                flag=True
                for m in range(len(wrd)):
                    if w[m]!=wrd[m]:
                        if k==1:
                            k=0
                        else:
                            flag=False
                            break
                if flag and k==0:
                    ans+=1
                i+=1
                j+=1
        return ans
    
----------------------------------------------------------------------------------------------
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        
        ans = 0
        
        for i in range(len(s)):
            for j in range(len(t)):
                
                x = i
                y = j
                diff = 0
                while x < len(s) and y < len(t):
                    if s[x] != t[y]:
                        diff+=1
                    if diff ==1:
                        ans+=1
                    elif diff ==2:
                        break
                    x+=1
                    y+=1
        return ans
