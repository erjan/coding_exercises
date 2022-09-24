'''
You are given a string s that consists of only digits.

Check if we can split s into two or more non-empty substrings such that the numerical values of the substrings are in descending order and the difference between numerical values of every two adjacent substrings is equal to 1.

For example, the string s = "0090089" can be split into ["0090", "089"] with numerical values [90,89]. The values are in descending order and adjacent values differ by 1, so this way is valid.
Another example, the string s = "001" can be split into ["0", "01"], ["00", "1"], or ["0", "0", "1"]. However all the ways are invalid because they have numerical values [0,1], [0,1], and [0,0,1] respectively, all of which are not in descending order.
Return true if it is possible to split s as described above, or false otherwise.

A substring is a contiguous sequence of characters in a string.
'''


class Solution:
    def splitString(self, s: str) -> bool:
        def find_split(cur_idx, n_splits, target):
            if cur_idx == len(s) and n_splits >= 2:
                return True

            val = 0
            for i in range(cur_idx, len(s)):
                val = val * 10 + int(s[i])
                if target is None and val == 0:  # Skip leading 0s.
                    continue
                if target is None or val == target:
                    if find_split(i + 1, n_splits + 1, val - 1):
                        return True
                if target and val > target:  # Early break.
                    break

            return False
    
        return find_split(0, 0, None)
