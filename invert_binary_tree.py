# Given the root of a binary tree, invert the tree, and return its root.


# I SOLVED IT MYSELF!

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        elif root.left and root.right:
            tmp = root.left
            root.left = root.right
            
            root.right = tmp            
        
        elif root.left and not root.right:
            root.right = root.left
            root.left = None
        elif not root.left and root.right:
            root.left = root.right
            root.right = None
            
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root
        
            
        
        

