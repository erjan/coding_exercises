'''
Given a string s, consider all duplicated substrings: (contiguous) substrings of s that occur 2 or more times. The occurrences may overlap.

Return any duplicated substring that has the longest possible length. If s does not have a duplicated substring, the answer is "".
'''


class Solution:
    def longestDupSubstring(self, s: str) -> str:
        """
            This problem can be solved using Sliding Window Technique.
            Logic:
                1. Iterate over the string from 0th index
                2. For each index, define a window of 1 initially.
                3. Check for the existence of the window in the remaining string:
                    a. If found, increase the size of window by 1 and repeat.
                    b. Else Goto next index. For next index, the size window will not start by 1 again as we have already found for 1. So for every next index, size of window will start from the size at previous index to avoid checking for repeating size.
        """
        ans = ""
        j   = 1
        for i in range(len(s)):
            window = s[i:i+j]
            heystack = s[i+1:]
            while window in heystack:
                ans = window
                j += 1
                window = s[i:i+j]
        return ans
