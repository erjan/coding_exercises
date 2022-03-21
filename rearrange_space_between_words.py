'''
You are given a string text of words that are placed among some number of spaces. Each word consists of one or more lowercase English letters and are separated by at least one space. It's guaranteed that text contains at least one word.

Rearrange the spaces so that there is an equal number of spaces between every pair of adjacent words and that number is maximized. If you cannot redistribute all the spaces equally, place the extra spaces at the end, meaning the returned string should be the same length as text.

Return the string after rearranging the spaces.
'''

class Solution:
    def reorderSpaces(self, text: str) -> str:
        
        s = text
        
        if len(s) == 1:
            return s

        sp = s.count(' ')
        words = s.split()
        res = ''
        if len(words) == 1:
            res = words[0] + ' ' * sp
            print(res)
            return res
        proper_num_spaces = sp // (len(words)-1)
        extra_spaces = sp % (len(words)-1)
        print('extra spaces', extra_spaces)

        res = ''

        for i in range(len(words)):
            res += words[i] + ' ' * proper_num_spaces

        res = res.strip()

        res += ' ' * extra_spaces
        print(res)
        return res
      
#------ better solution      
class Solution:
    def reorderSpaces(self, text: str) -> str:
        s = text
        words = s.split()
        sp = s.count(' ')

        if len(words) == 1:
            return words[0] + ' ' * sp

        else:
            q, r = divmod(sp, len(words)-1)
            res = ((' ' * q).join(words) + ' ' * r)
            return res      
