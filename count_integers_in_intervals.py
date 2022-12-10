'''
Given an empty set of intervals, implement a data structure that can:

Add an interval to the set of intervals.
Count the number of integers that are present in at least one interval.
Implement the CountIntervals class:

CountIntervals() Initializes the object with an empty set of intervals.
void add(int left, int right) Adds the interval [left, right] to the set of intervals.
int count() Returns the number of integers that are present in at least one interval.
Note that an interval [left, right] denotes all the integers x where left <= x <= right.
'''

from sortedcontainers import SortedList

class CountIntervals:

    def __init__(self):
        self.cnt = 0 
        self.intervals = SortedList()

    def add(self, left, right):
        k = self.intervals.bisect_left((left - 1, right))
        while k < len(self.intervals) and self.intervals[k][1] <= right: 
            r, l = self.intervals.pop(k)
            self.cnt -= r - l + 1
            right = max(right, r)
            left = min(left, l)
            
        self.cnt += right - left + 1
        self.intervals.add((right, left))

    def count(self):
        return self.cnt
      
--------------------------------------------------------------------------------------------------
from sortedcontainers import SortedDict

class CountIntervals(object):

    def __init__(self):
		# { right -> left } sorted by key (right end of the interval)
        self.d = SortedDict()
        # sum of all merged intervals == number of integers that are present in at least one interval.
        self.cnt = 0 

    def add(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: None
        """
        # Find the first interval whose key >= left, i.e. whose right end >= left
        i = self.d.bisect_left(left)
        # iterate all the intervals covered or partially covered by [left, right] 
        while i < len(self.d) and self.d.values()[i] <= right:
            r, l = self.d.items()[i]
            # Merge interval into a new larger interal:
            left = min(left, l)
            right = max(right, r)
            # Subtracting the sum of merged smaller interval
            self.cnt -= r - l + 1
            # deleted the merged smaller interval from the SortedDict
            self.d.popitem(i)
        
        # Adding by the sum of merged larger interval
        self.cnt += right - left + 1
        # Add the new merged interval 
        self.d[right] = left

    def count(self):
        """
        :rtype: int
        """
        return self.cnt
      

# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()
