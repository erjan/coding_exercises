'''
You are given an integer n, which indicates that there are n courses labeled from 1 to n. You are also given an array relations where relations[i] = [prevCoursei, nextCoursei], representing a prerequisite relationship between course prevCoursei and course nextCoursei: course prevCoursei has to be taken before course nextCoursei.

In one semester, you can take any number of courses as long as you have taken all the prerequisites in the previous semester for the courses you are taking.

Return the minimum number of semesters needed to take all courses. If there is no way to take all the courses, return -1.
'''

class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        g = collections.defaultdict(set)
        g_reversed = collections.defaultdict(set)
        for c in relations:
            g[c[0]].add(c[1])            
            g_reversed[c[1]].add(c[0])            
        
        queue = []
        for i in range(1, N+1):
            if not g_reversed[i]:
                queue.append((1,i))
        
        max_level = 0 
        topological_sort = []
        while queue:
            level, v1 = queue.pop(0)
            topological_sort.append(v1)
            max_level = max(level, max_level)
            for v2 in g[v1]:
                g_reversed[v2].remove(v1)
                if not g_reversed[v2]:
                    queue.append((level+1, v2))                    
        
        return max_level if len(topological_sort) == N else -1
-------------------------------------------------

class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        
        inDegree = {i: 0 for i in range(1, N+1)}
        child = {i: [] for i in range(1, N+1)}
        
        for a,b in relations:
            
            inDegree[b] += 1
            child[a].append(b)
            
        sources = deque([])
        
    
        
        for k, v in inDegree.items():
            
            if v == 0:
                sources.append(k)
                
        if not sources:
            
            return -1
                
        res = 0

        
        while sources:
            
            for _ in range(len(sources)):
                
                item = sources.popleft()
                
                for ch in child[item]:
                    
                    inDegree[ch] -= 1
                    if inDegree[ch] == 0:
                        sources.append(ch)
            res += 1
            
        for k, v in inDegree.items():
            
            if v != 0:
                return -1
        return res
----------------------------------------------------------------

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = defaultdict(list)
        indegree = [0] * n
        
        for prev_course, next_course in relations:
            indegree[next_course - 1] += 1
            graph[prev_course - 1].append(next_course - 1)
            
        queue = []
        order = []
        max_level = 0
        
        for i in range(n):
            if indegree[i] == 0:
                queue.append((i, 1))
                  
        while queue: # bfs will traverse the graph by level
            node, level = queue.pop(0)
            order.append(node)
            max_level = max(max_level, level)
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append((nei, level + 1))
            
        return max_level if len(order) == n else -1
--------------------------------------------------------------------------

Idea
First, we construct a graph where each node maps to its dependencies. To find out the depth of every node we traverse all of its descendants in depth-first fashion and assign the depth to be 1 more than the deepest child we encounter. We also check for cycles by assigning a temporary depth of -1 to every node we visit.

Complexity
Time: O(E), where E is the number of edges, since we traverse the edges during graph construction and DFS.
Space: O(E), because we store the graph of dependences.

def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:

	dependences = defaultdict(list)  # course and its dependences
	for a, b in relations:
		dependences[b].append(a)

	node_depth = {}
	def visit(node):
		if node in node_depth: return node_depth[node]
		node_depth[node] = -1  # visiting
		maxdep = 0
		for dep in dependences[node]:
			depth = visit(dep)
			if depth == -1: return -1
			maxdep = max(maxdep, depth)
		del dependences[node]
		node_depth[node] = 1 + maxdep
		return node_depth[node]
		
	while dependences:
		if visit(next(iter(dependences))) == -1: return -1
	return max(node_depth.values())
--------------------------------------------------------------------------------

Using Kahn's algo

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = {}
        indeg = [0]*n
        for u, v in relations: 
            graph.setdefault(u-1, []).append(v-1)
            indeg[v-1] += 1
        
        ans = 0
        queue = [x for x in range(n) if not indeg[x]]
        while queue: 
            ans += 1
            newq = []
            for x in queue: 
                for xx in graph.get(x, []): 
                    indeg[xx] -= 1
                    if not indeg[xx]: newq.append(xx)
            queue = newq
        return -1 if any(indeg) else ans
      

      
      
      
