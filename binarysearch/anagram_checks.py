'''

Given two strings s0 and s1, return whether they are anagrams of each other.

Constraints

n ≤ 100,000 where n is the length of s0
m ≤ 100,000 where m is the length of s1
'''


class Solution:
    def solve(self, s0, s1):

        if len(s0) != len(s1):
            return False
        
        s0 = list(s0)
        s1 = list(s1)

        s0.sort()
        s1.sort()

        if s0 != s1:
            return False
        return True

      
#another

class Solution:
    def solve(self, s0, s1):

        freq = {}
        freq2 = {}

        if len(s0) != len(s1):
            return False

        for ch in s0:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        for ch in s1:
            if ch in freq2:
                freq2[ch] += 1
            else:
                freq2[ch] = 1

        for key in freq.keys():
            if key not in freq2 or freq[key] != freq2[key]:
                return False

        return True

        
