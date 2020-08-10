'''
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
    '''
    
from string import ascii_uppercase as ups
class Solution:
    def titleToNumber(self, s: str) -> int:
        s = ''.join(reversed(s))
        abc = dict(zip(ups,[i for i in range(1,27)]))  
        res = 0

        for i in range(len(s)):        
            n = 1
            n = 26**i
            n*= abc[s[i]]
            res+= n

        print(res)
        return res
