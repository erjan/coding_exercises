'''
An alphabetical continuous string is a string consisting of consecutive letters in the alphabet. In other words, it is any substring of the string "abcdefghijklmnopqrstuvwxyz".

For example, "abc" is an alphabetical continuous string, while "acb" and "za" are not.
Given a string s consisting of lowercase letters only, return the length of the longest alphabetical continuous substring.
'''



--- At each position, it either belongs to previous continues substring or it is the beginning of a new substring.

class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        cur = 1 ### We are currently at 0 position, so the length is 1.
        res = 1 ### At least the string should contain 1 letter.
        for i in range(1,len(s)):
        	### If the ith letter is continued from the previous letter, 
        	### update the curLength and store the maximum length to res
            if ord(s[i])-ord(s[i-1])==1:
                cur = cur+1
                res = max(cur,res)
            ### This is the start of a new substring with length 1.
            else:
                cur = 1
        return res



