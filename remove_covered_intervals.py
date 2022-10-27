'''
Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove all intervals that are covered by another interval in the list.

The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.

Return the number of remaining intervals.
'''

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x : (x[0], -x[1]))
        
        res = 0
        ending = 0
        
        for _, end in intervals:
            if end > ending:
                res += 1
                ending = end
        
        return res
      
------------------------------------------------------------------------------------------
class Solution:
	def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:

		intervals=sorted(intervals)

		i=0
		while i<len(intervals)-1:

				a,b = intervals[i]
				p,q = intervals[i+1]

				if a <= p and q <= b:
					intervals.remove(intervals[i+1])
					i=i-1

				elif p <= a and b <= q:
					intervals.remove(intervals[i])
					i=i-1

				i=i+1
		return len(intervals)
-------------------------------------------------------------------------

class Solution:
    def removeCoveredIntervals(self, new: List[List[int]]) -> int:
        arr=[]
        for i in range(len(new)):
            for j in range(len(new)):
                if i!=j and new[j][0] <= new[i][0] and new[i][1] <= new[j][1]:
                    arr.append(new[i])
                    break
        return len(new)-len(arr)
