'''
In a binary tree, a lonely node is a node that is the only child of its parent node. The root of the tree is not lonely 
because it does not have a parent node.

Given the root of a binary tree, return an array containing the values of all lonely nodes in the tree. Return the list in any order.
'''



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        
        total = list()
        
        def dfs(root):
            
            if not root:
                return 
        
            if not root.left and not root.right:
                return 
            
            elif root.left and not root.right:
                total.append(root.left.val) 
                dfs(root.left)

            elif root.right and not root.left:
                total.append(root.right.val) 
                dfs(root.right)
   
            else:
                dfs(root.left)
                dfs(root.right)

        dfs(root)
        
        print(total)
        
        return total


