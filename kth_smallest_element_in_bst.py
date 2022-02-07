# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# my own solution

class Solution:    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        main = list()
        def trav(root):
            if not root:
                return []
            else:
                main.append(root.val)
                trav(root.left)
                trav(root.right)
                
        trav(root)
        main.sort()
        print(main)
        return main[k-1]
        
