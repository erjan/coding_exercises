'''
Given a string s and an array of strings words, determine whether s is a prefix string of words.

A string s is a prefix string of words if s can be made by concatenating the first k strings in words for some positive k no larger than words.length.

Return true if s is a prefix string of words, or false otherwise.
'''
#my own solution

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        total_len = len(s)
        made_len = 0
        new_s = ''
        for i in range(len(words)):
            if made_len >= total_len:
                break
            else:
                new_s += words[i]
                made_len = made_len + len(words[i])
        print(new_s)
        print('lengths are: ')
        print('new_s length : %d' % len(new_s))
        print('target word length %d ' % len(s))
        if new_s == s:
            print('good word')
        else:
            print('bad!')
        return new_s == s
