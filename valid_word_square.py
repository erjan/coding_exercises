'''
Given an array of strings words, return true if it forms a valid word square.

A sequence of strings forms a valid word square if the kth row and column read the same string, where 0 <= k < max(numRows, numColumns).
'''


class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
	    # Iterate each row to check the valid square
        for i, r in enumerate(words):
            c = ''.join([r[i] for r in words if i < len(r)])
            if len(c) != len(r) or c != r:
                return False
            
        return True



#another

class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for index, word in enumerate(words): 
            # Check if kth row word is the same as kth column word
            if not self.match(index, word, words):
                return False
            
        return True
    
    def match(self, index, word, words):
        # Get all the letters at specified index and make into a new word
        new_word = ""
        
        for cur_word in words:
            # Break immediately if we have Index error as not all word length will be the same
            try:
                new_word += cur_word[i]
            except IndexError:
                break
        
        # check if created word matches the original word
        return new_word == word
