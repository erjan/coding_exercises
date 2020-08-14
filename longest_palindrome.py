'''
Given a string which consists of lowercase or uppercase letters, find the length of the 
longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.
'''


class Solution:
    def longestPalindrome(self, s: str) -> int:
        print('len of s is %d' % len(s))
        c = Counter(s)

        c = dict(c)
        res = 0
        one_possible = False
        for k,v in c.items():
            if v % 2 == 0:
                res += v
            elif v % 2 != 0 and one_possible == False:
                one_possible = True
                res+=v
            elif v%2 != 0 and one_possible:
                res+= v-1
        return res

