'''
You are given two integers, x and y, which represent your current location 
on a Cartesian grid: (x, y). You are also given an array points where each points[i] = [ai, bi] represents 
that a point exists at (ai, bi). A point is valid if it shares the same x-coordinate or the same y-coordinate as your location.

Return the index (0-indexed) of the valid point with the smallest Manhattan 
distance from your current location. If there are multiple, return the valid 
point with the smallest index. If there are no valid points, return -1.

The Manhattan distance between two points (x1, y1) and (x2, y2) is abs(x1 - x2) + abs(y1 - y2).
'''

#my own solution

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        def man_dist(p, x, y):
            res = abs(x-p[0]) + abs(y-p[1])
            return res
        
        valid = list()
        for p in points:

            if p[0] == x or p[1] == y:
                valid.append([p, points.index(p)])
        if len(valid) == 0:
            print('bad')
            return -1

        min_dist = float('inf')
        for i in range(len(valid)):

            point = valid[i]
            dist = man_dist(point[0], x, y)
            if dist < min_dist:
                min_dist = dist
            valid[i] = [dist,  valid[i][1]]
        res = list()
        for i in range(len(valid)):
            if valid[i][0] == min_dist:
                res.append(valid[i])

        del points, min_dist, valid

        res.sort(key=lambda x: x[1])
        print(res)
        res = res[0][1]
        print(res)
        return res

      
#another better solution

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        minDist = math.inf
        ans = -1
        for i in range(len(points)):
            if points[i][0]==x or points[i][1]==y:
                manDist = abs(points[i][0]-x)+abs(points[i][1]-y)
                if manDist<minDist:
                    ans = i
                    minDist = manDist
        return ans
