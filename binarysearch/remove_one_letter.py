'''
Given two strings s0 and s1, return whether you can obtain s1 by removing 1 letter from s0.

Constraints

0 ≤ n ≤ 200,000 where n is the length of s0
0 ≤ m ≤ 200,000 where m is the length of `s1
'''

class Solution:
    def solve(self, s0, s1):
        if len(s0) != len(s1)+1:
            return False

        for i in range(len(s1)):
            if s1[i] != s0[i]:
                # check the substring
                return s1[i:] == s0[i+1:]

    
        return True
