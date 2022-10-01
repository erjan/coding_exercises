'''
A string is considered beautiful if it satisfies the following conditions:

Each of the 5 English vowels ('a', 'e', 'i', 'o', 'u') must appear at least once in it.
The letters must be sorted in alphabetical order (i.e. all 'a's before 'e's, all 'e's before 'i's, etc.).
For example, strings "aeiou" and "aaaaaaeiiiioou" are considered beautiful, but "uaeio", "aeoiu", and "aaaeeeooo" are not beautiful.

Given a string word consisting of English vowels, return the length of the longest beautiful substring of word. If no such substring exists, return 0.

A substring is a contiguous sequence of characters in a string.
'''

class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        begin = None
        best = 0
        a_detected = False
        for index, value in enumerate(word):
            if not a_detected and value == 'a':
                begin = index
                a_detected = True
            elif a_detected and value < word[index-1]:
                if len(set(word[begin:index])) == 5:
                    best = max(best, len(word[begin:index]))
                if value == 'a':
                    begin = index
                else:
                    begin = None
                    a_detected = False
        best = max(best, len(word[begin:])) if a_detected and len(set(word[begin:])) == 5 else best
        return best
