'''
You are given two strings s and t of the same length and an integer maxCost.

You want to change s to t. Changing the ith character of s to ith character of t costs |s[i] - t[i]| (i.e., the absolute difference between the ASCII values of the characters).

Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of t with a cost less than or equal to maxCost. If there is no substring from s that can be changed to its corresponding substring from t, return 0.
'''

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        cost=0
        l=0
        ans=0
        for r in range(len(s)):
            
            cost+= abs(ord(s[r])-ord(t[r]))
            while cost > maxCost:
                cost -= abs(ord(s[l]) - ord(t[l]))
                l+=1
            ans=max(ans,  r-l+1)
        return ans
