'''
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
'''

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        s = word
        all_caps = True
        all_low = True
        for i in range(len(s)):
            if s[i].isupper() == False:
                all_caps = False
                break

        for i in range(len(s)):
            if s[i].islower() == False:
                all_low = False
                break
        first_letter_cap = s[0].isupper()
        the_rest = s[1:]
        for i in range(len(the_rest)):
            if the_rest[i].isupper():
                first_letter_cap = False
                break
        if all_caps or all_low or first_letter_cap:
            return True
        return False 
