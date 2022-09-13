'''
You are given a circle represented as (radius, xCenter, yCenter) and an axis-aligned rectangle represented as (x1, y1, x2, y2), where (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the top-right corner of the rectangle.

Return true if the circle and rectangle are overlapped otherwise return false. In other words, check if there is any point (xi, yi) that belongs to the circle and the rectangle at the same time.
'''

class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        """
        T(n) = O(1)
        S(n) = O(1)
        """
        # Case 1: center is inside of rect
        if x1 <= x_center <= x2 and y1 <= y_center <= y2:
            return True
        
        # Case 2: center is outside but x or y coord is inside [x1, x2] or [y1, y2]
        d1 = self.dist_to_edge(x1, x_center)
        d2 = self.dist_to_edge(x2, x_center)
        d3 = self.dist_to_edge(y1, y_center)
        d4 = self.dist_to_edge(y2, y_center)
        if x1 <= x_center <= x2:
            return radius >= d3 or radius >= d4
        elif y1 <= y_center <= y2:
            return radius >= d1 or radius >= d2
        
        # Case 3: center is outside and coord is also outside both rect ranges
        d2c1 = self.dist_to_corner((x_center, y_center), (x1, y1))
        d2c2 = self.dist_to_corner((x_center, y_center), (x1, y2))
        d2c3 = self.dist_to_corner((x_center, y_center), (x2, y1))
        d2c4 = self.dist_to_corner((x_center, y_center), (x2, y2))
        return any(radius > d2c for d2c in [d2c1, d2c2, d2c3, d2c4])

    def dist_to_edge(self, x1, x2):
        return abs(x1 - x2)
    
    def dist_to_corner(self, p1, p2):
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
      
-----------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def checkOverlap(self, r: int, xc: int, yc: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        
        if xc >= x1 and xc <= x2 and yc >= y1 and yc <= y2:
            return True
        
        elif xc > x2:
            if yc > y2:
                return r**2 >= (xc-x2)**2 + (yc-y2)**2
            elif yc >= y1 and yc < y2:
                return r >= xc-x2
            else: # yc < y1
                return r**2 >= (xc-x2)**2 + (yc-y1)**2
        elif xc <= x1:
            if yc > y2:
                return r**2 >= (xc-x1)**2 + (yc-y2)**2
            elif yc >= y1 and yc < y2:
                return r >= x1-xc
            else: # yc < y1
                return r**2 >= (xc-x1)**2 + (yc-y1)**2
        elif xc > x1 and xc < x2 and yc > y2:
            
            return r >= yc -y2
        else: 
            return r >= y1-yc
