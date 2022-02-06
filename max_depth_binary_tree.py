'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# yay i did it myself!!!!
class Solution:
    
    max_len = 0
    
    def helper(self,root, acc):
        if not root:
            return 0
        elif root is not None and root.left is None and root.right is None:
            acc += 1
            if acc > self.max_len:
                self.max_len = acc
        else:
            acc = acc + 1
            self.helper(root.left, acc )
            self.helper(root.right, acc )    
            
    def maxDepth(self, root: Optional[TreeNode]) -> int:
                
        if root is None:
            return 0
        res = self.helper(root, 0)  
        return self.max_len
      
        
