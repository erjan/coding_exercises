'''
Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the preorder traversal way, and return it.

Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the original binary tree.
'''

#my own solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        s = root
        if s and s.left is None and s.right is None:
            return str(s.val)
        if not s:
            return ""

        if s.left == None and s.right is None:
            return s.val

        left = self.tree2str(s.left)
        right = self.tree2str(s.right)

        if right == "":
            return str(s.val) + "(" + str(left) + ")"
        else:
            return str(s.val) + "(" + str(left) + ")" + "(" + str(right) + ")"
