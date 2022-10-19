'''
Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.



We come to two conclusions after analisys (hints are very helpful in this case):
We cannot introduce new characters
List of counts of characters will stay consistent

'''


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Saves some time
        if len(word1) != len(word2):
            return False
        
        from collections import Counter
        counts1 = Counter(word1)
        counts2 = Counter(word2)
        
        # No new chars can appear with operations
        if counts1.keys() != counts2.keys():
            return False
        
        # Counts can be swapped, but they will stay consistent
        if sorted(counts1.values()) != sorted(counts2.values()):
            return False
        
        return True
      
-----------------------------------------------------------------------------------
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        
        
        d1 = Counter(word1)
        d2 = Counter(word2)
        
        w1 = list(word1)
        w2 = list(word2)
        
        w1.sort()
        w2.sort()
        
        if w1 == w2:
            return True
        
        if d1.keys()!= d2.keys():
            return False
        
        if sorted(d1.values()) != sorted(d2.values()):
            return False
        
        return True
