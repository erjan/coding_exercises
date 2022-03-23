'''
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the 
graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a 
bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a 
valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.
'''

class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        graph = self.buildGraph(edges)
        return self.hasPath(graph, start, end, set())
    
	# function to convert list of edges to adjacency list graph
    def buildGraph(self, edges):
        graph = {}
        for edge in edges:
            a, b = edge
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
            graph[a].append(b)
            graph[b].append(a)    
        return graph
    
    def hasPath(self, graph, src, dst, visited):
        if src == dst:
            return True
        if src in visited:
            return False
        visited.add(src)
        for neighbour in graph[src]:
            if self.hasPath(graph, neighbour, dst, visited) == True:
                return True
        return False


class Solution(object):
    def validPath(self, n, edges, start, end):
        """
        :type n: int
        :type edges: List[List[int]]
        :type start: int
        :type end: int
        :rtype: bool
        """
        visited = [False]*n
        d = {}
		#store the undirected edges for both vertices
        for i in edges:
            if i[0] in d:
                d[i[0]].append(i[1])
            else:
                d[i[0]] = [i[1]]
                
            if i[1] in d:
                d[i[1]].append(i[0])
            else:
                d[i[1]] = [i[0]]
        #create a queue as we will apply BFS
        q = [start]
        while q:
            curr = q.pop(0)  #pop the first element as we do in queue
            if curr == end:  #if its the end then we can return True
                return True
            elif curr in d and not visited[curr]: #else if it is not the end then check whether its visited or not
                q.extend(d[curr])  #add the adjacent vertices of the current node to the queue
            visited[curr] = True  #mark this curr vertex as visited = True, so that we dont visit this vertex again
        return False  #return False if the queue gets empty and we dont reach the end
