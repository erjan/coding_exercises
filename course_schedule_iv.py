'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course ai first if you want to take course bi.

For example, the pair [0, 1] indicates that you have to take course 0 before you can take course 1.
Prerequisites can also be indirect. If course a is a prerequisite of course b, and course b is a prerequisite of course c, then course a is a prerequisite of course c.

You are also given an array queries where queries[j] = [uj, vj]. For the jth query, you should answer whether course uj is a prerequisite of course vj or not.

Return a boolean array answer, where answer[j] is the answer to the jth query.
'''


from collections import defaultdict, deque

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        neighbors = {node: set() for node in range(numCourses)}    # store the graph
        indegree = defaultdict(int)     # store indegree info for each node
        pre_lookup = defaultdict(set)   # store the prerequisites info for each node
        
        # create the graph
        for pre, post in prerequisites:
            neighbors[pre].add(post)
            indegree[post] += 1
        
        # add 0 degree nodes into queue for topological sort
        queue = deque([])
        for n in neighbors:
            if indegree[n] == 0:
                queue.append(n)
        
        # use BFS to do topological sort to create a prerequisite lookup dictionary
        while queue:
            cur = queue.popleft()
            for neighbor in neighbors[cur]:
                pre_lookup[neighbor].add(cur)                   # add current node as the prerequisite of this neighbor node
                pre_lookup[neighbor].update(pre_lookup[cur])    # add all the preqs for current node to the neighbor node's preqs
                
                indegree[neighbor] -= 1         # regular topological search operations
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # traverse the queries and return the results
        result = [True if q[0] in pre_lookup[q[1]] else False for q in queries]
        
        return result
