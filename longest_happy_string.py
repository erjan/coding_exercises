'''
A string s is called happy if it satisfies the following conditions:

s only contains the letters 'a', 'b', and 'c'.
s does not contain any of "aaa", "bbb", or "ccc" as a substring.
s contains at most a occurrences of the letter 'a'.
s contains at most b occurrences of the letter 'b'.
s contains at most c occurrences of the letter 'c'.
Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.
'''

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        s = [[a, 'a'], [b, 'b'], [c, 'c']]
        ans = []
        while True:
            s.sort()
            i = 1 if len(ans) >= 2 and ans[-2] == ans[-1] == s[2][1] else 2
            if s[i][0]:
                ans.append(s[i][1])
                s[i][0] -= 1
            else:
                break
        return ''.join(ans)
