'''
You are given a string allowed consisting of distinct characters and an array of strings words. 
A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.
'''

#my own solution! yay!!!

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        good_word = 0
        for word in words:
            word = set(word)
            bad = False
            for w in word:
                if w not in allowed:
                    bad = True
                    break
            if not bad:
                good_word += 1
        print('good words number %d' % good_word)
        return good_word
