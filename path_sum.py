'''
Given the root of a binary tree and an integer targetSum, return true if the 
tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
'''
#my own solution with accumulator value

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def check(self,root, target, targetSum):
        if root is not None and targetSum == (target + root.val) and root.left is None and root.right is None:
            return True
        
        elif root is not None and root.left is None and root.right is None and targetSum != (target + root.val):
            return False  
        
        elif root is None:
            return False
        else:
            return self.check(root.left,target + root.val, targetSum) or self.check(root.right,target + root.val,targetSum)
                        
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        return self.check(root, 0, targetSum)        
# much better solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if root is None:
            return False
        elif not root.left and not root.right and root.val== targetSum:
            return True
        targetSum = targetSum - root.val
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
        
        
