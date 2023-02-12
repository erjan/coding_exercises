'''
You are given two strings s and t.

You are allowed to remove any number of characters from the string t.

The score string is 0 if no characters are removed from the string t, otherwise:

Let left be the minimum index among all removed characters.
Let right be the maximum index among all removed characters.
Then the score of the string is right - left + 1.

Return the minimum possible score to make t a subsequence of s.

A subsequence of a string is a new string that is formed from
the original string by deleting some (can be none) of the 
characters without disturbing the relative positions
of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
'''

class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        suffix = [-1]*len(s)
        j = len(t)-1
        for i in reversed(range(len(s))): 
            if 0 <= j and s[i] == t[j]: j -= 1
            suffix[i] = j 
        ans = j + 1
        j = 0 
        for i, ch in enumerate(s): 
            ans = min(ans, max(0, suffix[i] - j + 1))
            if j < len(t) and s[i] == t[j]: j += 1
        return min(ans, len(t)-j)
