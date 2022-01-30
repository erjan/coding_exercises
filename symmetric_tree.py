# i started watching the solution on youtube, then did not watch to end and realized the solution!!! myself!!
# я начал смотреть решение на ютубе и не досмотрел - все равно сам сделал!

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
'''

class Solution:
    
    def helper(self,l,r):
        if l is None or r is None:
            if l == r:
                return True
            return False
        
        if l.val != r.val:
            return False
                
        if self.helper(l.right, r.left) == False or self.helper(l.left, r.right) == False:
            return False
        return True
        
        
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        return self.helper(root.left, root.right)
            
                        
      
        
    
                
        
