'''
Rationale
Complete the task if the wait time is lower than the current day. Put the next day for it. Otherwise, skip the days to the time where it can be completed
We could use a Hash table to see when we're allowed to do the task
'''

class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        next_day = defaultdict(int)
        days = 1
        
        for task in tasks:
            if next_day[task] <= days:
                next_day[task] = days + space + 1
                days += 1
            else:    
                days += next_day[task] - days + 1
                next_day[task] = days + space
        
        return days - 1
