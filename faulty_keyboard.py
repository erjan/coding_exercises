'''
Your laptop keyboard is faulty, and whenever you type a character 'i' on it, it reverses the string that you have written. Typing other characters works as expected.

You are given a 0-indexed string s, and you type each character of s using your faulty keyboard.

Return the final string that will be present on your laptop screen.
'''


class Solution:
    def finalString(self, s: str) -> str:

        res = ''
        for i in range(len(s)):

            if s[i] != 'i':
                res += s[i]
            else:
                res = res[::-1]
        return res
