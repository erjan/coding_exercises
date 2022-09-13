'''
You are given an array of points in the X-Y plane points where points[i] = [xi, yi].

Return the minimum area of a rectangle formed from these points, with sides parallel to the X and Y axes. If there is not any such rectangle, return 0.
'''

class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        x_points = defaultdict(list)
        y_points = defaultdict(list)
        
        for point in points:
            x_points[point[0]].append(point[1])
            y_points[point[1]].append(point[0])
            
        min_area = float("inf")
        for x in x_points:
            if not len(x_points[x]) > 1:
                continue
            ys = x_points[x]
            ys.sort()
            for i in range(len(ys)-1):
                y1 = ys[i]
                y2 = ys[i+1]
                y2_xs = set(y_points[y2])
                for y_x in y_points[y1]:
                    if y_x in y2_xs and y_x != x:
                        min_area = min(min_area, abs(y_x - x) * abs(y1-y2))
        return min_area if min_area != float("inf") else 0
