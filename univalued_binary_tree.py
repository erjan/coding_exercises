'''
A binary tree is uni-valued if every node in the tree has the same value.

Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        main = root.val
        def check(root, main):
   
            if root:
                if root.val!= main:
                    return False
                
                if not check(root.right,main) or not check(root.left,main):
                    return False
            return True
            
        
        result = check(root,main)
        return result
        
#from discussions        
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        if root.left and root.val != root.left.val:
            return False
            
        if root.right and root.val != root.right.val:
            return False
        
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)        
