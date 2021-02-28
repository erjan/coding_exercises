'''
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.
'''


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1 = ''
        s2 = ''
        
        for i in word1:
            s1+= i
        
        for i in word2:
            s2 += i
            
        return s1 == s2
        
