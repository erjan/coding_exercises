'''
There are n employees, each with a unique id from 0 to n - 1.

You are given a 2D integer array logs where logs[i] = [idi, leaveTimei] where:

idi is the id of the employee that worked on the ith task, and
leaveTimei is the time at which the employee finished the ith task. All the values leaveTimei are unique.
Note that the ith task starts the moment right after the (i - 1)th task ends, and the 0th task starts at time 0.

Return the id of the employee that worked the task with the longest time. If there is a tie between two or more employees, return the smallest id among them.
'''


class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        prevTime = 0
        longestTask = 0
        resultid = float("inf")
        for eid, time in logs:
            taskTime = time - prevTime
            # print(taskTime)
            prevTime = time
            if taskTime > longestTask:
                longestTask = taskTime
                resultid = eid
            elif taskTime == longestTask:
                resultid = min(eid, resultid)
                
        return resultid
