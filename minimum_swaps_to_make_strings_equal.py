'''
You are given two strings s1 and s2 of equal length consisting of letters "x" and "y" only. Your task is to make these two strings equal to each other. You can swap any two characters that belong to different strings, which means: swap s1[i] and s2[j].

Return the minimum number of swaps required to make s1 and s2 equal, or return -1 if it is impossible to do so.
'''

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy = yx = 0
        for c1, c2 in zip(s1, s2):
            if c1 == 'x' and c2 == 'y':
                xy += 1
            elif c1 == 'y' and c2 == 'x':
                yx += 1
        
        if (xy + yx) % 2:
            return -1
        
        return xy // 2 + yx // 2 + (xy % 2) * 2
      
------------------------------------------------------------------------------------

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        h = defaultdict(int)
        count = 0    # variable to keep track of the number of mismatches; it is impossible to make strings equal if count is odd
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
                h[s1[i]] += 1
        if count % 2 != 0:     
            return -1
        res, a, b = 0, h['x'], h['y']
        res += a // 2 + b // 2
        if a % 2 == 0:
            return res
        return res + 2
----------------------------------------------------------------------------------------------
"""
yy    y\  y    x y
xx  = x \ x  = x y
(2pairs)       1 swap == countofyxpairs//2


xx    x\  x    y x
yy  = y \ y  = y x
(2pairs)       1 swap == countofxypairs//2


yyy    y\  y  y   x y  + y
xxx  = x \ x  x = x y    x
(2pairs + 1 pair)       1 swap  ... countofyxpairs//2 +countofyxpairs%2


xxx    x\  x x    y x  + x
yyy  = y \ y y =  y x    y
(2pairs + 1 pair)       1 swap   ... countofxypairs//2 +countofxypairs%2


if only countofyxpairs%2 == 1 or countofxypairs%2 ==1 then we can't do it == -1

if both countofyxpairs%2 == 1 AND countofxypairs%2 ==1 then we can do it:

y x    y x     y y   y \   y   x y
x y. = x |  =  x x = x   \ x  =x y
         y
         
         so 2 moves
"""
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy, yx = 0, 0
        for c1, c2 in zip(s1, s2):
            if c1=='x' and c2=='y':
                xy += 1
            elif c1=='y' and c2=='x':
                yx += 1
        if (xy%2 + yx%2)%2==1: #if sum is odd meaning that we have 1 additional x-y, solution is not possible.
            return -1
        return (xy//2 + yx//2 + xy%2 + yx%2)
      
