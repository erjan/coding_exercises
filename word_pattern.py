'''
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
'''


class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        pattern = list(pattern)
        st = str
        st = list(st.split(' '))
        if len(pattern) != len(st):
            return False


        d = dict()
        for pattern_char, letter in zip(pattern,st):
            if pattern_char not in d.keys():
                if letter not in d.values():
                    d[pattern_char] = letter
                elif letter in d.values():
                    return False
            elif pattern_char in d.keys():
                if d[pattern_char] !=  letter:
                    return False
        return True
