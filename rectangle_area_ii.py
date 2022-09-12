'''
You are given a 2D array of axis-aligned rectangles. Each rectangle[i] = [xi1, yi1, xi2, yi2] denotes the ith rectangle where (xi1, yi1) are the coordinates of the bottom-left corner, and (xi2, yi2) are the coordinates of the top-right corner.

Calculate the total area covered by all rectangles in the plane. Any area covered by two or more rectangles should only be counted once.

Return the total area. Since the answer may be too large, return it modulo 109 + 7.
'''

class SegmentTree:
    def __init__(self, xs):
        self.cnts = defaultdict(int)
        self.total = defaultdict(int)
        self.xs = xs

    def update(self, v, tl, tr, l, r, h):
        if l > r: return
        if l == tl and r == tr:
            self.cnts[v] += h
        else:
            tm = (tl + tr)//2
            self.update(v*2, tl, tm, l, min(r, tm), h)
            self.update(v*2+1, tm+1, tr, max(l, tm+1), r, h)
          
        if self.cnts[v] > 0:
            self.total[v] = self.xs[tr + 1] - self.xs[tl]
        else:
            self.total[v] = self.total[v*2] + self.total[v*2+1]
        return self.total[v]
    
class Solution:
    def rectangleArea(self, rectangles):
        xs = sorted(set([x for x1, y1, x2, y2 in rectangles for x in [x1, x2]]))
        xs_i = {x:i for i, x in enumerate(xs)}

        STree = SegmentTree(xs)
        L = []
        for x1, y1, x2, y2 in rectangles:
            L.append([y1, 1, x1, x2])
            L.append([y2, -1, x1, x2])
        L.sort()

        cur_y = cur_x_sum = area = 0
        
        for y, op_cl, x1, x2 in L:
            area += (y - cur_y) * cur_x_sum
            cur_y = y
            STree.update(1, 0,  len(xs) - 1, xs_i[x1], xs_i[x2]-1, op_cl)
            cur_x_sum = STree.total[1]
            
        return area % (10 ** 9 + 7)
      
--------------------------------------------------------------------------------------------------------
def rectangleArea(self, rectangles):
        xs = sorted(set([x for x1, y1, x2, y2 in rectangles for x in [x1, x2]]))
        x_i = {v: i for i, v in enumerate(xs)}
        count = [0] * len(x_i)
        L = []
        for x1, y1, x2, y2 in rectangles:
            L.append([y1, x1, x2, 1])
            L.append([y2, x1, x2, -1])
        L.sort()
        cur_y = cur_x_sum = area = 0
        for y, x1, x2, sig in L:
            area += (y - cur_y) * cur_x_sum
            cur_y = y
            for i in range(x_i[x1], x_i[x2]):
                count[i] += sig
            cur_x_sum = sum(x2 - x1 if c else 0 for x1, x2, c in zip(xs, xs[1:], count))
        return area % (10 ** 9 + 7)
      
-------------------------------------------------------------------------------------
 def rectangleArea(self, rectangles):
        xs = sorted(set([x for x1, y1, x2, y2 in rectangles for x in [x1, x2]]))
        x_i = {v: i for i, v in enumerate(xs)}
        count = [0] * len(x_i)
        L = []
        for x1, y1, x2, y2 in rectangles:
            L.append([y1, x1, x2, 1])
            L.append([y2, x1, x2, -1])
        L.sort()
        cur_y = cur_x_sum = area = 0
        for y, x1, x2, sig in L:
            area += (y - cur_y) * cur_x_sum
            cur_y = y
            for i in range(x_i[x1], x_i[x2]):
                count[i] += sig
            cur_x_sum = sum(x2 - x1 if c else 0 for x1, x2, c in zip(xs, xs[1:], count))
        return area % (10 ** 9 + 7)
      
---------------------------------------------------------------------------------------
class Solution(object):
    def rectangleArea(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        events = {}
        for x1, y1, x2, y2 in rectangles:
            events.setdefault(y1, []).append((1, x1, x2)) # start this interval
            events.setdefault(y2, []).append((0, x1, x2)) # end this interval

        events = sorted(events.items(), key=lambda x: x[0])
        area = 0
        intervals = [] # blist.sortedlist()
        last_y = events[0][0]
        width = 0
        for y, event in events:
            area += width * (y - last_y)

            for start, x1, x2 in event:
                if start:
                    intervals.append((x1, x2))
                else:
                    intervals.remove((x1, x2))

            width = self.merge_interval(intervals)
            last_y = y

        return area % (10**9 + 7)

    def merge_interval(self, intervals):
        if not intervals:
            return 0

        intervals.sort()
        end = intervals[0][1]
        total = intervals[0][1] - intervals[0][0]
        for l, r in intervals:
            if l < end and r > end:
                total += r - end
                end = r

            if l >= end:
                total += r - l
                end = r

        return total
