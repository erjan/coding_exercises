#Given the root of a binary tree, return the preorder traversal of its nodes' values.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            return  [root.val] +self.preorderTraversal(root.left)  + self.preorderTraversal(root.right)
        else:
            return []
          
          
# dont make mistake! [root] vs [root.val]          
          
          
          
