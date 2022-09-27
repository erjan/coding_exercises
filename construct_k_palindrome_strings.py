'''
Given a string s and an integer k, return true if you can use all the characters in s to construct k palindrome strings or false otherwise.
'''

from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        h = Counter(s)
        countOdd = 0
        for value in h.values():
            if value % 2:
                countOdd += 1
        if countOdd > k:
            return False
        return True
        
The solution is based on the understanding that a string can be a palindrome only if it has at most 1 character whose frequency is odd. 
So if
the number of characters having an odd frequency is greater than the number of palindromes we need to form, then naturally it's impossible to do so.

---------------------------------------------------------------
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        '''
        For a palindrome, its odd-count character has to be less than or eqaul to one. 
        Then in order to get k many palindromic substrings, the number of odd-count chracters in s has to be less than
        or equal to k '''
        
        if len(s) < k:
            return False
        freq = Counter(s)
        return sum(1 for val in freq.values() if val % 2 != 0) <= k
