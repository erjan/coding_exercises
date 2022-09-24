'''
You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
'''

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.maximum = 0
        
    def backtrack(start,array,s):
        if len(s)==len(set(s)):
            self.maximum = max(self.maximum,len(s))
        else:
            return
        for i in range(start,len(array)):
            backtrack(i+1,array,s + array[i])
            
    backtrack(0,arr,"")
    return self.maximum
