'''
Given a string word, return the sum of the number of vowels ('a', 'e', 'i', 'o', and 'u') in every substring of word.

A substring is a contiguous (non-empty) sequence of characters within a string.

Note: Due to the large constraints, the answer may not fit in a signed 32-bit integer. Please be careful during the calculations.
'''

class Solution:
    def countVowels(self, word: str) -> int:
        dp = []
        for i, el in enumerate(word):
            if el in 'aeiou':
                running_sum = i + 1 + (dp[-1] if dp else 0)
                dp.append(running_sum)
            else:
                dp.append(dp[-1] if dp else 0)
        return sum(dp)
