'''
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#my own solution!!!!

class Solution:
    
    main = []
    
    def helper(self,root, acc):
        if not root:
            return 
        elif root is not None and root.left is None and root.right is None:
            acc += str(root.val)
            self.main.append(acc)
        else:
            acc = acc + str(root.val) + "->"
            self.helper(root.left, acc )
            self.helper(root.right, acc ) 
            
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        self.main = []
        res = self.helper(root, "")  
        
        print(self.main)
        
        
        res = []
        for i in range( len(self.main)):
            el = self.main[i]
            el = el.split('->')
            el = list(map(lambda x: int(x),el))
            
            if sum(el) == targetSum:
                res.append(el)
        return res
            
            
    
