'''
Given a binary tree root and an integer target, delete all the leaf nodes with value target.

Note that once you delete a leaf node with value target, if its 
parent node becomes a leaf node and has the value target, it should also be deleted (you need to continue doing that until you cannot).
'''


class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if root:
            root.left = self.removeLeafNodes(root.left, target)
            root.right = self.removeLeafNodes(root.right, target) 
            if root.val == target and not root.left and not root.right:
                root = None
        return root 
