'''
You are given two arrays of strings that represent two inclusive events that happened on the same day, event1 and event2, where:

event1 = [startTime1, endTime1] and
event2 = [startTime2, endTime2].
Event times are valid 24 hours format in the form of HH:MM.

A conflict happens when two events have some non-empty intersection (i.e., some moment is common to both events).

Return true if there is a conflict between two events. Otherwise, return false.
'''

class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        start1 = int(event1[0][:2]) * 60 + int(event1[0][3:])
        end1 = int(event1[1][:2]) * 60 + int(event1[1][3:])
        start2 = int(event2[0][:2]) * 60 + int(event2[0][3:])
        end2 = int(event2[1][:2]) * 60 + int(event2[1][3:])
        return True if start1 <= start2 <= end1 or start2 <= start1 <= end2 else False
