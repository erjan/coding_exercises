'''
Given the root of a binary tree, return the number of nodes where the value of the node is equal to the sum of the values of its descendants.

A descendant of a node x is any node that is on the path from node x to some leaf node. The sum is considered to be 0 if the node has no descendants.
'''


class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        
        def fn(node):
            """Return sum of nodes' value on sub-tree."""
            nonlocal ans
            if not node: return 0 
            sm = fn(node.left) + fn(node.right)
            if sm == node.val: ans += 1
            return sm + node.val 
        
        ans = 0 
        fn(root)
        return ans
      
----------------------------------
def equalToDescendants(root):
    """
    :type root: Optional[TreeNode]
    :rtype: int
    """
    from functools import lru_cache
    @lru_cache(maxsize = None)
    def get_sum_des(node):
        # gives the sum of the node + its descendents - so if you want only sum of descendents you need to subtract the node.val itself - see *
        if not node:
            return 0
        else:
            return node.val + get_sum_des(node.right) + get_sum_des(node.left)

    cnt = 0
    stack = [root]
    while stack:
        node = stack.pop()
        if get_sum_des(node) - node.val == node.val: # <- see *
            cnt += 1
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
            
    return cnt
  
  --------------------------------------
  def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        count = 0
        def dfs(node=root):
            if not node:
                return 0
            nonlocal count
            sum_ = dfs(node.left)+dfs(node.right)
            count += sum_ == node.val
            return sum_+node.val
        dfs()
        return count
      
----------------------------------------------------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        
        res = 0
        def helper(root):
            nonlocal res
            if root == None:
                return 0
            
            if root.left == root.right == None:
                res += 1 if root.val == 0 else 0
                return root.val
            
            left_sum = helper(root.left)
            right_sum = helper(root.right)
            
            if root.val == left_sum + right_sum:
                res += 1
            return right_sum + left_sum + root.val
        helper(root)
        return res
        
        
        
