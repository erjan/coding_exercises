'''
A substring is a contiguous (non-empty) sequence of characters within a string.

A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and has all five vowels present in it.

Given a string word, return the number of vowel substrings in word.
'''

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        s = word
        count = 0
        vowels = list(set('aeiou'))
        i = 0
        print('STRING: ', s)
        while i < len(s):
            if s[i] in vowels:
                j = i+1
                while j < len(s) and s[j] in vowels:
                    j += 1
                    substring = s[i:j]
                    if list(set(substring)) == vowels:
                        count += 1
                i += 1

            else:
                i += 1

        return count
