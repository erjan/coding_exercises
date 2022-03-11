'''
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.
'''



class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s = sentence
        abc = string.ascii_lowercase

        res = collections.Counter(s)

        res = ''.join(sorted(set(res.keys())))

        print('abc')
        print(abc)
        print('res')
        print(res)
        if len(res) != 26:
            print('bad')
            return False
        else:
            print('pangram')
            return True
