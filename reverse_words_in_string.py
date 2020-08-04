'''
Given an input string, reverse the string word by word.

 

Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
'''



class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join((' '.join(s.split())).split(' ')[::-1])
      
