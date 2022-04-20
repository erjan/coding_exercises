'''
Given the root of a binary tree, return true if you can partition the tree into two trees with equal sums of values after removing exactly one edge on the original tree.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        
        def get_sum(root, d):
            if not root:
                return 0
            
            l = get_sum(root.left, d)
            r = get_sum(root.right, d)
            
            sum = l+r+root.val
            d[sum] = d.get(sum, 0) + 1
            return sum
        
        d = {}
        total_sum = get_sum(root, d)
        
        if total_sum == 0:
            return d[0] >= 2
        
        return True if total_sum//2 in d and total_sum%2 == 0 else False
      
-----------------------------------------------------------

class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        
        def fn(node): 
            """Return sum of sub-tree."""
            if not node: return 0 
            ans = node.val + fn(node.left) + fn(node.right)
            freq[ans] += 1
            return ans
        
        freq = defaultdict(int)
        total = fn(root)
        return not total and freq[total] > 1 or total and total % 2 == 0 and freq[total//2]
----------------------------------------------------------------------------------------------------

class Solution:
    def checkEqualTree(self, root: TreeNode) -> bool:
        sums = set()
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if root.left: sums.add(left)
            if root.right: sums.add(right)
            return left + right + root.val
        total = dfs(root)
        return total % 2 == 0 and total//2 in sums
--------------------------------------------------------------------------------------------------

We can do 2 recursions:

We will recurse to find sum of the underlying tree for each node,
We will recurse to find node which has underlying tree of exactly half of the sum of entire initial tree.
class Solution:
    def checkEqualTree(self, root: 'TreeNode') -> bool:
        def helper(root: 'TreeNode') -> bool:
            if root is None:
                return
            if root.left is None and root.right is None:
                root.sum = root.val
            left = helper(root.left)
            right = helper(root.right)
            root.sum = left + right + root.val
        def search(root: 'TreeNode', num: int) -> bool:
            if root is None:
                return False
            if root.sum == num:
                return True
            return search(root.left, num) or search(root.right, num)
                
            
        helper(root)
        return search(root.left, root.sum / 2) or search(root.right, root.sum / 2)
------------------------------------------------

Sum up all vals of nodes in the tree as total and store every sums of subtrees except the whole one in a set seen. Simply check if there exists any sum of a subtree is equal to the half of total. Here is my code:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        def sum_up(node):
            res = 0
            if node:
                res = node.val + sum_up(node.left) + sum_up(node.right)
                seen.add(res)
            return res
        
        seen = set()
        # to handle the case when total == 0, don't put it in seen
        total = sum_up(root.left) + sum_up(root.right) + root.val
        return (total // 2) in seen
      
      
