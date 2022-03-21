'''
Given a string s and an integer k, reverse the first k 
characters for every 2k characters counting from the start of the string.

If there are fewer than k characters 
left, reverse all of them. If there are less than 2k but greater than 
or equal to k characters, then reverse the first k characters and leave the other as original.
'''

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s)<(k):return s[::-1]
        if len(s)<(2*k):return (s[:k][::-1]+s[k:])
        return s[:k][::-1]+s[k:2*k]+self.reverseStr(s[2*k:],k)
