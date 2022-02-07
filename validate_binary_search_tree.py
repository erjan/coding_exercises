'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            return self.inorderTraversal(root.left) + [root.val]+ self.inorderTraversal(root.right)
        else:
            return []
                  
                    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
         
        d = self.inorderTraversal(root)
        print(d)
        if len(d) == 1:
            return True
        for i in range(len(d)-1):
            if d[i+1] <= d[i]:
                return False
        return True
