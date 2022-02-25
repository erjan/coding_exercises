'''
In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.
'''

#my own solution

from collections import Counter
from math import gcd

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        n = deck
        d = Counter(n)
        temp = list(d.values())
        m = min(temp)
        if m < 2:
            return False
        else:
            for i in range(len(temp)-1):
                f1 = temp[i]
                f2 = temp[i+1]
                if gcd(f1,f2) == 1:
                    return False
            return True
        
            
            

      
