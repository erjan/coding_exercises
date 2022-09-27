'''
Special binary strings are binary strings with the following two properties:

The number of 0's is equal to the number of 1's.
Every prefix of the binary string has at least as many 1's as 0's.
You are given a special binary string s.

A move consists of choosing two consecutive, non-empty, special substrings of s, and swapping them. Two strings are consecutive if the last character of the first string is exactly one index before the first character of the second string.

Return the lexicographically largest resulting string possible after applying the mentioned operations on the string.

 
 '''

class Solution:
    def makeLargestSpecial(self, s: str) -> str:

        l = 0
        balance = 0
        sublist = []
        for r in range(len(s)):
            balance += 1 if s[r]=='1' else -1
            if balance==0:
                sublist.append("1" + self.makeLargestSpecial(s[l+1:r])+ "0")
                l = r+1

        sublist.sort(reverse=True)
        return ''.join(sublist)
