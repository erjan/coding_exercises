'''
You are given an integer n and a 2D integer array queries.

There are n cities numbered from 0 to n - 1. Initially, there is a unidirectional road from city i to city i + 1 for all 0 <= i < n - 1.

queries[i] = [ui, vi] represents the addition of a new unidirectional road from city ui to city vi. After each query, you need to find the length of the shortest path from city 0 to city n - 1.

Return an array answer where for each i in the range [0, queries.length - 1], answer[i] is the length of the shortest path from city 0 to city n - 1 after processing the first i + 1 queries.
'''

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        res = []
        graph = defaultdict(list)

        for i in range(n-1):
            graph[i].append(i+1)

        for q in queries:
            u,v = q
            graph[u].append(v)
            
            q = deque([(0,0)])

            visited = set()

            while q:
                cur_node, cur_step = q.popleft()

                if cur_node == n-1:
                    res.append(cur_step)
                    break
                
                if cur_node not in visited:
                    visited.add(cur_node)
                
                for node in graph[cur_node]:
                    if node not in visited:
                        q.append( ((node,cur_step+1)) )
        return res
                
