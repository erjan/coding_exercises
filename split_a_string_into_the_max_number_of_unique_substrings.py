'''
Given a string s, return the maximum number of unique substrings that the given string can be split into.

You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique.

A substring is a contiguous sequence of characters within a string.
'''


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n, seen = len(s), set()

        def dfs(i) -> int:
            if i == n:
                return 0

            output = 0

            for j in range(i + 1, n + 1):
                sub_str = s[i:j]

                if sub_str not in seen:
                    seen.add(sub_str)
                    output = max(output, 1 + dfs(j))
                    seen.remove(sub_str)

            return output

        return dfs(0)
