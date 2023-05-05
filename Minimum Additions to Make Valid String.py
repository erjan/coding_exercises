'''
Given a string word to which you can insert letters "a", "b" or "c" anywhere and any number of times, return the minimum 
number of letters that must be inserted so that word becomes valid.

A string is called valid if it can be formed by concatenating the string "abc" several times.
'''

class Solution:
    def addMinimum(self, word: str) -> int:
        it = 0
        result = 0
        while it < len(word) :
            if word[it:it+3] == "abc":
                it += 3  
            elif word[it:it+2] in ["ab","ac","bc"]:
                result += 1
                it += 2
            else:
                result += 2
                it += 1
        return result
                    
