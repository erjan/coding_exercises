'''
Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].
'''

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        
        a = s
        b = goal
        
        if len(a) != len(b):
            return False
        
        if a == b and len(set(a)) < len(a):
            return True
        
        
        diff = []
        
        for i in range(len(s)):
            if a[i] != b[i]:
                diff.append( [a[i], b[i]]  )
                
        
        
        if len(diff) > 2:
            return False
        
        if len(diff) == 2:
            
            mismatch1 = diff[0]
            mismatch2 = diff[1]
            
            mismatch2 = mismatch2[::-1]
            
            if mismatch1 == mismatch2:
                return True
        
        return False
        
