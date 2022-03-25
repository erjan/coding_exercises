'''
Given the root of a Binary Search Tree and a target number k, return 
true if there exist two elements in the BST such that their sum is equal to the given target.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
                       
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
         
            if root:
                return inorderTraversal(root.left) + [root.val]+ inorderTraversal(root.right)
            else:
                return []
                    
                               
        a = inorderTraversal(root)
        
        l = 0
        r = len(a)-1
        
        while l < r:
            
            if a[l] + a[r] == k:
                return True
            
            elif a[l] + a[r] > k:
                r-=1
            elif a[l] + a[r] < k:
                l+=1
        return False
        
        
