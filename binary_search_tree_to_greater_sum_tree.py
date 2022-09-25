'''
Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        cur_sum = 0
        def dfs(node):
            nonlocal cur_sum
            if not node:
                return                      
            dfs(node.right)         
            node.val += cur_sum      # Keep traverse until arrive at the right node, update value     
            cur_sum = node.val       # Remember the sum so far            
            dfs(node.left)           # Continue on the left node
            
        dfs(root)       
        return root
      
--------------------------------------------------------------------------------------------------------
class Solution:
    
    def reversed_order_traversal(self, node):
        if node is not None:
            yield from self.reversed_order_traversal(node.right)
            yield node
            yield from self.reversed_order_traversal(node.left)
    
    def bstToGst(self, root: TreeNode) -> TreeNode:
        current_sum = 0
        for node in self.reversed_order_traversal(root):
            current_sum += node.val
            node.val = current_sum
        return root
      
-------------------------------------------------------------------------------
class Solution:
    def bstToGst(self, root):
        total = 0
        stack = []
        n     = root
        
        while n or stack:
            if not n:
                n = stack.pop()
            else:
                while n.right:
                    stack.append(n)
                    n = n.right
            total += n.val
            n.val  = total
            n      = n.left
        return root
