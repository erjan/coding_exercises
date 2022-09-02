
'''
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
'''


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        root = node
        if not root:
            return root
        

        q = deque([root])
        res = {}
        visited = set()

        
        while q:
            n = q.popleft()
            if n in visited:
                continue
                
            visited.add(n)
            
            if n not in res:
                res[n] = Node(n.val)

            for neb in n.neighbors:

                if neb not in res:

                    res[neb] = Node(neb.val)
                res[n].neighbors.append(res[neb])
                q.append(neb)   

        return res[node] 
