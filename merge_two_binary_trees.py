#RECURSIVE SOLUTION
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, r1: Optional[TreeNode], r2: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(r1,r2):            
            if  r1 is None and r2 is None:
                return None

            if r1 is not None and r2 is None:
                return r1
         
            if r1 is None and r2 is not None:
                return r2

            if r1 is not None and r2 is not None:
                x = TreeNode(r1.val+r2.val)
                x.left = helper(r1.left, r2.left) 
                x.right =  helper(r1.right, r2.right)
            return x
        
        return helper(r1,r2)
        
      
#iterative solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root1:
            return root2
        if not root2:
            return root1

        q = deque([(root1,root2)])

        while q:
            cur1, cur2 = q.pop()

            if cur1.left and cur2.left:
                q.append((cur1.left, cur2.left))

            elif not cur1.left:
                cur1.left = cur2.left

            if cur1.right and cur2.right:
                q.append((cur1.right, cur2.right))

            elif not cur1.right:
                cur1.right = cur2.right

            cur1.val = cur1.val + cur2.val

        return root1
       
        
