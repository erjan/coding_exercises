'''
A set of real numbers can be represented as the union of several disjoint intervals, where each interval is in the form [a, b). A real number x is in the set if one of its intervals [a, b) contains x (i.e. a <= x < b).

You are given a sorted list of disjoint intervals intervals representing a set of real numbers as described above, where intervals[i] = [ai, bi] represents the interval [ai, bi). You are also given another interval toBeRemoved.

Return the set of real numbers with the interval toBeRemoved removed from intervals. In other words, return the set of real numbers such that every x in the set is in intervals but not in toBeRemoved. Your answer should be a sorted list of disjoint intervals as described above.

 
 '''

my simple yet maybe naive solution.
for each interval in the invervals list, there are just 4 senarios:

interval is outside of the toBeRemoved range, append to res
interval intersects with the toBeRemoved on the frond end, only append the [a, toBeRemoved[0]] portion
interval intersects with the toBeRemoved on the back end, only append the [toBeRemoved[1], b] portion
inverval could be bigger than toBeRemoved, in that case, add both front end and the back end portion of the inverval
inverval is in completely in toBeRemoved, do nothing! it is to be removed
then just turn them into 4 if statements.

class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res = []
        for a, b in intervals:
            if b <= toBeRemoved[0] or a >= toBeRemoved[1]:  # out of range
                res.append([a, b])
            elif a < toBeRemoved[0] < b <= toBeRemoved[1]:  # intersect in the front
                res.append([a, toBeRemoved[0]])
            elif toBeRemoved[0] <= a < toBeRemoved[1] < b:  # intersect on the back
                res.append([toBeRemoved[1], b])
            elif a < toBeRemoved[0] and b > toBeRemoved[1]:  # interval is bigger than toBeRemoved
                res.append([a, toBeRemoved[0]])
                res.append([toBeRemoved[1], b])
        return res
--------------------------------------------------------

def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
	x, y = toBeRemoved
	res = []
	for a, b in intervals:
		left, right = max(x, a), min(y, b)
		if right <= left: # no intersection
			res.append([a, b])
			continue
		if a < left: res.append([a, left])
		if b > right: res.append([right, b])
	return res
-------------------------------------------------------------

class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res = []
        
        for s, e in sorted(intervals):
            # Situation 1: no overlaps
            if e < toBeRemoved[0] or s > toBeRemoved[1]:
                res.append([s,e])
            # Situation 2: s-e in toBeRemoved
            # Situation 3: e in [toBeRemoved]
            # Situation 4: s in [toBeRemoved]
            else:
                if s < toBeRemoved[0]:
                    res.append([s, toBeRemoved[0]])
                if e > toBeRemoved[1]:
                    res.append([toBeRemoved[1], e])
        return res

------------------------------------------------------------------------

class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        start = self.bsearchLeft(intervals,toBeRemoved[0])
        last = self.bsearchRight(intervals,toBeRemoved[1])
        if start > last:
            return intervals
        if start == last:
            intv = []
            low, high = toBeRemoved
            curL, curH = intervals[start]
            if curL < low: intv.append([curL,low]) 
            if high < curH: intv.append([high,curH]) 
            return intervals[:start] + intv + intervals[start+1:]
        
        intervals[start][1] = toBeRemoved[0]
        intervals[last][0] = toBeRemoved[1]
        if intervals[start][0] >= intervals[start][1]: start -= 1
        if intervals[last][0] >= intervals[last][1]: last += 1 
        
        return intervals[:start+1] + intervals[last:]
        
        
    
    def bsearchLeft(self, intervals, beg):
        l, r = 0, len(intervals)-1
        while l <= r:
            m = int((l+r)/2)
            if intervals[m][1] > beg: r = m - 1
            else: l = m + 1
        return l
    
    def bsearchRight(self, intervals, last):
        l, r = 0, len(intervals)-1
        while l <= r:
            m = int((l+r)/2)
            if intervals[m][0] > last: r = m - 1
            else: l = m + 1
        return r
----------------------------------------------

class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        output = []
        for interval in intervals:
            if interval[1] <= toBeRemoved[0] or interval[0] >= toBeRemoved[1]:
                output.append(interval)
            elif interval[1] > toBeRemoved[1] and interval[0] < toBeRemoved[0]:
                output.append([interval[0],toBeRemoved[0]])
                output.append([toBeRemoved[1],interval[1]])
            elif interval[1] > toBeRemoved[0] and interval[0] < toBeRemoved[0] :
                output.append([interval[0],toBeRemoved[0]])
            elif interval[0] < toBeRemoved[1] and interval[1] > toBeRemoved[1] :
                output.append([toBeRemoved[1],interval[1]])
        return output
      
      
      

      
