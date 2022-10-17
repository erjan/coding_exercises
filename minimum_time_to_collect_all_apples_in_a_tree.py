'''
Given an undirected tree consisting of n vertices numbered from 0 to n-1, which has some apples in their vertices. You spend 1 second to walk over one edge of the tree. Return the minimum time in seconds you have to spend to collect all apples in the tree, starting at vertex 0 and coming back to this vertex.

The edges of the undirected tree are given in the array edges, where edges[i] = [ai, bi] means that exists an edge connecting the vertices ai and bi. Additionally, there is a boolean array hasApple, where hasApple[i] = true means that vertex i has an apple; otherwise, it does not have any apple.
'''

    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        tree = defaultdict(list)
        
        for i,j in edges:
            tree[i].append(j)
			tree[j].append(i)
        
        def dfs(node, parent):
            
            res = 0
            
            for child in tree[node]:
				if child != parent:
					res += dfs(child,node)
        
            if hasApple[node] and node != 0:
                hasApple[parent] = True
                return res+2
            return res
            
        return dfs(0,0)
      
-----------------------------------------------------------------------------------------------------------
from collections import defaultdict

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        adjacency_list = defaultdict(list)
        
        # Build adjacency list to represent the tree
        for src_node, dst_node in edges:
            adjacency_list[src_node].append(dst_node)
            adjacency_list[dst_node].append(src_node)
        
        # Record of visited nodes
        visited = set()
        
        #------------------------------------------------------------------------------------
        def collect_in_dfs(cur_node):
            
            visited.add(cur_node)
            
            cost_of_collect = 0
            
            for child_node in adjacency_list[cur_node]:
                
                if child_node in visited:
                    # avoid repeated traversal
                    continue
                
                
                cost_from_child = collect_in_dfs(child_node)
                
                if cost_from_child or hasApple[child_node]:
                    # update cost of collection (i.e., cost of green arrows)
                    # The first +1 is for path from cur_node to child_node, and the second +1 is for going back.
					# Totally, +2

                    cost_of_collect += cost_from_child + 2
            
            return cost_of_collect
        
        #------------------------------------------------------------------------------------
        root_node_idx = 0
        return collect_in_dfs(cur_node=root_node_idx)
