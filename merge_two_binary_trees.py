# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, r1: Optional[TreeNode], r2: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(r1,r2):            
            if  r1 is None and r2 is None:
                return None

            if r1 is not None and r2 is None:
                return r1
         
            if r1 is None and r2 is not None:
                return r2

            if r1 is not None and r2 is not None:
                x = TreeNode(r1.val+r2.val)
                x.left = helper(r1.left, r2.left) 
                x.right =  helper(r1.right, r2.right)
            return x
        
        return helper(r1,r2)
        
      
    
