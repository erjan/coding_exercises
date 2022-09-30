'''
You are given a string s of length n containing only four kinds of characters: 'Q', 'W', 'E', and 'R'.

A string is said to be balanced if each of its characters appears n / 4 times where n is the length of the string.

Return the minimum length of the substring that can be replaced with any other string of the same length to make s balanced. If s is already balanced, return 0.
'''

class Solution:
    def balancedString(self, s):
        count = collections.Counter(s)
        res = n = len(s)
        if all(n/4==count[char] for char in 'QWER'):
            return 0
        left = 0
        for right, char in enumerate(s):
            # replace char whose index==right to check if it is balanced
            count[char] -= 1
			# if it is balanced, window shrinks to get the smallest length of window
            while left <= right and all(n / 4 >= count[char] for char in 'QWER'):
                res = min(res, right - left + 1)
                count[s[left]] =count[s[left]]+ 1
                left += 1
        return res
