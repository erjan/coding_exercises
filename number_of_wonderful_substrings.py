'''
A wonderful string is a string where at most one letter appears an odd number of times.

For example, "ccjjc" and "abab" are wonderful, but "ab" is not.
Given a string word that consists of the first ten lowercase English letters ('a' through 'j'), return the number of wonderful non-empty substrings in word. If the same substring appears multiple times in word, then count each occurrence separately.

A substring is a contiguous sequence of characters in a string.
'''

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        n = len(word)
        mask = 0
        prefix = defaultdict(int)
        prefix[0] += 1
        ans = 0
        for w in word:
            mask ^= 1 << (ord(w) - ord('a'))
            # no difference
            ans += prefix[mask]
            for i in range(10):
                # only differed by one digit 
                tmp = mask ^ (1 << i)
                ans += prefix[tmp]
            prefix[mask] += 1
        return ans
