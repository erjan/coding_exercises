'''
You have n tasks and m workers. Each task has a strength requirement stored in a 0-indexed integer array tasks, with the ith task requiring tasks[i] strength to complete. The strength of each worker is stored in a 0-indexed integer array workers, with the jth worker having workers[j] strength. Each worker can only be assigned to a single task and must have a strength greater than or equal to the task's strength requirement (i.e., workers[j] >= tasks[i]).

Additionally, you have pills magical pills that will increase a worker's strength by strength. You can decide which workers receive the magical pills, however, you may only give each worker at most one magical pill.

Given the 0-indexed integer arrays tasks and workers and the integers pills and strength, return the maximum number of tasks that can be completed.
'''


class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        
        from sortedcontainers import SortedList
        
        tasks.sort()
        workers.sort()
        
        def check_valid(ans):
            
            # _tasks = SortedList(tasks[:ans])
            _tasks = deque(tasks[:ans])
            _workers = workers[-ans:]
            remain_pills = pills
            
            for worker in _workers:
                task = _tasks[0]
                if worker >= task:
                    # the worker can finish the min task without pill, just move on
                    # _tasks.pop(0)
                    _tasks.popleft()
                elif worker + strength >= task and remain_pills:
                    # the worker cannot finish the min task without pill, but can solve it with pill
                    # remove the max task that the strengthened worker can finish instead
                    # remove_task_idx = _tasks.bisect_right(worker + strength)
                    remove_task_idx = bisect.bisect_right(_tasks, worker + strength)
                    # _tasks.pop(remove_task_idx - 1)
                    del _tasks[remove_task_idx - 1]
                    remain_pills -= 1
                else:
                    return False
            return True
        
        lo, hi = 0, min(len(workers), len(tasks))
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if check_valid(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
      
-----------------------------------------------------------------------------------------------------------------------------
class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()
        
        def fn(k, p=pills): 
            """Return True if k tasks can be completed."""
            ww = workers[-k:]
            for t in reversed(tasks[:k]): 
                if t <= ww[-1]: ww.pop()
                elif t <= ww[-1] + strength and p: 
                    p -= 1
                    i = bisect_left(ww, t - strength)
                    ww.pop(i)
                else: return False 
            return True 
          
        lo, hi = 0, min(len(tasks), len(workers))
        while lo < hi: 
            mid = lo + hi + 1 >> 1
            if fn(mid): lo = mid
            else: hi = mid - 1
        return lo 
      
-----------------------------------------------------------------------------------------------------------------------------------


from sortedcontainers import SortedList

class Solution:
    def maxTaskAssign(self, tasks, workers, pills, strength):
        tasks = sorted(tasks)
        workers = sorted(workers)

        def check(k):
            W = SortedList(workers[-k:])
            tries = pills

            for elem in tasks[:k][::-1]:
                place = W.bisect_left(elem)
                if place < len(W):
                    W.pop(place)
                elif tries > 0:
                    place2 = W.bisect_left(elem - strength)
                    if place2 < len(W):
                        W.pop(place2)
                        tries -= 1
                else:
                    return False

            return len(W) == 0

        beg, end = 0, min(len(workers), len(tasks)) + 1
        while beg + 1 < end:
            mid = (beg + end)//2
            if check(mid):
                beg = mid
            else:
                end = mid

        return beg
      
--------------------------------------------------------------------------------------------------------------
