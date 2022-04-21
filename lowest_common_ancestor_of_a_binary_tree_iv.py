'''
Given the root of a binary tree and an array of TreeNode objects nodes, return the lowest common ancestor (LCA) of all the nodes in nodes. All the nodes will exist in the tree, and all values of the tree's nodes are unique.

Extending the definition of LCA on Wikipedia: "The lowest common ancestor of n nodes p1, p2, ..., pn in a binary tree T is the lowest node that has every pi as a descendant (where we allow a node to be a descendant of itself) for every valid i". A descendant of a node x is a node y that is on the path from node x to some leaf node.
'''

Algo
Traverse the tree depth-first in post order.

Implementation

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        nodes = set(nodes)
        
        def fn(node):
            """Return LCA of nodes."""
            if not node or node in nodes: return node 
            left, right = fn(node.left), fn(node.right)
            return node if left and right else left or right
        
        return fn(root)
-----------------------------------------------------

Explanation
Basically a variation of the first official solution of LeetCode 236
Implementation
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        s = set(nodes)
        ans = None
        def dfs(node):
            nonlocal ans
            if not node:
                return False
            left = dfs(node.left)
            right = dfs(node.right)
            mid = node in s
            if left + right + mid >= 2:
                ans = node
            return left or right or mid    
        dfs(root)
        return ans if ans else nodes[0]
--------------------------------------------------------------------

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        
        def dfs(node):
            nonlocal nodes
            if not node or node in nodes:
                return node
            
            left = dfs(node.left)
            right = dfs(node.right)
            if left and right:
                return node
            else:
                return left or right
            
        return dfs(root)
------------------------------------------------------------------------------------

def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        def search(root, nodes):
            if not root:
                return 
            if root in nodes:
                return root
            left = search(root.left, nodes)
            right = search(root.right, nodes)
            if left and right:
                return root
            return left if left else right
        return search(root, nodes)

------------------------------------------------

def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        nodes = set(nodes)
        def dfs(node=root):
            if node:
                left, right = dfs(node.left), dfs(node.right)
                return node if node in nodes or (left and right) else left or right
        return dfs()
      
      
      
      
      
