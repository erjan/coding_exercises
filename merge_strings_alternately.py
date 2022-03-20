'''
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
'''

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        w1 = word1
        w2 = word2
        minlen = min(len(w1), len(w2))
        res = ''
        for i in range(minlen):

            res += w1[i]
            res += w2[i]

        if len(w2) > len(w1):
            diff = len(w2) - len(w1)
            res += w2[-diff:]

        elif len(w2) < len(w1):
            diff = len(w1) - len(w2)
            res += w1[-diff:]
        print(res)
        return res
