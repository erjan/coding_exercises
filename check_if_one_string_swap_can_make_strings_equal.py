'''
You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.
'''

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        c = 0
        l = list()
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                l.append(i)
                c += 1
                print(i)

        if c != 2:
            return False
                
        s1 = list(s1)
        s1[l[0]], s1[l[1]] = s1[l[1]], s1[l[0]]
        s1 = ''.join(s1)
        print(s1)
        print(s2)
        if s1 == s2:
            return True
        return False
 
