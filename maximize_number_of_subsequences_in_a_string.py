'''
You are given a 0-indexed string text and another 0-indexed string pattern of length 2, both of which consist of only lowercase English letters.

You can add either pattern[0] or pattern[1] anywhere in text exactly once. Note that the character can be added even at the beginning or at the end of text.

Return the maximum number of times pattern can occur as a subsequence of the modified text.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.
'''

    def maximumSubsequenceCount(self, text, pattern):
        res = cnt1 = cnt2 = 0
        for c in text:
            if c == pattern[1]:
                res += cnt1
                cnt2 += 1
            if c == pattern[0]:
                cnt1 += 1
        return res + max(cnt1, cnt2)
      
--------------------------------------------------------------------
class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        total = count_a = count_b = 0
        for c in text:
            if c == pattern[1]:
                total += count_a
                count_b += 1
            if c == pattern[0]:
                count_a += 1
        
        return total + max(count_a, count_b)
