'''
Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.
'''


class Solution(object):
    def distanceK(self, root, target, K):
        
        # dfs preorder traversal to map each node to its parent
        def get_parent(node = root, parent = None):
            if not node: return
            hashmap[node] = parent
            get_parent(node.left, node), get_parent(node.right, node)
        
        def search(node = target, distance = 0):
            if not node or node.val in visited: return
            visited.add(node.val)
            if distance == K: answer.append(node.val)
            for neighbour in (hashmap[node], node.left, node.right):
                search(neighbour, distance+1)
        
        hashmap, answer, visited = {}, [], set()
        get_parent(), search()
        return answer
-------------------------------------------------------------------------------
class Solution:
    def convert_into_graph(self, node, parent, g):
        # To convert into graph we need to know who is the parent
        if not node:
            return
        
        if parent:
            g[node].append(parent)
            
        if node.right:
            g[node].append(node.right)
            self.convert_into_graph(node.right, node, g)
        
        if node.left:
            g[node].append(node.left)
            self.convert_into_graph(node.left, node, g)
        
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        g = defaultdict(list)
        vis, q, res = set(), deque(), []
        # We have a graph, now we can use simply BFS to calculate K distance from node.
        self.convert_into_graph(root, None, g)
        
        q.append((target, 0))
        
        while q:
            n, d = q.popleft()
            vis.add(n)
            
            if d == K:
                res.append(n.val)
            
            # adjacency list traversal
            for nei in g[n]:
                if nei not in vis:
                    q.append((nei, d + 1)) 
                
        return res
