'''
Given the root of a binary tree, the depth of each node is the shortest distance to the root.

Return the smallest subtree such that it contains all the deepest nodes in the original tree.

A node is called the deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is a tree consisting of that node, plus the set of all descendants of that node.
'''

class Solution:
    def findDepth(self, node):
        if not node:
            return 0
        return 1 + max(self.findDepth(node.left), self.findDepth(node.right))
    
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if self.findDepth(root.left) == self.findDepth(root.right):
            return root
        elif self.findDepth(root.left) > self.findDepth(root.right):
            return self.subtreeWithAllDeepest(root.left)
        else:
            return self.subtreeWithAllDeepest(root.right)
          
-----------------------------------------------------------------------------

    def subtreeWithAllDeepest(self, root):
        def deep(root):
            if not root: return 0, None
            l, r = deep(root.left), deep(root.right)
            if l[0] > r[0]: return l[0] + 1, l[1]
            elif l[0] < r[0]: return r[0] + 1, r[1]
            else: return l[0] + 1, root
        return deep(root)[1]
