'''
The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.

For example, the beauty of "abaacc" is 3 - 1 = 2.
Given a string s, return the sum of beauty of all of its substrings.
'''

class Solution:
    def beautySum(self, s: str) -> int:
        beauty=0
        for i in range(len(s)-2):
            Freq={}
            for j in range(i,len(s)):
                Freq.setdefault(s[j],0)
                Freq[s[j]]+=1
                beauty+=max(Freq.values())-min(Freq.values())
        return beauty
