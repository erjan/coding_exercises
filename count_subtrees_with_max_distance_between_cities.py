'''
There are n cities numbered from 1 to n. You are given an array edges of size n-1, where edges[i] = [ui, vi] represents a bidirectional edge between cities ui and vi. There exists a unique path between each pair of cities. In other words, the cities form a tree.

A subtree is a subset of cities where every city is reachable from every other city in the subset, where the path between each pair passes through only the cities from the subset. Two subtrees are different if there is a city in one subtree that is not present in the other.

For each d from 1 to n-1, find the number of subtrees in which the maximum distance between any two cities in the subtree is equal to d.

Return an array of size n-1 where the dth element (1-indexed) is the number of subtrees in which the maximum distance between any two cities is equal to d.

Notice that the distance between the two cities is the number of edges in the path between them.
'''

class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        def bfs(source, verticies):
            q = collections.deque()
            q.append((source, 0))
            visited = set()
            visited.add(source)
            
            while q:
                furthest_node, furthest_dist = node, dist = q.popleft()
                for nei in adj[node]:
                    if nei in verticies and nei not in visited:
                        q.append((nei, dist+1))
                        visited.add(nei)
                        
            
            return furthest_node, furthest_dist, visited
        
        def get_diameter(bitmask, counter):
            if counter < 2:
                return
            
            # check if all 1's are connected, if not return
            set_of_verticies = set()
            for vertex, is_set in enumerate(bitmask):
                if is_set:
                    set_of_verticies.add(vertex)
                    source = vertex
                    
            farthest_node, _, visited_nodes_set = bfs(source, set_of_verticies)
            if len(visited_nodes_set) < len(set_of_verticies):
                return  # not connected
            
            visited_nodes_set.clear()
            _, diam, _ = bfs(farthest_node, set_of_verticies)
            ans[diam]+=1
            return
        
        
        def dfs(start_idx, counter):
            if start_idx > n:
                get_diameter(bitmask, counter)
                return
            
            # do not set start_idx to 1
            dfs(start_idx+1, counter)
            
            # set start_idx to 1
            bitmask[start_idx] = 1
            dfs(start_idx+1, counter+1)
            
            # revert start_idx
            bitmask[start_idx] = 0
     
        adj = collections.defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
           
        ans = [0] * n
        bitmask = [0] * (n+1)
        counter = 0 
        dfs(1, 0)

        return ans[1:]
