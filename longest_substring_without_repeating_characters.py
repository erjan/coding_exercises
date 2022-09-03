'''
Given a string s, find the length of the longest substring without repeating characters.
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        r = 0
        res = 0
        seen = set()

        while l < len(s):
            seen.clear()
            r = l
            while r < len(s):
                if s[r] in seen:
                    break
                seen.add(s[r])
                r += 1
            res = max(res, r-l)
            l += 1
        print(res)
        return res
