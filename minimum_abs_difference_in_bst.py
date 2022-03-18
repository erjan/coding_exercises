'''
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return None                
        def get(root, res):
            if not root:
                return None
            
            get(root.left,res)
            res.append(root.val)
            get(root.right, res)            
        res = []
        get(root,res)
        diff = float('inf')
        
        
        for i in range(len(res)-1):
            if res[i+1]- res[i] < diff:
                diff = res[i+1] - res[i]
        
        return diff
        
        
