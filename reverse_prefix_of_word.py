'''
Given a 0-indexed string word and a character ch, reverse the segment of word that starts
at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.

For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that 
starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".
Return the resulting string.
'''

#my own solution

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        if ch not in word:
            return word
        else:

            s = word.index(ch)
            pref = word[:(s+1)]
            pref = pref[::-1]
            after_pref = word[(s+1):]
            word = pref + after_pref
            print(word)
            return word
        
