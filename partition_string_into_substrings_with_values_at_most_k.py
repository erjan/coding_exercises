'''
You are given a string s consisting of digits from 1 to 9 and an integer k.

A partition of a string s is called good if:

Each digit of s is part of exactly one substring.
The value of each substring is less than or equal to k.
Return the minimum number of substrings in a good partition of s. If no good partition of s exists, return -1.

Note that:

The value of a string is its result when interpreted as an integer. For example, the value of "123" is 123 and the value of "1" is 1.
A substring is a contiguous sequence of characters within a string.
'''


class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        curr, ans = 0, 1
        for d in s:
            if int(d) > k:
                return -1
            curr = 10 * curr + int(d)
            if curr > k:
                ans += 1
                curr = int(d)
        return ans
      
-----------------------------------------------------------------------
class Solution:
    def minimumPartition(self, s: str, k: int) -> int:

        if k < 10: return len(s) if k >= int(max(s)) else -1
        
        k, ans = str(k), 0
        digits = len(k)

        while s:
            s = s[digits:] if s[:digits] <= k else s[digits-1:]
            ans+= 1

        return ans
