'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#my own solution
import sys
class Solution:
    
    min_len = sys.maxsize
    
    def helper(self,root, acc):
        if not root:
            return 0
        elif root is not None and root.left is None and root.right is None:
            acc += 1
            if acc < self.min_len:
                self.min_len = acc
        else:
            acc = acc + 1
            self.helper(root.left, acc )
            self.helper(root.right, acc )    
            
    def minDepth(self, root: Optional[TreeNode]) -> int:
                
        if root is None:
            return 0
        res = self.helper(root, 0)  
        return self.min_len

    
#another great readable solution: not mine

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def helper(root):
            
            if not root:
                return 0
            if not root.right and not root.left:
                return 1
            if not root.left and root.right:
                return 1 + helper(root.right)
            if root.left and not root.right:
                return 1 + helper(root.left)
            if root.left and root.right:
                return min( helper(root.right)+1 , helper(root.left)+1)
            
        return helper(root) if root else 0
