
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
    
    
-------------------------------------------------------------------------------------------------------------


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node:
            return node
        
        res = dict()
        visited = set()

        self.dfs(node,res,visited)
        return res[node]
    
    def dfs(self,node,res,visited):
        if node in visited:
            return
        
        visited.add(node)
        if node not in res:
            res[node] = Node(node.val)
        
        for node_ in node.neighbors:
            if node_ not in res:
                res[node_] = Node(node_.val)
            res[node].neighbors.append(res[node_])
            self.dfs(node_,res,visited)
      
-------------------------------------------------------------------------------------------------------------------------------

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        res = dict()
        visited = set()
        stack = deque([node])

        while stack:
            n = stack.pop()
            if n in visited:
                continue
            visited.add(n)

            if n not in res:
                res[n] = Node(n.val)
            for nebor in n.neighbors:
                if nebor not in res:
                    res[nebor] = Node(nebor.val)
                res[n].neighbors.append(res[nebor])
                stack.append(nebor)
                
        return res[node]
