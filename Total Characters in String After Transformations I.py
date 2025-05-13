'''
You are given a string s and an integer t, representing the number of transformations to perform. In one transformation, every character in s is replaced according to the following rules:

If the character is 'z', replace it with the string "ab".
Otherwise, replace it with the next character in the alphabet. For example, 'a' is replaced with 'b', 'b' is replaced with 'c', and so on.
Return the length of the resulting string after exactly t transformations.

Since the answer may be very large, return it modulo 109 + 7.
'''

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        
        m = 10**9+7
        n = len(s)

        d = dict()
        d['z'] = 'ab'
        res = ''
        for i in range(t):
            if s[i]!= 'z':
                res += chr(ord(s[i]) + 1)
            else:
                res += 'ab'
        return len(res)


-----------------------------------------------------------------------------------------
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        cnt = [0] * 26
        res = len(s)
        z = 25
        
        for c in s:
            cnt[ord(c) - ord('a')] += 1
        
        for _ in range(t):
            res = (res + cnt[z]) % MOD
            cnt[(z + 1) % 26] = (cnt[(z + 1) % 26] + cnt[z]) % MOD
            z = (z + 25) % 26
        
        return res
