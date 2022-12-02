'''
You are given an array points containing the coordinates of points on a 2D plane, sorted by the x-values, where points[i] = [xi, yi] such that xi < xj for all 1 <= i < j <= points.length. You are also given an integer k.

Return the maximum value of the equation yi + yj + |xi - xj| where |xi - xj| <= k and 1 <= i < j <= points.length.

It is guaranteed that there exists at least one pair of points that satisfy the constraint |xi - xj| <= k.

 
 '''


class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        q = collections.deque()
        res = -float('inf')

        for j in range(0,len(points)):
            while q and points[j][0] - q[0][1] > k:
                q.popleft()
            
            if q:
                res = max(res, q[0][0] + points[j][1] + points[j][0])
            
            while q and q[-1][0] <= points[j][1] - points[j][0]:
                q.pop()
            
            q.append([points[j][1] - points[j][0], points[j][0]])
        
        return res

        
        

# Brute force approach, gives TLE
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        values = []
        
        for i in range(0,len(points)-1):
            for j in range(i+1,len(points)):
                if abs(points[i][0] - points[j][0]) <= k:
                    value_of_eq = points[i][1] + points[j][1] + abs(points[i][0] - points[j][0])
                    values.append(value_of_eq)
        
        return max(values)
