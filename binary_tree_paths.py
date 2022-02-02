'''
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
            

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.main = []
        res = self.helper(root, "")  
        return self.main
      
