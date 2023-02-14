'''
You are given a binary string s and a positive integer k.

You can apply the following operation on the string any number of times:

Choose any substring of size k from s and flip all its characters, that is, turn all 1's into 0's, and all 0's into 1's.
Return the number of distinct strings you can obtain. Since the answer may be too large, return it modulo 109 + 7.

Note that:

A binary string is a string that consists only of the characters 0 and 1.
A substring is a contiguous part of a string.
'''




Flipping s[i:i+k] means flip substring starting from 'i', with length of 'k'.
Content of 's' doesn't matter. By flipping s[i:i+k], you are guaranteed to get a different string. No duplicate as long as you don't flip s[i:i+k] again.
For each 'i', we can choose to flip or not flip it, totally 2^(len(s)-k+1) ways.

    def countDistinctStrings(self, s: str, k: int) -> int:
        return pow(2,len(s)-k+1,10**9+7)
    
--------------------------------------------------------------
class Solution:
    def countDistinctStrings(self, s, k):
        n = len(s)
        return pow(2,(n-k+1),10**9+7)
        

