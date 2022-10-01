'''
You are given the root of a binary tree with unique values, and an integer start. At minute 0, an infection starts from the node with value start.

Each minute, a node becomes infected if:

The node is currently uninfected.
The node is adjacent to an infected node.
Return the number of minutes needed for the entire tree to be infected.
'''


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list)
        
        def build_graph(parent, node):
            if not node: return 
            
            if parent:
                graph[parent.val].append(node)
                graph[node.val].append(parent)
            
            build_graph(node, node.left)
            build_graph(node, node.right)
        
        build_graph(None, root)
        
        vis = set()
        max_infection = 0
        queue = deque([(start, 0)])
        vis.add(start)
        
        while queue:
            node_val, time = queue.popleft()
            max_infection = max(max_infection, time)
            
            for nei in graph[node_val]:
                if nei.val not in vis:
                    vis.add(nei.val)
                    queue.append((nei.val, time + 1))
        
        return max_infection
