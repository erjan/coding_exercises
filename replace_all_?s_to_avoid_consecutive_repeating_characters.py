'''
Given a string s containing only lowercase English letters and the '?' character, convert all the '?' characters into lowercase letters such that the final string does not contain any consecutive repeating characters. You cannot modify the non '?' characters.

It is guaranteed that there are no consecutive repeating characters in the given string except for '?'.

Return the final string after all the conversions (possibly zero) have been made. If there is more than one solution, return any of them. It can be shown that an answer is always possible with the given constraints.
'''

class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)

        for i in range(len(s)):

            if s[i] == '?':
                for c in "abc":
                    if (i == 0 or s[i-1] != c) and (i+1 == len(s) or s[i+1] != c):
                        s[i] = c
                        break
        res = ''.join(s)
        print(res)
        return res
