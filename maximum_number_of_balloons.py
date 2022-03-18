'''
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.
'''

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
           s = text

        b = s.count('b')
        a = s.count('a')
        l = s.count('l')//2
        o = s.count('o')//2
        n = s.count('n')
        print(b, a, l, o, n)
        res = min(b, a, l, o, n)
        print('total')
        print(res)
        return res
