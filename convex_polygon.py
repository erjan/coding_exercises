'''

You are given an array of points on the X-Y plane points where points[i] = [xi, yi]. The points form a polygon when joined sequentially.

Return true if this polygon is convex and false otherwise.

You may assume the polygon formed by given points is always a simple polygon. In other words, we ensure that exactly two edges intersect at each vertex and that edges otherwise don't intersect each other.

'''

class Solution:
    def isConvex(self, points: List[List[int]]) -> bool:
        points.append(points[0])
        points.append(points[1])
        s = set()
        for i in range(len(points)-2):
            x1, y1 = points[i]
            x2, y2 = points[i+1]
            x3, y3 = points[i+2]
            z = (x2 - x1)*(y3 - y1) - (y2 - y1)*(x3 - x1)
            if z != 0:
                s.add(z > 0)
        return len(s) == 1
