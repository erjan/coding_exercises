'''
You are given a string s consisting of the characters 'a', 'b', and 'c' and a non-negative integer k. Each minute, you may take either the leftmost character of s, or the rightmost character of s.

Return the minimum number of minutes needed for you to take at least k of each character, or return -1 if it is not possible to take k of each character.
'''

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        limits = {c: s.count(c) - k for c in 'abc'}
        if any(x < 0 for x in limits.values()):
            return -1

        cnts = {c: 0 for c in 'abc'}
        ans = l = 0
        for r, c in enumerate(s):
            cnts[c] += 1
            while cnts[c] > limits[c]:
                cnts[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)

        return len(s) - ans
