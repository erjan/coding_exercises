'''
You are given a string s consisting of lowercase English letters, and an integer k.

First, convert s into an integer by replacing each letter with its position in the alphabet (i.e., replace 'a' with 1, 'b' with 2, ..., 'z' with 26). Then, transform the integer by replacing it with the sum of its digits. Repeat the transform operation k times in total.

For example, if s = "zbax" and k = 2, then the resulting integer would be 8 by the following operations:

Convert: "zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124
Transform #1: 262124 ➝ 2 + 6 + 2 + 1 + 2 + 4 ➝ 17
Transform #2: 17 ➝ 1 + 7 ➝ 8
Return the resulting integer after performing the operations described above.
'''

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def transform(n):
            s = 0
            for digit in str(n):
                s += int(digit)
            return s
        
        l = [i for i in range(1, 27)]
        abc = string.ascii_lowercase
        d = dict(zip(abc, l))

        s = list(s)
        for i in range(len(s)):
            s[i] = d[s[i]]

        for i in range(len(s)):
            s[i] = str(s[i])
        s = int(''.join(s))

        res = 0
        i = 0

        while i < k:
            res = transform(s)
            s = res
            i += 1

        print(res)
        return res
