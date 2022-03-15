'''
Given an array of points on the X-Y 
plane points where points[i] = [xi, yi], return the area of the 
largest triangle that can be formed by any three different points. Answers within 10-5 of the actual answer will be accepted.
'''

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:                
        def area(a,b,c):            
            # ax(by-cy) + bx(ay-cy) + cx(ay-by)//2
            return abs( a[0] * (b[1]-c[1]) + b[0]*(c[1]-a[1]) + c[0]*(a[1]- b[1]))/2                
        
        triples = combinations(points,3)        
        m = 0        
        for tr in triples:
            
            cur_area = area(*tr)
            
            if cur_area > m:
                m = cur_area
        return m
            
            
