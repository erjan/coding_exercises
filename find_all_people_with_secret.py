'''
You are given an integer n indicating there are n people numbered from 0 to n - 1. You are also given a 0-indexed 2D integer array meetings where meetings[i] = [xi, yi, timei] indicates that person xi and person yi have a meeting at timei. A person may attend multiple meetings at the same time. Finally, you are given an integer firstPerson.

Person 0 has a secret and initially shares the secret with a person firstPerson at time 0. This secret is then shared every time a meeting takes place with a person that has the secret. More formally, for every meeting, if a person xi has the secret at timei, then they will share the secret with person yi, and vice versa.

The secrets are shared instantaneously. That is, a person may receive the secret and share it with people in other meetings within the same time frame.

Return a list of all the people that have the secret after all the meetings have taken place. You may return the answer in any order.
'''


from collections import defaultdict

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetMap = {}

        for a, b, t in meetings:
            if not t in meetMap:
                meetMap[t] = defaultdict(set)
            
            meetMap[t][a].add(b)
            meetMap[t][b].add(a)

        withSecret = set([0, firstPerson])

        def dfs(graph, node, visited):
            if node in visited:
                return
            visited.add(node)

            for v in graph[node]:
                if v in visited:
                    continue
                dfs(graph, v, visited)

        for t in sorted(meetMap.keys()):
            graph = meetMap[t]
            
            visited = set()
            for p in set(graph.keys()).intersection(withSecret):
                if p in visited:
                    continue
                
                dfs(graph, p, visited)

            withSecret.update(visited)


        return list(withSecret)

            
