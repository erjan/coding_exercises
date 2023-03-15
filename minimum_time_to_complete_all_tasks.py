'''
There is a computer that can run an unlimited number of tasks at the same time. You are given a 2D integer array tasks where tasks[i] = [starti, endi, durationi] indicates that the ith task should run for a total of durationi seconds (not necessarily continuous) within the inclusive time range [starti, endi].

You may turn on the computer only when it needs to run a task. You can also turn it off if it is idle.

Return the minimum time during which the computer should be turned on to complete all tasks.
'''


class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        tasks = sorted(tasks,key=lambda x:x[1])
        chosen_set = set()
        for task in tasks:
            cur_start,cur_end,cur_duration = task[0],task[1],task[2]
            for time in chosen_set:
                if time >= cur_start and time <=cur_end:
                    cur_duration-=1
                if cur_duration==0:
                    break
            while cur_duration>0:
                if cur_end not in chosen_set:
                    chosen_set.add(cur_end)
                    cur_duration-=1
                cur_end-=1
        return len(chosen_set)
                    
        
-------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        
        tasks.sort(key = lambda x:(x[1],x[0]))
        
        times = [False]*2001
        
        for start, end, duration in tasks:
            dur,e = duration,end
            for s in range(start,end+1):
                if times[s]:
                    dur -= 1
                    
            while dur > 0:
                if not times[e]:
                    times[e] = True
                    dur -= 1
                e -= 1
        
        return sum(times)
--------------------------------------------------------------------------------------------------
class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        runSet = set()
        tasks.sort(key = lambda x: [x[1], x[0], -x[2]])
        for i, v in enumerate(tasks):
            start, end, duration = v
            run = end
            while duration > 0:
                if run not in runSet:
                    runSet.add(run)
                    duration -= 1
                    for j in range(i + 1, len(tasks)):
                        if tasks[j][0] <= run:
                            tasks[j][2] -= 1
                run -= 1
        return len(runSet)
