'''
Given a string s, return the number of substrings that have only one distinct letter.
'''


class Solution:
    def countLetters(self, s: str) -> int:
            count = 0
            for i in range(len(s)):

                for j in range(i, len(s)):

                    substr = s[i:j+1]
                    if len(set(substr)) == 1:
                        count += 1
            print(count)
            return count
