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
    
------------------------------------------------------------
#bottom up dp
class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        
        dp = [set() for _ in range(len(tasks))]
        
        dp[0].add(tuple([sessionTime - tasks[0]]))
        
        for i in range(1, len(tasks)):
            for prev_session in dp[i-1]:
                dp[i].add(tuple(sorted(list(prev_session) + [sessionTime - tasks[i]])))
                
                for j in range(0, len(prev_session)):
                    if prev_session[j] >= tasks[i]:
                        next_session = list(prev_session) + []
                        next_session[j] -= tasks[i]
                        dp[i].add(tuple(sorted(next_session)))
                        
        ans = len(tasks)
        for x in dp[len(tasks) - 1]:
            ans = min(ans, len(x))
        
        return ans
-----------------------------------------------------------------------------
#top down dp

class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        
        @cache
        def dp(mask_tuple, prev):
            
            if len(mask_tuple) == 0:
                return 1
            
            
            mask_list = list(mask_tuple)
            ans = inf
            
            for i in range(len(mask_list)):
                
                new_tuple = mask_list[:i] + mask_list[i+1:] 
                curr = prev + mask_list[i]
                temp = inf
                
                if curr > sessionTime:
                    # cant take this task. start new session
                    # thiis can lead to inf loop
                    temp = 1 + dp(mask_tuple, 0)
                else:
                    # can include this task in same session
                    temp = dp(tuple(new_tuple), curr)
                
                ans = min(ans, temp)
            
            return ans
                    
        return dp(tuple(tasks), 0)
    
