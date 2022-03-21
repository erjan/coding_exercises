'''
You are given an alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).

You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.

Return the reformatted string or return an empty string if it is impossible to reformat the string.
'''

class Solution:
    def reformat(self, s: str) -> str:
        if len(s) == 1:
            print(s)
            return s

        d, c = [], []
        for ch in s:
            if ch.isdigit():
                d.append(ch)
            else:
                c.append(ch)

        if abs(len(d) - len(c)) > 1:
            print('bad')
            return ''

        minlen = min(len(d), len(c))
        res = ''

        if len(d) - len(c) == 1:
            for i in range(minlen):
                res += d[i] + c[i]
            print('more digits than chars')
            res += d[-1]

        elif len(c) - len(d) == 1:
            for i in range(minlen):
                res += c[i] + d[i]
            print('more chars than digits')
            res += c[-1]
        
        elif len(c) == len(d):
            for i in range(minlen):
                res += c[i] + d[i]

        print(res)
        return res
