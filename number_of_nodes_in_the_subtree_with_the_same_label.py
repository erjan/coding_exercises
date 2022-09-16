'''
You are given a tree (i.e. a connected, undirected graph that has no cycles) consisting of n nodes numbered from 0 to n - 1 and exactly n - 1 edges. The root of the tree is the node 0, and each node of the tree has a label which is a lower-case character given in the string labels (i.e. The node with the number i has the label labels[i]).

The edges array is given on the form edges[i] = [ai, bi], which means there is an edge between nodes ai and bi in the tree.

Return an array of size n where ans[i] is the number of nodes in the subtree of the ith node which have the same label as node i.

A subtree of a tree T is the tree consisting of a node in T and all of its descendant nodes.
'''

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        response = [0] * n
        # Save edges in more usable data structure, to get the list of possible next nodes in the constant time
        node2edges = [[] for _ in range(n)]
        for edge in edges:
            node2edges[edge[0]].append(edge[1])
            node2edges[edge[1]].append(edge[0])
            
        def dfs(nodeId: int, parentNodeId: int, labelCounter: List[int]) -> None:
            # nodeLabelId is an ASCII code of symbol minus 97, because a == 97, b == 98, c == 99, etc, z == 122
            nodeLabelId = ord(labels[nodeId]) - 97
            # save to temporary variable amount of nodes with label same as is for current node.
            # Everything that will be added for this nodeLabelId after, will counts as subtree of this node.
            before = labelCounter[nodeLabelId]
            # Count this node as well
            labelCounter[nodeLabelId] += 1
            # Visit all possible nextNodes
            for nextNodeId in node2edges[nodeId]:
                # except the one we have came from
                if nextNodeId == parentNodeId:
                    continue
                dfs(nextNodeId, nodeId, labelCounter)
            # Set the result for the current node:
            # everything that was added after we saved the "before" variable was added from subtree of this node.
            response[nodeId] = labelCounter[nodeLabelId] - before
        
        # Start with root node (ID 0) and parentNodeId == -1 which is mean that any nextNode is acceptable for the root
        dfs(0, -1, [0] * 26)
        return response
      
----------------------------------------------------

import collections

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        tree = collections.defaultdict(set)
        rec = [[0] * 26 for _ in range(n)]
        
        for node1, node2 in edges:
            tree[node1].add(node2)
            tree[node2].add(node1)
            
        degrees = {}
        deque = collections.deque([])
        for node in tree:
            degrees[node] = len(tree[node])
            if degrees[node] == 1:
                deque.append(node)
        
        
        while deque:
            node = deque.popleft()
            label = labels[node]
            position = ord(label) - ord('a') 
            rec[node][position] += 1 # update number of each label at current node
            if node != 0:
                parent = tree[node].pop() # we only have one element at the node
                degrees[parent] -= 1 # parenet degree decrease by 1
                tree[parent].remove(node) # remove the child from the parent
                for i in range(26):
                    rec[parent][i] += rec[node][i] #update the number of label we meet for the parent's nodes
                    
                if degrees[parent] == 1: # now the parent becomes a leaf 
                    deque.append(parent)
        
        res = [0] * n
        for i in range(n):
            position = ord(labels[i]) - ord('a')
            res[i] = rec[i][position]
        
        return res
------------------------------------------------------------------------------------------------------------------
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        
        graph = defaultdict(list)
        val = dict()
        
        res = [0] * n
        
        for i in range(n):
            graph[i] = []
        
        for i, (s, d) in enumerate(edges):
            graph[s].append(d)
            graph[d].append(s)
            val[s] = labels[s]
            val[d] = labels[d]

        
        def dfs(node, counter, parent):
            for neigh in graph[node]:
                if neigh != parent:
                    dfs_res = dfs(neigh, defaultdict(int), node)
                    for v in dfs_res:
                        counter[v] += dfs_res[v]
                
            counter[val[node]] += 1
            res[node] = counter[val[node]]
            return counter
            
        dfs(0, defaultdict(int), -1)
        
        return res
      
