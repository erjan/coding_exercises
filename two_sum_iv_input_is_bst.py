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
     
    
    
#another solution from discussions
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False

        return self._findTarget(root, set(), k)
    
    def _findTarget(self, node, nodes, k):
        if not node:
            return False

        complement = k - node.val
        if complement in nodes:
            return True
          
          
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        stack, seen = [root], set()
        
        while stack:
            curr = stack.pop()
            # If we've seen k - curr.val,
            # we have k - curr.val + curr.val = k
            if k - curr.val in seen:
                return True
            seen.add(curr.val)
            
            # Visit children
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
                
        return False          

        nodes.add(node.val)

        return self._findTarget(node.left, nodes, k) or self._findTarget(node.right, nodes, k)        
        
