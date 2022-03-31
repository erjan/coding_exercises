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
