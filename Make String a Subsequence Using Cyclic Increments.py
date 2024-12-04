'''
You are given two 0-indexed strings str1 and str2.

In an operation, you select a set of indices in str1, and for each index i in the set, increment str1[i] to the next character cyclically. That is 'a' becomes 'b', 'b' becomes 'c', and so on, and 'z' becomes 'a'.

Return true if it is possible to make str2 a subsequence of str1 by performing the operation at most once, and false otherwise.

Note: A subsequence of a string is a new string that is formed from the original string by deleting some (possibly none) of the characters without disturbing the relative positions of the remaining characters.
'''


class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
            
        def shiftleft(x):

            if x == 'z':
                return 'a'
            
            return chr(ord(x)+1)

        str1 = list(str1)
        str2 = list(str2)

        p1 = 0
        p2 = 0
    
        while p1 < len(str1) and p2<len(str2):
            if str1[p1] == str2[p2] or shiftleft(str1[p1]) == str2[p2]:
                p1+=1
                p2+=1
       
            else:
                p1+=1
        
        #if we reach the end of str2 with pointer 2 - ok
        if p2 == len(str2):
            return True
        return False
      
