'''
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
'''


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if root.val == key:
            if not (root.right or root.left):
                del root
                return None
            
            elif root.left and not root.right:
                return root.left
            
            elif not root.left and root.right:
                return root.right
           
            else:
                NewRoot = cur = root.right
                while cur.left:
                    cur = cur.left
                cur.left = root.left
                
                return NewRoot
            
        if root.val > key: 
            root.left = self.deleteNode(root.left,key)  # Recursion on left subtree
        if root.val < key: 
            root.right = self.deleteNode(root.right,key)  # Recursion on right subtree
        return root
