'''
You are given an array of points in the X-Y plane points where points[i] = [xi, yi].

Return the minimum area of any rectangle formed from these points, with sides not necessarily parallel to the X and Y axes. If there is not any such rectangle, return 0.

Answers within 10-5 of the actual answer will be accepted.
'''

class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        ans = inf
        seen = {}
        for i, (x0, y0) in enumerate(points):
            for x1, y1 in points[i+1:]:
                cx = (x0 + x1)/2
                cy = (y0 + y1)/2
                d2 = (x0 - x1)**2 + (y0 - y1)**2
                for xx, yy in seen.get((cx, cy, d2), []): 
                    area = sqrt(((x0-xx)**2 + (y0-yy)**2) * ((x1-xx)**2 + (y1-yy)**2))
                    ans = min(ans, area)
                seen.setdefault((cx, cy, d2), []).append((x0, y0))
        return ans if ans < inf else 0
