'''
Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no points are inside the area.

A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.

Note that points on the edge of a vertical area are not considered included in the
'''

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        mx = 0
        for i in range(len(points) - 1):
            temp = points[i + 1][0] - points[i][0]
            if temp > mx:
                mx = temp
        return mx
      
--------------------------------------
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        # only taking x-axis point as it's relevant
        arr = [i[0] for i in points]
        
        arr.sort()
        
        diff = -1
        for i in range(1, len(arr)):
            diff = max(diff, arr[i] - arr[i - 1])
        
        return diff
