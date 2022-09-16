'''
Given a rectangle of size n x m, return the minimum number of integer-sided squares that tile the rectangle.
'''

class Solution:
    @cache
    def solve(self, x1, y1, x2, y2):
        if y2 > x2:                             # For the cases in the "portrait" direction,  
            return self.solve(y1, x1, y2, x2)   # always rotate them into the "landscape" direction
        elif x2 * y2 == 0:
            return 0
        elif x1 == 0 and y1 == 0 and x2 == y2:
            return 1
        elif y1 == y2:
            return self.solve(0, 0, x2 - x1, y2)
        elif x1 == y1 == 0:
            return min([self.solve(d, d, x2, y2) for d in range(1, y2 + 1)]) + 1
        elif x1 < y2 - y1 < x2:
            return self.solve(y2 - y1, (x2-x1) - (x2 - (y2-y1)), y2, x2-x1) + 1
        elif x1 == y2 - y1:
            return self.solve(0, 0, x2-x1, y2) + 1
        elif x1 > y2 - y1:
            return self.solve(x1 - (y2 - y1), y1, x2 - (y2 - y1), y2) + 1
            
    def tilingRectangle(self, n: int, m: int) -> int:
        return self.solve(0, 0, n, m)
      
-------------------------------------------------------------------------------------------------------------
class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        @cache
        def R(i, j):
            if i == j:
                return 1
            else:
                min_ = math.inf
                
                for l in range(1, i):
                    min_ = min(min_, R(l, j) + R(i - l, j))
                
                for l in range(1, j):
                    min_ = min(min_, R(l, i) + R(j - l, i))
                    
                for k in range(1, j):
                    for l in range(1, i):
                        min_ = min(min_, L(i, j, l, k) + R(l, k))
                        
                return min_
        
        @cache
        def L(i, j, k, l):            
            min_ =  min(R(l, j - k) + R(i - l, j), R(i, j - k) + R(k, i - l))

            for g in range(1, l):
                min_ = min(min_, R(g, j - k) + L(i - g, j, k, l - g))

            for g in range(l + 1, i):
                min_ = min(min_, R(g, j - k) + L(j, i - l, g - l, j - k))
                
            for g in range(1, k):
                min_ = min(min_, R(i - l, g) + L(i, j - g, k - g, l))
            
            
            for g in range(k + 1, j):
                min_ = min(min_, R(i - l, g) + L(i, j - k, g - k, i - l))
            
            return min_
        
        return R(m, n)
