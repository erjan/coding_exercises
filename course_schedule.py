'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
'''


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        todo = {i: set() for i in range(numCourses)} 
        graph = defaultdict(set)
        for i,j in prerequisites:
            todo[i].add(j)
            graph[j].add(i)
        q = deque([])
        for k,v in todo.items():
            if len(v) == 0:
                q.append(k)
        while q:
            n = q.popleft()
            for i in graph[n]:
                todo[i].remove(n)
                if len(todo[i]) == 0:
                    q.append(i)
            todo.pop(n)
        return not todo
