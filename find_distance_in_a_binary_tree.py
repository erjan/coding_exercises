'''
Given the root of a binary tree and two integers p and q, return the distance between the nodes of value p and value q in the tree.

The distance between two nodes is the number of edges on the path from one to the other.

 
 '''

Algo
Traverse the tree in post-order. Return 1) if p or q is found in the sub-tree, and 2) the distance from p or q to the current node (if found).
Btw, I think this problem deserves a "Medium" in difficulty.

Implementation

class Solution:
    def findDistance(self, root: TreeNode, p: int, q: int) -> int:
        
        def fn(node):
            """Traverse the tree post-order."""
            nonlocal ans 
            if not node: return False, -inf
            ltf, lv = fn(node.left)
            rtf, rv = fn(node.right)
            
            if node.val in (p, q) or ltf and rtf: 
                if ltf: ans += lv + 1
                if rtf: ans += rv + 1
                return True, 0
            return ltf or rtf, max(lv, rv) + 1
                
        ans = 0
        fn(root)
        return ans 
Analysis
Time complexity O(N)
Space complexity O(N)

Edited on 1/28/2021
Adding an alternative implementation via tri-color encoding.

return 0 for branches with no p or q;
return a negative distance for branches with a p or q;
return a positive distance for branches with both p and q.
class Solution:
    def findDistance(self, root: TreeNode, p: int, q: int) -> int:
        if p == q: return 0 # edge case 
        
        def fn(node): 
            """Return distance of p and q."""
            if not node: return 0 # boundary condition 
            left, right = fn(node.left), fn(node.right)
            if left > 0 or right > 0: return max(left, right)
            if left < 0 and right < 0: return -left - right
            if left < 0 or right < 0: return -min(left, right) if node.val in (p, q) else min(left, right)-1
            return -1 if node.val in (p, q) else 0
        
        return fn(root)
      
-------------------------------------------------

The Euler path is a useful tool to have for solving any LCA problem here is how it works:

Traverse the graph visiting root, left, root, right, root to make an Euler Path
The lowest common ancestor (LCA) is at the lowest depth node between p and q in the Euler Path

In this problem the distance between any two nodes is the sum of each node's distance from the LCA.
In the above example the LCA 5 is at depth 1, node 6 is at depth 2, and node 4 is at depth 3.
So the shortest path from node 6 to node 4 is (2 - 1) + (3 - 1) = 3.

class Solution:
    def findDistance(self, root: TreeNode, p: int, q: int) -> int:
        
        def euler(node, d):
            path.append(node.val)
            depth.append(d)
            if node.left:
                euler(node.left, d + 1)
                path.append(node.val)
                depth.append(d)
            if node.right:
                euler(node.right, d + 1)
                path.append(node.val)
                depth.append(d)
            
        path, depth = [], []
        euler(root, 0)
        i, j = sorted((path.index(p), path.index(q)))
        k = min(range(i, j+1), key = lambda k: depth[k])
        return depth[i] + depth[j] - 2 * depth[k]
------------------------------------------------------------

Explanation
Similar to 236. Lowest Common Ancestor of a Binary Tree
Starting DFS from top to bottom, return (distance_to_p, distance_to_q), for example
When p is met at p node, return (1, 0)
When q is met at q node, return (0, 1)
When distance_to_p (or distance_to_q) is greater than 0, meaning p (or q) is met in sub-tree, thus plus 1
In the following implementation:
x: distance to p
y: distance to q
Implementation
class Solution:
    def findDistance(self, root: TreeNode, p: int, q: int) -> int:
        if p == q: return 0                # edge case
        ans = sys.maxsize
        def dfs(node):
            nonlocal ans
            x = y = 0
            if not node: return x, y       # edge case
            if node.left:
                lx, ly = dfs(node.left)    # get x, y of left subtree
                x, y = x + lx, y + ly
            if node.right:    
                rx, ry = dfs(node.right)   # get x, y of left subtree
                x, y = x + rx, y + ry
            x += 1 if x else 0             # when x is met in subtree, plus 1
            y += 1 if y else 0             # when y is met in subtree, plus 1
            x += 1 if node.val == p else 0 # when p is met for the first time
            y += 1 if node.val == q else 0 # when q is met for the first time
            if x > 0 and y > 0 and x + y - 2 < ans:
                ans = x + y - 2            # update `ans` when above condition met
            return x, y
        dfs(root)
        return ans
--------------------------------------------------------

class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        parents = dict()
        # recursively build a data structure that holds each node's parent
        # O(n) time and space
        def recParents(node): 
            if node.left:
                parents[node.left.val] = node
                recParents(node.left)
            if node.right:
                parents[node.right.val] = node
                recParents(node.right)
        parents[root.val] = None
        
        recParents(root)
        
        # create list with values from node to root
        # O(h) time and space, where h is the height of the tree
        def getPath(val):
            ans = []
            ans.append(val)
            while parents[val] != None:
                ans.append(parents[val].val)
                val = parents[val].val
            return ans
                
        # use stack to find LCA (there are other ways to do it, but I wanted to give it a try ;))
        # O(h) time and space
        q_path = getPath(q)
        p_path = getPath(p)
        while p_path and q_path and p_path[-1] == q_path[-1]:
            p_path.pop()
            q_path.pop()
        
        # space and time complexity O(n + h) = O(n), since n is by definition bigger than or equal h. 
		# Smaller O(n) time not possible, since we have to visit all nodes in the worst case
        return len(q_path) + len(p_path)
-------------------------------------------------------------------

class Solution:
    def traversal(self, root, node2dist, target, res):
        if not root:
            return 0
        
        if root.val == target:
            if root.val in node2dist:
                res.append(node2dist[root.val] + 0)
                return 0
                
            node2dist[root.val] = 0
            return 1
        
        dist = self.traversal(root.left, node2dist, target, res)
        if dist == 0:
            dist = self.traversal(root.right, node2dist, target, res)
            if dist == 0:
                return 0

        if root.val in node2dist and len(res) == 0:
            res.append(node2dist[root.val] + dist)
            return 0
        
        node2dist[root.val] = dist
        
        return dist + 1
    
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        d = {}
        self.traversal(root, d, p, [])
        
        res = []
        self.traversal(root, d, q, res)
        
        return res[0]
    
      
      
      
