'''
We can scramble a string s to get a string t using the following algorithm:

If the length of the string is 1, stop.
If the length of the string is > 1, do the following:
Split the string into two non-empty substrings at a random index, i.e., if the string is s, divide it to x and y where s = x + y.
Randomly decide to swap the two substrings or to keep them in the same order. i.e., after this step, s may become s = x + y or s = y + x.
Apply step 1 recursively on each of the two substrings x and y.
Given two strings s1 and s2 of the same length, return true if s2 is a scrambled string of s1, otherwise, return false.
'''

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @lru_cache(None)
        def dp(i, j, length):
            if length == 1:
                return s1[i] == s2[j]
            
            for size in range(1, length):
                """
                    [Optional]  Breaking s1[i...i + length - 1] into  
                                s1[i...i + size - 1]                     size
                                s1[i + size....i + length - 1]           length - size

                                s2[j + length - size....j + length - 1]  size
                                s2[j....j + length - size - 1]           length - size
                """
                if (dp(i, j + length - size, size) and dp(i + size, j, length - size)) or (dp(i, j, size) and dp(i + size, j + size, length - size)):
                    return True 
                
            return False
        
        return dp(0, 0, len(s1))
