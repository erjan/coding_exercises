'''
You are given two strings s1 and s2, both of length 4, consisting of lowercase English letters.

You can apply the following operation on any of the two strings any number of times:

Choose any two indices i and j such that j - i = 2, then swap the two characters at those indices in the string.
Return true if you can make the strings s1 and s2 equal, and false otherwise.
'''
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        

        s1 = list(s1)
        s2 = list(s2)

        for i in range(len(s1)):
            for j in range(i+2,len(s1)):
                if s1[i]!= s2[i] and j-i == 2:
                    s1[i],s1[j] = s1[j],s1[i]
        
        s1 = ''.join(s1)
        s2 = ''.join(s2)
        return s1 == s2                    
