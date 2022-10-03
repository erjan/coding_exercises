'''
You are given n tasks labeled from 0 to n - 1 represented by a 2D integer array tasks, where tasks[i] = [enqueueTimei, processingTimei] means that the i​​​​​​th​​​​ task will be available to process at enqueueTimei and will take processingTimei to finish processing.

You have a single-threaded CPU that can process at most one task at a time and will act in the following way:

If the CPU is idle and there are no available tasks to process, the CPU remains idle.
If the CPU is idle and there are available tasks, the CPU will choose the one with the shortest processing time. If multiple tasks have the same shortest processing time, it will choose the task with the smallest index.
Once a task is started, the CPU will process the entire task without stopping.
The CPU can finish a task then start a new one instantly.
Return the order in which the CPU will process the tasks.
'''

def getOrder(self, tasks: List[List[int]]) -> List[int]:
    # Sort tasks by start time
    tasks = sorted([(start, task_length, index)
                    for index, (start, task_length) in enumerate(tasks)], reverse=True)
    ans = []
    current_time = 0
    heap = []

    while tasks or heap:
        # No more queued tasks; jump ahead to next arrival
        if not heap:
            current_time = max(current_time, tasks[-1][0])
            
        # Add all tasks that have arrived by the current time
        while tasks and tasks[-1][0] <= current_time:
            start, process_time, task_index = tasks.pop()
            # Heap is ordered by process time and old task index
            heapq.heappush(heap, (process_time, task_index))
        
        next_task_length, next_task_index = heapq.heappop(heap)
        ans.append(next_task_index)
        
        # Advance time forward
        current_time += next_task_length

    return ans
