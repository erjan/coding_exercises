'''
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.
'''


Simple union-find with path compression.

Python solution 1

def countComponents(self, n, edges):
    p = range(n)
    def find(v):
        if p[v] != v:
            p[v] = find(p[v])
        return p[v]
    for v, w in edges:
        p[find(v)] = find(w)
    return len(set(map(find, p)))
Python solution 2

def countComponents(self, n, edges):
    p = range(n)
    def find(v):
        if p[v] != v:
            p[v] = find(p[v])
        return p[v]
    for e in edges:
        v, w = map(find, e)
        p[v] = w
        n -= v != w
    return n
    
----------------------------------------------------------------------------------
Thought process
union find, find disjoint sets, then check how many sets there are

path compression
union by rank
be aware that after a union operation, the parent of a node might not be updated immediately
to solve this problem and avoid potential bugs, we should not rely on the raw parent representation, instead, we should call find(node) to actually obtain the correct parent/set label
dfs, bfs, if a node is not already visited, try bfs/dfs starting from this node, add the count of connected components by 1

Simple UnionFind
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[rx] = ry 
        
        for x, y in edges:
            union(x, y)
        return len({find(i) for i in range(n)})
UnionFind with Union by Rank
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        rank = [1] * n
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            if rank[rx] > rank[ry]:
                parent[ry] = rx
            elif rank[rx] < rank[ry]:
                parent[rx] = ry
            else:
                parent[rx] = ry
                rank[ry] += 1
        
        for x, y in edges:
            union(x, y)
        return len({find(i) for i in range(n)})
DFS
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        def dfs(node, seen):
            seen.add(node)
            for neighbor in graph[node]:
                if neighbor not in seen:
                    dfs(neighbor, seen)
        count = 0
        seen = set()
        for node in range(n):
            if node not in seen:
                dfs(node, seen)
                count += 1
        return count
BFS
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        def bfs(node, seen):
            queue = collections.deque([node])
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        queue.append(neighbor)
        count = 0
        seen = set()
        for node in range(n):
            if node not in seen:
                seen.add(node)
                bfs(node, seen)
                count += 1
        return count
------------------------------------------------------------------------------------
DFS and BFS are similiar. First we build an adjacent-list graph base on edges. Then we iterate all nodes in graph: {0,...,n-1}.
In each iteration, we can either DFS or BFS to remove all connected component nodes. The times that node is still in our graph when we iterate it is the number of connected components.

def countComponents(n, edges):
	g, cnt, seen = collections.defaultdict(set), 0, set()
	for u, v in edges: 
		g[u].add(v), g[v].add(u)

	def dfs(node):
		if node not in seen:
			seen.add(node)
			for nei in g[node]: dfs(nei)
		return 1

	def bfs(q):
		for node in q:
			if node not in seen:
				q += g[node]
				seen.add(node)
		return 1

	# return sum(dfs(i) for i in range(n) if i not in seen)
	return sum(bfs([i]) for i in range(n) if i not in seen)
We can save space of seen by deleting node in graph after we search it so that we can check if we have visited a node by checking whether it's in the graph.

We can also use union-find to solve this problem. We first union all connected nodes and then count the distinctive union groups

def countComponents(n, edges):
	p = list(range(n))
	def find(x):
		if x != p[x]: p[x] = find(p[x])
		return p[x]
	for u, v in edges:
		p[find(u)] = find(v)
	return len(set(map(find, range(n))))
  
-------------------------------------------------------------------
class UnionFind(object):
    def __init__(self, n):
        self.count = n
        self.size = [1] * n
        self.id = range(n)

    def find(self, p):
        while self.id[p] != p:
            self.id[p] = self.id[self.id[p]]
            p = self.id[p]
        return p

    def union(self, p, q):
        idp, idq = map(self.find, (p, q))
        if idp == idq:
            return

        less, more = (
            (idp, idq) if self.size[idp] < self.size[idq] else (idq, idp))

        self.id[less] = self.id[more]
        self.size[more] += self.size[less]

        self.count -= 1


class Solution(object):
    def countComponents(self, n, edges):
        unionFind = UnionFind(n)
        [unionFind.union(*e) for e in edges]
        return unionFind.count
        
