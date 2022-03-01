'''
Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).
'''

#my own solution

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        check = high - low+1
        
        if check %2 == 0:
            return check//2
        
        if high - low == 0:
            if high %2 == 1:
                return 1
            else:
                return 0
        elif high - low == 1:
            return 1
        
        elif check %2 == 1:
            
            if low %2 == 0:
                return check//2
            
            elif low %2 == 1:
                return check//2+1
