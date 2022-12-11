'''
A Range Module is a module that tracks ranges of numbers. Design a data structure to track the ranges represented as half-open intervals and query about them.

A half-open interval [left, right) denotes all the real numbers x where left <= x < right.

Implement the RangeModule class:

RangeModule() Initializes the object of the data structure.
void addRange(int left, int right) Adds the half-open interval [left, right), tracking every real number in that interval. Adding an interval that partially overlaps with currently tracked numbers should add any numbers in the interval [left, right) that are not already tracked.
boolean queryRange(int left, int right) Returns true if every real number in the interval [left, right) is currently being tracked, and false otherwise.
void removeRange(int left, int right) Stops tracking every real number currently being tracked in the half-open interval [left, right).
'''

from sortedcontainers import SortedList

class RangeModule:

    def __init__(self):
        self.intervals = SortedList()

    def addRange(self, left: int, right: int) -> None:
        k = self.intervals.bisect_left([left, right])
        while k < len(self.intervals) and right >= self.intervals[k][0]: 
            right = max(right, self.intervals[k][1])
            self.intervals.pop(k)
        if k and self.intervals[k-1][1] >= left: 
            left = min(left, self.intervals[k-1][0])
            right = max(right, self.intervals[k-1][1])
            self.intervals.pop(k-1)
        self.intervals.add([left, right])

    def queryRange(self, left: int, right: int) -> bool:
        k = self.intervals.bisect_left([left, right])
        return k and self.intervals[k-1][0] <= left < right <= self.intervals[k-1][1] or k < len(self.intervals) and self.intervals[k][0] <= left < right <= self.intervals[k][1] 

    def removeRange(self, left: int, right: int) -> None:
        k = self.intervals.bisect_left([left, right])
        while k < len(self.intervals) and self.intervals[k][0] <= right: 
            if right < self.intervals[k][1]: 
                self.intervals[k][0] = right 
                break 
            else: self.intervals.pop(k)
        if k and left < self.intervals[k-1][1]: 
            if right < self.intervals[k-1][1]: self.intervals.add([right, self.intervals[k-1][1]])
            self.intervals[k-1][1] = left 
            
------------------------------------------------------------------------------------------
class RangeModule:

    def __init__(self):
        self.ranges = []

    def touching_ranges(self, left, right):
        '''find all the ranges that touch interval [left, right]'''
        i, j = 0, len(self.ranges)-1
        step = len(self.ranges) // 2
        while step >= 1:
            while i + step < len(self.ranges) and self.ranges[i+step-1][1] < left:
                i += step
            while j - step >= 0 and self.ranges[j-step+1][0] > right:
                j -= step
            step //= 2
        return i, j
        
    def addRange(self, left: int, right: int) -> None:
        if not self.ranges or self.ranges[-1][1] < left: 
            self.ranges.append((left, right))
            return
        if self.ranges[0][0] > right:
            self.ranges.insert(0, (left, right))
            return
        i, j = self.touching_ranges(left, right)
        self.ranges[i:j+1] = [(min(self.ranges[i][0], left), max(self.ranges[j][1], right))]
        
    def queryRange(self, left: int, right: int) -> bool:
        if not self.ranges: return False
        i, j = self.touching_ranges(left, right)
        return self.ranges[i][0] <= left and right <= self.ranges[i][1]

    def removeRange(self, left: int, right: int) -> None:
        if not self.ranges or self.ranges[0][0] > right or self.ranges[-1][1] < left: return
        i, j = self.touching_ranges(left, right)
        new_ranges = []
        for k in range(i, j+1):
            if self.ranges[k][0] < left:
                new_ranges.append((self.ranges[k][0], left))
            if self.ranges[k][1] > right:
                new_ranges.append((right, self.ranges[k][1]))
        self.ranges[i:j+1] = new_ranges
