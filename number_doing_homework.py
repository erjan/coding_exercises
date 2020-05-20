'''
Given two integer arrays startTime and endTime and given an integer queryTime.

The ith student started doing their homework at the time startTime[i] and finished it at time endTime[i].

Return the number of students doing their homework at time queryTime. More formally, return the number of students where queryTime lays in the interval [startTime[i], endTime[i]] inclusive.
'''


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        
        intervals = list(zip(startTime, endTime))
        counter = 0
        for i in range(len(intervals)):
            if queryTime >= intervals[i][0] and queryTime <= intervals[i][1]:
                counter+=1
        return counter
