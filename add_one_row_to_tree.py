'''
Given the root of a binary tree and two integers val and depth, add a row of nodes with value val at the given depth depth.

Note that the root node is at depth 1.

The adding rule is:

Given the integer depth, for each not null tree node cur at the depth depth - 1, create two tree 
nodes with value val as cur's left subtree root and right subtree root.
cur's original left subtree should be the left subtree of the new left subtree root.
cur's original right subtree should be the right subtree of the new right subtree root.
If depth == 1 that means there is no depth depth - 1 at all, then create a tree node with 
value val as the new root of the whole original tree, and the original tree is the new root's left subtree.
'''


class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1: return TreeNode(v, root, None)
        elif d == 2:
            root.left = TreeNode(v, root.left, None)
            root.right = TreeNode(v, None, root.right)
        else:
            if root.left: self.addOneRow(root.left, v, d-1)
            if root.right: self.addOneRow(root.right, v, d-1)
        return root
      
----------------------------------------------------------------------------
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int, side = "left") -> TreeNode:
        if d == 1:
            res = TreeNode(v)
            setattr(res, side, root)
            return res
        if root:
            root.left = self.addOneRow(root.left, v, d - 1)
            root.right = self.addOneRow(root.right, v, d - 1, 'right')
        return root
