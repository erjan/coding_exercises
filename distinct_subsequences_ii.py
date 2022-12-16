'''
Given a string s, return the number of distinct non-empty subsequences of s. Since the answer may be very large, return it modulo 109 + 7.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not.
'''

class Solution:
    def distinctSubseqII(self, s: str) -> int:
        freq = [0]*26 
        for i in reversed(range(len(s))): freq[ord(s[i])-97] = (1 + sum(freq)) % 1_000_000_007
        return sum(freq) % 1_000_000_007
