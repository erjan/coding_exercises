So, after dozens of wrong answers I'm here to cast some light on this helluva complicated question for me.

We have directed graph with self-loops, parallel edges (explain furhter) and all various nagging issues.

Let's start: create adjacency list from edges. Then start iteration.

Edge case: if we have source = 1, destination = 0, but 1 -> 0, then we're to return False.
But how to do it? If check to catch it and if we really have case as above => False, otherwise, when have [[]] adjacency list -> True (but question has restriction on min number of rows 2.

Go back to main loop: here we create fresh hash set to catch possible duplicated (loops). We're to refresh it after every new vertex loop, as we're allowed to have non-unique verticies.
For clarity:[[1,2,3], [2,3,4], [3,4], [4], []. Here we may have 3 as intermediate vertex, but if we don't refres hash set => wrong answer.

In recursive function:
At first we must have base case: if current vertex doesn't have outbound nodes, then we need to check whether it's really our destination + with such move we'll catch deadlocks.
Example: [....[4,6] (vertex=2)]. So, image 4 does have way to destination, but 6 don't -> it's deadlock which mustreturn False to overall result.

Next add current main vertex to visited and proceed to adjacent nodes. If it's adjacent nodes are already in visited => False as it may case loops (including self-loop): [[1], [0,1]] is an example with loop and self-loop.
Crucial: don't return True immediately as we're to catch possible deadlock. And it'll be impossible to do so if we terminate. We need to proceed further.

After some path has been cleared, we need to remove main vertex from visited so as not to cause errors.

If at some moment we get False, due to recursion stack we'll push it to the main fucntion where result will do all the work

To bear in mind:

don't add source and destination to visited
What is parallel edge? When we have 2+ edges from one to another node (2 similar nodes). Like [[1,2,2]] Here node 0 has 2 edges to node 2
When source != destination and len(adj[sourse]) == 0 => it's a an error
Hope it helps! Upvote plz!

class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = [[] for _ in range(n)]
        for e1, e2 in edges:
            adj[e1].append(e2)
        
        for vertex in adj[source]:
            
            visited = set()
            
            result = self.dfs(adj, destination, vertex, visited)
            if not result:
                return False

        if len(adj[source]) == 0:
            return source == destination
        
        return True
    
    def dfs(self, adj, destination, vertex, visited):
        # to catch deadlocks
        if not len(adj[vertex]):
            return vertex == destination

        visited.add(vertex)
        for node in adj[vertex]:
            # catch self-loops or loops
            if node in visited:
                return False
            
            result = self.dfs(adj, destination, node, visited)
            if not result:
                return False
 
        visited.remove(vertex)
        return True
------------------------------------------------------------------------------------------             
class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        def dfs(vtx= source):
            if (vtx in path) or (not graph[vtx] and vtx != destination):
                return False
            path.add(vtx)
            for nei in graph[vtx]:
                if not dfs(nei):
                    return False
            path.remove(vtx)
            return True
        
        graph = defaultdict(list)
        for v1, v2 in edges:
            graph[v1].append(v2)
           
        path = set()
        return dfs()
---------------------------------------------------------------
             

class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {}
        for u, v in edges: graph.setdefault(u, []).append(v)
        
        def fn(x): 
            """Return True if all paths starting from x lead to destination."""
            if x not in graph: return x == destination
            if color[x]: return color[x] == 1
            color[x] = -1 
            for xx in graph[x]: 
                if not fn(xx): return False 
            color[x] = 1
            return True 
        
        color = [0] * n 
        return fn(source)
---------------------         
             
class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = defaultdict(list)
        
        for a,b in edges:
            adj[a].append(b)
        
        # outgoing edges from destination
        if destination in adj:
            return False
        
        def dfs(s,visited):
            if s == destination:
                return True
            
            # cycle or end of the path
            if s in visited or s not in adj:
                return False
            
            return all( dfs(nxt,visited+[s])  for nxt in adj[s] )
        
        return dfs(source,[])
             
             
             
