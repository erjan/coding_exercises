'''
You are given a 2D integer array rectangles where rectangles[i] = [li, hi] indicates that ith rectangle 
has a length of li and a height of hi. You are also given a 2D integer array points where points[j] = [xj, yj] is a point with coordinates (xj, yj).

The ith rectangle has its bottom-left corner point at the coordinates (0, 0) and its top-right corner point at (li, hi).

Return an integer array count of length points.length where count[j] is the number of rectangles that contain the jth point.

The ith rectangle contains the jth point if 0 <= xj <= li and 0 <= yj <= hi. Note that 
points that lie on the edges of a rectangle are also considered to be contained by that rectangle.
'''


class Solution:
    def countRectangles(self, rect: List[List[int]], points: List[List[int]]) -> List[int]:
        
        hashmap = {}
        for x, y in rect:
            hashmap[y] = hashmap.get(y, []) + [x]
            
        for k in hashmap.keys():
            hashmap[k].sort()
        
        res = []
        for x, y in points:
            ans = 0
            for coord in range(y, 101):
                if coord in hashmap:
                    val = hashmap[coord]
                    ans += len(val) - bisect_left(val, x)
            res.append(ans)
        return res
      
----------------------------------------------------------------------------      
class Solution:
    def countRectangles(self, R, P):
        R.sort()
        dp = [[] for _ in range(101)]
        for l,h in R:
            dp[h].append(l)
        res = []
        for x,y in P:
            count = 0
            for h in range(y,101):
                count += len(dp[h]) - bisect.bisect_left(dp[h], x)
            res.append(count)
        return res
