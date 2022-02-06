''
Given the root of a binary search tree, rearrange the tree in in-order so that the 
leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.
'''


# MY OWN SOLUTION!! 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            return self.inorderTraversal(root.left) + [root.val]+ self.inorderTraversal(root.right)
        else:
            return []            
            
    def increasingBST(self, root: TreeNode) -> TreeNode:
        d = self.inorderTraversal(root)
        #print(d)
        
        root = TreeNode(-1)
        cur = root
        for i in range(len(d)):
            tmp = cur
            cur = TreeNode(d[i])
            tmp.right = cur
            
        cur = cur.right        
        return root.right
    
            
        
