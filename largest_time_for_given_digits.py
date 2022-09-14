'''
Given an array arr of 4 digits, find the latest 24-hour time that can be made using each digit exactly once.

24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59. The earliest 24-hour time is 00:00, and the latest is 23:59.

Return the latest 24-hour time in "HH:MM" format. If no valid time can be made, return an empty string.

 
 '''


from itertools import permutations
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        arr = list(permutations(sorted(A, reverse=True)))
        
        for h1, h2, m1, m2 in arr:
            if h1 * 10 + h2 < 24 and m1 * 10 + m2 < 60:
                return f'{h1}{h2}:{m1}{m2}'
        return ''
-------------------------------------------------------------------
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
# From 23:59 to 00:00 go over every minute of 24 hours. If A meets this requirement, then totaly 24 * 60 minutes. Since using sort during the ongoing judegment process, so the time complexity is low.
        A.sort()
        for h in range(23, -1, -1):
            for m in range(59, -1, -1):
                t = [h//10, h % 10, m // 10, m % 10]
                ts = sorted(t)
                if ts == A:
                    return str(t[0]) + str(t[1]) +':' + str(t[2]) + str(t[3])
        return ''
