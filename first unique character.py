#Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        t = Counter(s)
        t = dict(t)
        index = -1
        for i in range(len(s)):
            if t[s[i]] == 1:
                index = i
                break
        return index
