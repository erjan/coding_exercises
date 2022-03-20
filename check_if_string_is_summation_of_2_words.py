'''
The letter value of a letter is its position in the alphabet starting from 0 (i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, etc.).

The numerical value of some string of lowercase English letters s is the concatenation of the letter values of each letter in s, which is then converted into an integer.

For example, if s = "acb", we concatenate each letter's letter value, resulting in "021". After converting it, we get 21.
You are given three strings firstWord, secondWord, and targetWord, each consisting of lowercase English letters 'a' through 'j' inclusive.

Return true if the summation of the numerical values of firstWord and secondWord equals the numerical value of targetWord, or false otherwise.
'''

class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        s1 = 'abcdefghij'
        s2 = [i for i in range(11)]

        d = dict(zip(s1, s2))
        print(d)

        s1 = ''
        for i in range(len(firstWord)):

            s1 += str(d[firstWord[i]])
        s2 = ''

        for i in range(len(secondWord)):
            s2 += str(d[secondWord[i]])

        s3 = ''
        for i in range(len(targetWord)):
            s3 += str(d[targetWord[i]])

        print(s1,s2,s3)

        s1 = int(s1)
        s2 = int(s2)
        s3 = int(s3)

        return s1 + s2 == s3
