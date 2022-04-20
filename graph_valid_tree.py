'''
You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list 
of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.
'''


There are so many different approaches and so many different ways to implement each. I find it hard to decide, so here are several :-)

In all of them, I check one of these tree characterizations:

Has n-1 edges and is acyclic.
Has n-1 edges and is connected.
Solution 1 ... Union-Find

The test cases are small and harmless, simple union-find suffices (runs in about 50~60 ms).

def validTree(self, n, edges):
    parent = range(n)
    def find(x):
        return x if parent[x] == x else find(parent[x])
    def union(xy):
        x, y = map(find, xy)
        parent[x] = y
        return x != y
    return len(edges) == n-1 and all(map(union, edges))
A version without using all(...), to be closer to other programming languages:

def validTree(self, n, edges):
    parent = range(n)
    def find(x):
        return x if parent[x] == x else find(parent[x])
    for e in edges:
        x, y = map(find, e)
        if x == y:
            return False
        parent[x] = y
    return len(edges) == n - 1
A version checking len(edges) != n - 1 first, as parent = range(n) could fail for huge n:

def validTree(self, n, edges):
    if len(edges) != n - 1:
        return False
    parent = range(n)
    def find(x):
        return x if parent[x] == x else find(parent[x])
    def union(xy):
        x, y = map(find, xy)
        parent[x] = y
        return x != y
    return all(map(union, edges))
Solution 2 ... DFS

def validTree(self, n, edges):
    neighbors = {i: [] for i in range(n)}
    for v, w in edges:
        neighbors[v] += w,
        neighbors[w] += v,
    def visit(v):
        map(visit, neighbors.pop(v, []))
    visit(0)
    return len(edges) == n-1 and not neighbors
Or check the number of edges first, to be faster and to survive unreasonably huge n:

def validTree(self, n, edges):
    if len(edges) != n - 1:
        return False
    neighbors = {i: [] for i in range(n)}
    for v, w in edges:
        neighbors[v] += w,
        neighbors[w] += v,
    def visit(v):
        map(visit, neighbors.pop(v, []))
    visit(0)
    return not neighbors
For an iterative version, just replace the three "visit" lines with

    stack = [0]
    while stack:
        stack += neighbors.pop(stack.pop(), [])
Solution 3 ... BFS

Just like DFS above, but replace the three "visit" lines with

    queue = [0]
    for v in queue:
        queue += neighbors.pop(v, [])
or, since that is not guaranteed to work, the safer

    queue = collections.deque([0])
    while queue:
        queue.extend(neighbors.pop(queue.popleft(), []))
----------------------------------------------------------

def validTree(self, n, edges):
    dic = {i: set() for i in xrange(n)}
    for i, j in edges:
        dic[i].add(j)
        dic[j].add(i)
    stack = [dic.keys()[0]]
    visited = set()
    while stack:
        node = stack.pop()
        if node in visited:
            return False
        visited.add(node)
        for neighbour in dic[node]:
            stack.append(neighbour)
            dic[neighbour].remove(node)
        dic.pop(node)
    return not dic
-----------------------------------------------------------

UnionFind
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x != root_y:
                parent[root_x] = root_y
        
        for x, y in edges:
            union(x, y)
        return len({find(i) for i in range(n)}) == 1
BFS
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        graph = collections.defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        queue = collections.deque([0])
        seen = {0}
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
        return len(seen) == n
DFS (Recursive)
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        graph = collections.defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        seen = set()
        def dfs(node):
            seen.add(node)
            for neighbor in graph[node]:
                if neighbor not in seen:
                    dfs(neighbor)
        dfs(0)
        return len(seen) == n
DFS (Iterative)
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        graph = collections.defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        seen = set()
        stack = [0]
        while stack:
            node = stack.pop()
            seen.add(node)
            for neighbor in graph[node]:
                if neighbor not in seen:
                    stack.append(neighbor)
        return len(seen) == n
-----------------------------------------------------

A n-node valid tree is a graph that has n-1 edges without any isolated component or cycle. Since there are n-1 edges and n nodes, no isolated component <=> no cycle.

To detect isolated component, we can use BFS:
We just start from any node and delete every node we meet during the BFS. If there is any node left, then there is an isolated component.

def validTree(n, edges):
	if len(edges) != n-1: return False
	g, q = {i:[] for i in range(n)}, [0]
	for u, v in edges: 
		g[u].append(v), g[v].append(u)
	for x in q:
		q += g.pop(x, [])
	return not g
To detect cycle, we can use DFS or Union Find. If we meet same node twice in one DFS path or union two nodes that are already in the same group, then there is a cycle.
I used UF here:

def validTree(n, edges):
	if len(edges) != n-1: return False
	p = list(range(n))
	def find(x):
		if p[x] != x: p[x] = find(p[x])
		return p[x]
	for x, y in edges:
		px, py = find(x), find(y)
		if px == py: return False
		p[px] = py
	return True
----------------------------------------------------------

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
#         Making a graph here (following the DRY principle for both DFS and BFS cases)
        graph = {i: [] for i in range(n)}
        for edge1, edge2 in edges: 
            graph[edge1].append(edge2)
            graph[edge2].append(edge1)
        return self.usingGraphBFS(n, edges, graph)
    
    def usingGraphBFS(self, n, edges, graph):
        queue = deque([0])
        seen = set()
        parent = {}
        while len(queue):
            first = queue.popleft()
            seen.add(first)
            for child in graph.get(first):
                if parent.get(first) == child: continue
                if child in seen: return False
                parent[child] = first
                queue.append(child)
        return len(seen) == n
    
    def usingGraphDFS(self, n, edges, graph):
        nodes = set()
        parent = {}
        stack = [0]
        while len(stack):
            node = stack.pop()
            nodes.add(node)
            for child in graph[node]:
                if parent.get(node) == child: continue
                if child in parent: return False
                stack.append(child)
                parent[child] = node
        
        # print(nodes)  
        return len(nodes) == n
        
    def usingUnionFind(self, n, edges):
        nodes = [i for i in range(n)]
        for edge1, edge2 in edges:
            res = self.union(nodes, edge1, edge2)
            if not res: return False
        
        root = self.find(nodes, 0)
        for i in range(1, n):
            if self.find(nodes, i) != root: return False
        
        return True
    
    # Helper function        
    def checkCycle(self, graph, node, visited):
        if node in visited: return False
        visited.add(node)
        for child in graph[node]:
            res = self.checkCycle(graph, child, visited)
            if not res: return False
        return visited
     
    # Helper function
    def find(self, nodes, edge):
        root = edge
        while root != nodes[root]: root = nodes[root]
        while edge != nodes[edge]:
            temp = nodes[edge]
            nodes[edge] = root
            edge = temp
        return root
    
    # Helper function
    def union(self, nodes, edge1, edge2):
        root1 = self.find(nodes, edge1)
        root2 = self.find(nodes, edge2)
        if root1 == root2: return False
        nodes[root1] = nodes[root2]
        return True

      
  
        
