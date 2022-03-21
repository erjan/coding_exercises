'''
Given an array points where points[i] = [xi, yi] represents a point on the X-Y plane, return true if these points are a boomerang.

A boomerang is a set of three points that are all distinct and not in a straight line.

'''

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        
        point1 = points[0]
        point2 = points[1]
        point3 = points[2]

        temp1 = point1[0] * (  point2[1] - point3[1]    )
        temp2 = point2[0] * (  point3[1] - point2[1]    )
        temp3 = point3[0] * (  point1[1] - point2[1]    )

        if temp1 + temp2 + temp3 !=0:
            return True
        return False
