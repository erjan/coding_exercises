'''
You are given two 0-indexed integer arrays servers and tasks of lengths n​​​​​​ and m​​​​​​ respectively. servers[i] is the weight of the i​​​​​​th​​​​ server, and tasks[j] is the time needed to process the j​​​​​​th​​​​ task in seconds.

Tasks are assigned to the servers using a task queue. Initially, all servers are free, and the queue is empty.

At second j, the jth task is inserted into the queue (starting with the 0th task being inserted at second 0). As long as there are free servers and the queue is not empty, the task in the front of the queue will be assigned to a free server with the smallest weight, and in case of a tie, it is assigned to a free server with the smallest index.

If there are no free servers and the queue is not empty, we wait until a server becomes free and immediately assign the next task. If multiple servers become free at the same time, then multiple tasks from the queue will be assigned in order of insertion following the weight and index priorities above.

A server that is assigned task j at second t will be free again at second t + tasks[j].

Build an array ans​​​​ of length m, where ans[j] is the index of the server the j​​​​​​th task will be assigned to.

Return the array ans​​​​.
'''
class Solution:
def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
    
    # sort the servers in order of weight, keeping index 
    server_avail = [(w,i) for i,w in enumerate(servers)]
    heapify(server_avail)
    tasks_in_progress = []
    res = []
    st=0
    for j,task in enumerate(tasks):
        #starting time of task
        st = max(st,j)
        
        # if any server is not free then we can take start-time equal to end-time of task
        if not server_avail:
            st = tasks_in_progress[0][0]
        
        # pop the completed task's server and push inside the server avail
        while tasks_in_progress and tasks_in_progress[0][0]<=st:
            heapq.heappush(server_avail,heappop(tasks_in_progress)[1])
            
        # append index of used server in res
        res.append(server_avail[0][1])
        
        # push the first available server in "server_avail" heap to "tasks_in_progress" heap
        heapq.heappush(tasks_in_progress,(st+task,heappop(server_avail)))
    
    return res
