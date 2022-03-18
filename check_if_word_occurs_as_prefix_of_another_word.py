'''
Given a sentence that consists of some words separated by a single space, and a searchWord, check if searchWord is a prefix of any word in sentence.

Return the index of the word in sentence (1-indexed) where searchWord is a prefix of this word. If searchWord is a prefix of more than one word, return the index of the first word (minimum index). If there is no such word return -1.

A prefix of a string s is any leading contiguous substring of s.
'''

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
    
        s = sentence
        
        s = s.split()
        q = len(searchWord)
        index = 1
        for i in range(len(s)):
            
            if s[i][:q] == searchWord:
                index = i+1
                return index
        return -1
                
                
            
