'''
Two strings word1 and word2 are considered almost equivalent if the differences between the frequencies of each letter from 'a' to 'z' between word1 and word2 is at most 3.

Given two strings word1 and word2, each of length n, return true if word1 and word2 are almost equivalent, or false otherwise.

The frequency of a letter x is the number of times it occurs in the string.

 
 '''

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        s1 = word1
        s2 = word2
        abc = string.ascii_lowercase

        s1d = dict()
        s2d = dict()

        for i in range(len(abc)):
            s1d[abc[i]] = 0
        for i in range(len(abc)):
            s2d[abc[i]] = 0

        for i in range(len(s1)):
            s1d[s1[i]] += 1
        for i in range(len(s2)):
            s2d[s2[i]] += 1


        for k in s1d.keys():

            if abs(s1d[k] - s2d[k]) > 3:
                print('bad')
                return False
        return True
