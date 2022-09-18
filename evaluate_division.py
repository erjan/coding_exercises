'''
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.
'''

#bfs - my own

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        
        g = defaultdict(dict)
        
        for (x,y) , v in zip(equations, values):
            g[x][y] = v
            g[y][x] = 1/v
            
        
        def bfs(src,dest):
            if not (src in g  and dest in g): return -1.0
            
            queue = [(src,1.0)]
            visited = set()
            
            for x,v in queue:
                if x == dest:
                    return v
                visited.add(x)
                
                for y in g[x]:
                    if y not in visited:
                        queue.append((y,v*g[x][y]))
            return -1.0
        
        return [bfs(src,dest) for src, dest in queries]



#bfs
def calcEquation(equations, values, queries):
	G = collections.defaultdict(dict)
	for (x, y), v in zip(equations, values):
		G[x][y] = v
		G[y][x] = 1/v
	def bfs(src, dst):
		if not (src in G and dst in G): return -1.0
		q, seen = [(src, 1.0)], set()
		for x, v in q:
			if x == dst: 
				return v
			seen.add(x)
			for y in G[x]:
				if y not in seen: 
					q.append((y, v*G[x][y]))
		return -1.0
	return [bfs(s, d) for s, d in queries]

#union find
def calcEquation(equations, values):
	root = {}
	
	# xr = x/parent(x), pr = parent(x)/root(x), update xr to xr*pr = x/root(x)
	def find(x):
		p, xr = root.setdefault(x, (x, 1.0))
		if x != p:
			r, pr = find(p)
			root[x] = (r, xr*pr)
		return root[x]

	# if root(x) = root(y), equations "x / y" doable as (x/root(x)) / (y/root(y)) = xr / yr
	def union(x, y, ratio):
		px, xr, py, yr = *find(x), *find(y)
		if not ratio:
			return xr / yr if px == py else -1.0
		if px != py:
			root[px] = (py, yr/xr*ratio)

	for (x, y), v in zip(equations, values):
		union(x, y, v)
	return [union(x, y, 0) if x in root and y in root else -1.0 for x, y in queries]

-------------------------------------
#dfs
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def dfs(graph, start, end, visited):
            if start == end and graph[start]:
                return 1.0
            
            visited.add(start)
            for neigh, val in graph[start]:
                if neigh in visited:
                    continue
                
                tmp = dfs(graph, neigh, end, visited)
                if tmp > 0:
                    return val * tmp
            
            return -1.0
            
        graph = collections.defaultdict(set)
        for items, v in zip(equations, values):
            x, y = items
            graph[x].add((y, v))
            graph[y].add((x, 1.0 / v))
        
        res = []
        for q in queries:
            res.append(dfs(graph, q[0], q[1], set()))
        
        return res
