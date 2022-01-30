'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
            
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if p and q:
            if p.val == q.val:
                if self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right):
                    return True
                else:
                    return False
        if p and not q:
            return False
        elif p and not p:
            return False
        elif p is None and q is None:
            return True
                
        
           
