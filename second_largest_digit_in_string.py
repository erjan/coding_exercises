'''
Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if it does not exist.

An alphanumeric string is a string consisting of lowercase English letters and digits.
'''

class Solution:
    def secondHighest(self, s: str) -> int:
                
        res = list(filter(lambda x: x.isnumeric(), s))
        res = list(map(lambda x: int(x), res))
        res = list(set(res))
        res = sorted(res, reverse=True)

        print(res)

        if len(res) < 2:
            print('bad -1')
            return -1
        else:
            print(res[1])
            return res[1]
