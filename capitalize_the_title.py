'''
You are given a string title consisting of one or more words separated by a single space, where each word consists of English letters. Capitalize the string by changing the capitalization of each word such that:

If the length of the word is 1 or 2 letters, change all letters to lowercase.
Otherwise, change the first letter to uppercase and the remaining letters to lowercase.
Return the capitalized title.
'''

#my own solution

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        s = title
        s = s.lower()
        s = s.split()
        res = ''
        for i in range(len(s)):
            word = s[i]

            if len(word) >= 3:
                first_letter = word[0]
                rest = word[1:]
                first_letter = first_letter.upper()
                word = first_letter + rest
            word = ' ' + word
            res += ''.join(word)
            res = res.strip()
        print(res)
        return res
