'''
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).
'''

def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
	result = []
	partialResult = []

	def findPath(node):
		if node == len(graph)-1:
			result.append(partialResult.copy())
			return

		for i in graph[node]:
			partialResult.append(i)
			findPath(i)
			partialResult.pop()

	partialResult.append(0)
	findPath(0)
	return result

-----------------------------------------------------------------------------------

#dfs

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        stack = [(0, [0])]
        target = len(graph) - 1
        while stack:
            cur,route = stack.pop()
            if cur == target:
                result.append(route)
            else:
                for node in graph[cur]:
                    stack.append((node, route + [node]))
        return result
----------------------------------------------------------
#bfs

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        dq = deque([(0, [0])])
        target = len(graph) - 1
        while dq:
            cur,route = dq.popleft()
            if cur == target:
                result.append(route)
            else:
                for node in graph[cur]:
                    dq.append((node, route + [node]))
        return result
