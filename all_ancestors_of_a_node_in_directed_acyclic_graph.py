'''
You are given a positive integer n representing the number of nodes of a Directed Acyclic Graph (DAG). The nodes are numbered from 0 to n - 1 (inclusive).

You are also given a 2D integer array edges, where edges[i] = [fromi, toi] denotes that there is a unidirectional edge from fromi to toi in the graph.

Return a list answer, where answer[i] is the list of ancestors of the ith node, sorted in ascending order.

A node u is an ancestor of another node v if u can reach v via a set of edges
'''

class Solution:
    """
    we can use a bfs based approach to get the required ancestors for each node nodes
    nodes with indegree of 0 will have empty ancestors list
    then we will put all nodes with no incoming edges in queue
    until the queue is empty:
        pop the node
        for all neighbors of node:
            add the ancestor set of node along with the node in the ancestor set of neighbor
    """
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = {node: set() for node in range(n)}
        indegree = {node: 0 for node in range(n)}
        ans = [set() for _ in range(n)]
        for edge in edges:
            graph[edge[0]].add(edge[1])
            indegree[edge[1]]+=1
        nodes_with_no_incoming_edges = []
        for node, indeg in indegree.items():
            if indeg == 0:
                nodes_with_no_incoming_edges.append(node)
        while len(nodes_with_no_incoming_edges):
            node = nodes_with_no_incoming_edges.pop()
            for neighbor in graph[node]:
                ans[neighbor].add(node)
                ans[neighbor] = ans[neighbor].union(ans[node])
                indegree[neighbor]-=1
                if indegree[neighbor] == 0:
                    nodes_with_no_incoming_edges.append(neighbor)
                    
        sorted_ans = []           
        for ancestor in ans:
            temp = sorted(list(ancestor))
            sorted_ans.append(temp)
        return sorted_ans
