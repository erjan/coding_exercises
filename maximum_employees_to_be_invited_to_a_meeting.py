'''
A company is organizing a meeting and has a list of n employees, waiting to be invited. They have arranged for a large circular table, capable of seating any number of employees.

The employees are numbered from 0 to n - 1. Each employee has a favorite person and they will attend the meeting only if they can sit next to their favorite person at the table. The favorite person of an employee is not themself.

Given a 0-indexed integer array favorite, where favorite[i] denotes the favorite person of the ith employee, return the maximum number of employees that can be invited to the meeting.
'''

class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        graph = [[] for _ in range(n)]
        for i, x in enumerate(favorite): graph[x].append(i)
        
        def bfs(x, seen): 
            """Return longest arm of x."""
            ans = 0 
            queue = deque([x])
            while queue: 
                for _ in range(len(queue)): 
                    u = queue.popleft()
                    for v in graph[u]: 
                        if v not in seen: 
                            seen.add(v)
                            queue.append(v)
                ans += 1
            return ans 
        
        ans = 0 
        seen = [False]*n
        for i, x in enumerate(favorite): 
            if favorite[x] == i and not seen[i]: 
                seen[i] = seen[x] = True 
                ans += bfs(i, {i, x}) + bfs(x, {i, x})
                
        dp = [0]*n
        for i, x in enumerate(favorite): 
            if dp[i] == 0: 
                ii, val = i, 0
                memo = {}
                while ii not in memo: 
                    if dp[ii]: 
                        cycle = dp[ii]
                        break
                    memo[ii] = val
                    val += 1
                    ii = favorite[ii]
                else: cycle = val - memo[ii]
                for k in memo: dp[k] = cycle
        return max(ans, max(dp))
