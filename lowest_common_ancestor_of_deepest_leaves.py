'''
Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.

Recall that:

The node of a binary tree is a leaf if and only if it has no children
The depth of the root of the tree is 0. if the depth of a node is d, the depth of each of its children is d + 1.
The lowest common ancestor of a set S of nodes, is the node A with the largest depth such that every node in S is in the subtree with root A.
'''

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def post_order(root):
            if not root:
                return 0, None
            d1, n1 = post_order(root.left)
            d2, n2 = post_order(root.right)
            if d1 == d2:
                return d1+1, root
            elif d1 > d2:
                return d1+1, n1
            else:
                return d2+1, n2
            
        d, n = post_order(root)
        return n
      
--------------------------------------------------

class Solution:
    def ht(self, node):
        if not node:
            return 0
        return max(self.ht(node.left), self.ht(node.right)) + 1
    
    def dfs(self, node):
        if not node:
            return None
        left, right = self.ht(node.left), self.ht(node.right)
        if left == right:
            return node
        if left > right:
            return self.dfs(node.left)
        if left < right:
            return self.dfs(node.right)

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.dfs(root)
      
-------------------------------------------------------------------      
