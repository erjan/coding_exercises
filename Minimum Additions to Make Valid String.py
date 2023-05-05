'''
Given a string word to which you can insert letters "a", "b" or "c" anywhere and any number of times, return the minimum 
number of letters that must be inserted so that word becomes valid.

A string is called valid if it can be formed by concatenating the string "abc" several times.
'''

class Solution:
    def addMinimum(self, word: str) -> int:
        
        res = 0
        i = 0
        while i < len(word):

            if word[i:i+3]=='abc':
                i+=3
            elif word[i:i+2] == 'ab' or word[i:i+2] == 'bc' or word[i:i+2]=='ac':
                i+=2
                res+=1
            else:
                i+=1
                res+=2
        
        return res
