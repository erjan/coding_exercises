'''
The diameter of a tree is the number of edges in the longest path in that tree.

There is an undirected tree of n nodes labeled from 0 to n - 1. You are given a 2D array edges where edges.length == n - 1 and edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the tree.

Return the diameter of the tree.

 
 '''

Summary of algo:

starting from any node, apply (the first) breadth-first search and retain the last node while traversing the tree;
starting from the last node in the previous step, apply (the second) breadth-first search and return the max depth while traversing the tree.
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        #build tree
        connected = dict()
        for x, y in edges:
            connected.setdefault(x, set()).add(y)
            connected.setdefault(y, set()).add(x)
        
        def bfs(node, level=0):
            """Apply (graph) bfs starting at given node by level 
            and return last node in search and levels."""
            queue = [node]
            seen = set(queue)
            while queue: 
                temp = []
                for x in queue: 
                    for y in connected[x]: 
                        if y not in seen: 
                            temp.append(y)
                            seen.add(y)
                queue = temp 
                level += 1
            return x, level - 1
			
        #two passes 
        #1st pass - find a node on longest path
        #2nd pass - find length of longest path (i.e. diameter of the tree)
        node = bfs(0)[0]
        return bfs(node)[1]
      
---------------------------------------------------------------------------------
from collections import defaultdict

class Solution:
    
    max_diameter = 0
    
    def treeDiameter(self, edges: List[List[int]]) -> int:
        if not bool(edges):
            return 0
        d, root = self.get_tree(edges)
        self.get_diameter(d, root, root)
        return self.max_diameter - 1

    def get_tree(self, edges):
        d = defaultdict(lambda: [])
        # node, edges
        root = [None, None]
        for edge in edges:
            d[edge[0]].append(edge[1])
            if root[1] is None or len(d[edge[0]]) > root[1]:
                root[0] = edge[0]
                root[1] = len(d[edge[0]])
            
            d[edge[1]].append(edge[0])
            if len(d[edge[1]]) > root[1]:
                root[0] = edge[1]
                root[1] = len(d[edge[1]])
        return d, root[0]
    
    def get_diameter(self, d, node, parent):
        if node is None:
            return 0

        max_branch = 0
        next_max_branch = 0
        for child in d[node]:
            if child == parent:
                continue
            cur_branch = self.get_diameter(d, child, node)
            
            if cur_branch > next_max_branch:
                if cur_branch > max_branch:
                    next_max_branch = max_branch
                    max_branch = cur_branch
                else:
                    next_max_branch = cur_branch

        if max_branch + next_max_branch + 1 > self.max_diameter:
            self.max_diameter = max_branch + next_max_branch + 1

        return max_branch + 1
--------------------------------------------------------------

class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:    
        """
        DFS Graph
		
		Complexities: 
			Time: O(N), N - number of nodes
            Space: O(N), N - number of nodes
        """
        
        def _dfs(node: int = 0) -> int:  
            nonlocal diameter
            
            top1_distance, top2_distance = 0, 0
            distance = 0
                        
            for next_node in graph[node]:
                distance = 1 + _dfs(next_node)
                
                if distance > top1_distance:
                    top1_distance, top2_distance = distance, top1_distance
                    
                elif distance > top2_distance:
                    top2_distance = distance
                    
            diameter = max(diameter, top1_distance + top2_distance)
            
            return top1_distance
                
                
        N = len(edges)
        graph = {node: [] for node in range(N + 1)}
        diameter = 0
        
        for node, connect in edges:
            graph[node].append(connect)
            
        _dfs()
        
        return diameter
----------------------------------------------------------------

class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        
        
        graph = defaultdict(list)
        
        for a, b in edges:
            
            graph[a].append(b)
            graph[b].append(a)
            
        
        
        def bfs(root):
            
            seen = set()
            seen.add(root)
            
            stack = deque([(root, 0)])
            
            while stack:
                item, dist = stack.popleft()
                
                
                for ch in graph[item]:
                    if ch not in seen:
                        seen.add(ch)
                        stack.append((ch, dist + 1))
                        
            return item, dist
        
        B, dist1 = bfs(edges[0][0])
        
        C, dist2 = bfs(B)
        
        return dist2
--------------------------------------------------------      
      
      
      
