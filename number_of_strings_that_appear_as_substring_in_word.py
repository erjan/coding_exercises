'''
Given an array of strings patterns and a string word, return the number of strings in patterns that exist as a substring in word.

A substring is a contiguous sequence of characters within a string.
'''

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        p = patterns
        
        c = 0
        for w in p:
            if w in word:
                c += 1
        print(c)
        return c

    
  def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum(i in word for i in patterns)
