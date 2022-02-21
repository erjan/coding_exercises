'''
Given a string licensePlate and an array of strings words, find the shortest completing word in words.

A completing word is a word that contains all the letters in licensePlate. Ignore numbers and spaces in licensePlate, and treat letters as case insensitive. If a letter appears more than once in licensePlate, then it must appear in the word the same number of times or more.

For example, if licensePlate = "aBc 12c", then it contains letters 'a', 'b' (ignoring case), and 'c' twice. Possible completing words are "abccdef", "caaacab", and "cbca".

Return the shortest completing word in words. It is guaranteed an answer exists. If there are multiple shortest completing words, return the first one that occurs in words.
'''

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        lp = licensePlate
        cnt = collections.Counter("".join(c for c in lp.lower() if c.isalpha()))
        return min([w for w in words if not cnt - collections.Counter(w)], key = len)
