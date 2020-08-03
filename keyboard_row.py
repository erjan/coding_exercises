'''
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
'''


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = list('qwertyuiop')
        second_row =list('asdfghjkl')
        third_row = list('zxcvbnm')
        result = []
        for word in words:
            s = set(word.lower())
            if s.issubset(first_row) or s.issubset(second_row) or s.issubset(third_row):
                result.append((word))
        print(result)
        return result
