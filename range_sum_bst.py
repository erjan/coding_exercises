# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        self.total_s = 0
        
        def helper(root):
            if root is not None:
                if root.val > low:
                    helper(root.left)

                if low <= root.val <=high:
                    self.total_s += root.val

                if root.val < high:
                    helper(root.right)
                
        helper(root)
        return self.total_s
            
            
