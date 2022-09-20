'''
There are n tasks assigned to you. The task times are represented as an integer array tasks of length n, where the ith task takes tasks[i] hours to finish. A work session is when you work for at most sessionTime consecutive hours and then take a break.

You should finish the given tasks in a way that satisfies the following conditions:

If you start a task in a work session, you must complete it in the same work session.
You can start a new task immediately after finishing the previous one.
You may complete the tasks in any order.
Given tasks and sessionTime, return the minimum number of work sessions needed to finish all the tasks following the conditions above.

The tests are generated such that sessionTime is greater than or equal to the maximum element in tasks[i].
'''


class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        def process_task(idx_task, buckets):
            if idx_task == len(tasks):
                return True
            for i in range(len(buckets)):
                if buckets[i] + tasks[idx_task] <= sessionTime:
                    buckets[i] += tasks[idx_task]
                    if process_task(idx_task + 1, buckets):
                        return True
                    buckets[i] -= tasks[idx_task]
                    if buckets[i] == 0:
                        return False
            return False

        def possible(num_buckets):
            buckets = [0 for _ in range(num_buckets)]
            buckets[0] = tasks[0]
            return process_task(1, buckets)
        
        tasks.sort(reverse=True)
        
        l, r = max(1, sum(tasks) // sessionTime), len(tasks)

        while l < r:
            m = (l + r) // 2
            
            if possible(m):
                r = m
            else:
                l = m + 1

        return l
