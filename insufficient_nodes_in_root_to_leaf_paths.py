'''
Given the root of a binary tree and an integer limit, delete all insufficient nodes in the tree simultaneously, and return the root of the resulting binary tree.

A node is insufficient if every root to leaf path intersecting this node has a sum strictly less than limit.

A leaf is a node with no children.
'''

class Solution:
    # Time: O(n)
    # Space: O(H)
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        val = self.dfs(root, 0, limit)
        return None if val < limit else root
        
    def dfs(self, node, path_sum, limit):
        if not node:
            return path_sum
        l = self.dfs(node.left, path_sum + node.val, limit)
        r = self.dfs(node.right, path_sum + node.val, limit)
        if not node.left and not node.right:
            ret_val = path_sum + node.val
        elif not node.left:
            ret_val = r
        elif not node.right:
            ret_val = l
        else:
            ret_val = max(l, r)
            
        if l < limit:
            node.left = None
        if r < limit:
            node.right = None
        return ret_val
      
------------------------------------------------------------------
class Solution(object):
    def sufficientSubset(self, root, limit):
        """
        time: O(n)
        space: O(height)
        """
        if not root:
            return None
        val = self.helper(root, limit, root.val)
        if val < limit:
            return None
        else:
            return root
    
    def helper(self, root, limit, pathsum):
        if not root.left and not root.right:
            return pathsum
        
        if root.left:
            leftsum = self.helper(root.left, limit, pathsum+root.left.val)
            if leftsum < limit:
                root.left = None
            
        if root.right:
            rightsum = self.helper(root.right, limit, pathsum+root.right.val)
            if rightsum < limit:
                root.right = None
                
        if not root.left and not root.right:
            return float('-inf')
        if not root.left:
            return rightsum
        if not root.right:
            return leftsum
        return max(leftsum, rightsum)
-------------------------------------------------
class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int, pathSum = 0) -> TreeNode:
        if not root: return None
        if not root.left and not root.right:
            if pathSum + root.val < limit:
                return None
            return root
        root.left = self.sufficientSubset(root.left, limit, pathSum + root.val)
        root.right = self.sufficientSubset(root.right, limit, pathSum + root.val)
        if not root.left and not root.right:
            return None
        return root
      
