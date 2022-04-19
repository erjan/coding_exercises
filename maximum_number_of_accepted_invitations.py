'''
There are m boys and n girls in a class attending an upcoming party.

You are given an m x n integer matrix grid, where grid[i][j] equals 0 or 1. If grid[i][j] == 1, then that means the ith boy can invite the jth girl to the party. A boy can invite at most one girl, and a girl can accept at most one invitation from a boy.

Return the maximum possible number of accepted invitations.

 

Example 1:

Input: grid = [[1,1,1],
               [1,0,1],
               [0,0,1]]
Output: 3
Explanation: The invitations are sent as follows:
- The 1st boy invites the 2nd girl.
- The 2nd boy invites the 1st girl.
- The 3rd boy invites the 3rd girl.
Example 2:

Input: grid = [[1,0,1,0],
               [1,0,0,0],
               [0,0,1,0],
               [1,1,1,0]]
Output: 3
Explanation: The invitations are sent as follows:
-The 1st boy invites the 3rd girl.
-The 2nd boy invites the 1st girl.
-The 3rd boy invites no one.
-The 4th boy invites the 2nd girl.
'''


 def maximumInvitations(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        matching = [-1] * N # girls' mate
        
        def dfs(node, seen):
            for nei in range(N): # ask each girl
                if grid[node][nei] and not seen[nei]: # a potential mate; the girl has not been asked before
                    seen[nei] = True # mark her as asked
                    if matching[nei] == -1 or dfs(matching[nei], seen): # if the girl does not have a mate or her mate can be matched to someone else
                        matching[nei] = node # we match her to the boy "node"
                        return True
            return False
    
        res = 0
        for i in range(M):
            seen = [False] * N
            if dfs(i, seen):
                res += 1
                
        return res
      
-------------------------------------------------------------


class Solution:
    def maximumInvitations(self, a: List[List[int]]) -> int:
        
        # ford-fulkerson
        # residual graph
        
        n = len(a)
        m = len(a[0])
        
        # node -> successors
        g = defaultdict(set)
        
        SOURCE = "source"
        SINK = "sink"
    
        # source to boys
        for i in range(n):
            g[SOURCE].add(("b",i))
            
        # girls to sink
        for j in range(m):
            g["g",j].add(SINK)
        
        # boys to girls
        for i in range(n):
            for j in range(m):
                if a[i][j]:
                    g["b",i].add(("g",j))
        
        
        def recurse(u):
            
            if u in seen:
                return None
            seen.add(u)
            
            if u == SINK:
                return deque()
            
            for v in g[u]:
                cret = recurse(v)
                
                if cret is not None:
                    cret.appendleft((u,v))
                    return cret
            
            return None
            
        
        ret = 0
        
        while True:
            
            seen = set()
            
            chain = recurse(SOURCE)
            
            if chain is None:
                break
            
            # reverse residuals for all edges in the chain
            for u,v in chain:
                g[u].remove(v)
                g[v].add(u)
            
            ret += 1
        
        return ret
--------------------------------------

class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        graph = {r: {c for c, n in enumerate(row) if n} for r, row in enumerate(grid)}
        matches = {}
        for rx in graph:
            parents = {}
            visited = graph[rx].copy()
            stack = list(visited)
            while stack:
                c = stack.pop()
                r = matches.get(c)
                if r is None:
                    while c in parents:
                        p = parents[c]
                        matches[c] = matches[p]
                        c = p
                    matches[c] = rx
                    break
                visit = graph[r] - visited
                visited |= visit
                stack.extend(visit)
                parents |= {x: c for x in visit}
        return len(matches)
-----------------------------------------------


class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        match = [-1] * n
        
        def fn(i): 
            """Look up match for ith boy."""
            for j in range(n):
                if grid[i][j] and not seen[j]: 
                    seen[j] = True
                    if match[j] == -1 or fn(match[j]): 
                        match[j] = i
                        return True 
            return False 
        
        for i in range(m):
            seen = [False] * n
            if fn(i): ans += 1
        return ans 
      
      
      
      
