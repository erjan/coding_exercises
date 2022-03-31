

'''
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

'''


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        intervals.sort(key = lambda x: x[0])
        
        for i in range(len(intervals)-1):
            
            first = intervals[i]
            second = intervals[i+1]
            
            if first[1] > second[0]:
                return False
        return True
        
