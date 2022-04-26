'''
Given two strings s0 and s1, each representing a sentence, return the number of unique words that are shared between the two sentences.

Note: words are case-insensitive so "hello" and "Hello" are the same word.
'''


class Solution:
    def solve(self, s0, s1):

        s0 = s0.lower()
        s1 = s1.lower()

        s0 = set(s0.split())
        s1 = set(s1.split())


        return len(s0.intersection(s1))

        
