#Given the root of a binary tree, return the postorder traversal of its nodes' values.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if root :
            return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
        
        # post order-root, left, right
        else:
            return []
          
          
#HUGE MISTAKE!!! i CODED [root] entire root, not [root.val]!!!
        
