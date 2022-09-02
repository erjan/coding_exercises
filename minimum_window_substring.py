'''
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.
'''


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window_start, matched = 0, 0
        min_length_window = s
        min_length = len(s) + 1
        char_frequencies = {}

        for char in t:
            if char not in char_frequencies:
                char_frequencies[char] = 0
            char_frequencies[char] += 1

        for window_end in range(len(s)):
            right_char = s[window_end]
            if right_char in char_frequencies:
                char_frequencies[right_char] -= 1
                if char_frequencies[right_char] == 0:
                    matched += 1

            while matched == len(char_frequencies):
                if window_end - window_start + 1 < min_length:
                    min_length_window = s[window_start:window_end + 1]
                    min_length = len(min_length_window)

                left_char = s[window_start]
                window_start += 1
                if left_char in char_frequencies:
                    if char_frequencies[left_char] == 0:
                        matched -= 1
                    char_frequencies[left_char] += 1

        if min_length == len(s) + 1: return ""

        return min_length_window
