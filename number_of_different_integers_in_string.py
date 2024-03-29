'''
You are given a string word that consists of digits and lowercase English letters.

You will replace every non-digit character with a space. For example, "a123bc34d8ef34" will become " 123  34 8  34". Notice that you are left with some integers that are separated by at least one space: "123", "34", "8", and "34".

Return the number of different integers after performing the replacement operations on word.

Two integers are considered different if their decimal representations without any leading zeros are different.


 '''

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        s = word
        s = list(s)
        for i in range(len(s)):

            if s[i].isnumeric():
                continue
            else:
                s[i] = ' '

        s = ''.join(s)
        s = s.split()
        s = set(map(lambda x: int(x), s))

        res = len(s)
        print(res)
        return res
