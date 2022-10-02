'''
You are given the root of a binary tree with n nodes where each node in the tree has node.val coins. There are n coins in total throughout the whole tree.

In one move, we may choose two adjacent nodes and move one coin from one node to another. A move may be from parent to child, or from child to parent.

Return the minimum number of moves required to make every node have exactly one coin.
'''

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        self.rst = 0
        self.helper(root)
        return self.rst 
    
    
    def helper(self, root):
        if not root:
            return 0
        
        left = self.helper(root.left)
        right = self.helper(root.right)
        if root.left and root.left.val != 1:
            x = root.left.val - 1
            self.rst += abs(x)
            root.val += x
            root.left.val = 1
        if root.right and root.right.val != 1:
            x = root.right.val - 1
            self.rst += abs(x)
            root.val += x
            root.right.val = 1
