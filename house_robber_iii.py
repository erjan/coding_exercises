 '''
 The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.

Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.

Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.
'''
  
we construct a dp tree, each node in dp tree represents [rob the current node how much you gain, skip the current node how much you gain]
dp_node[0] =[rob the current node how much you gain]
dp_node[1] =[skip the current node how much you gain]
we start the stolen from the leaf: Depth First Search
for each node you have 2 opitions:
option 1: rob the node, then you can't rob the child of the node.
dp_node[0] = node.val + dp_node.left[1] +dp_node.right[1]
option 2: skip the node, then you can rob or skip the child of the node.
dp_node[1] = dp_node.left[0] + dp_node.right[0]
the maximum of gain of the node depents on max(dp_node[0],dp_node[1])
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    Input: [3,4,5,1,3,null,1]
 input tree            dp tree:
     3                  [3+3+1,4+5]
    / \                /        \
   4   5            [4,3]      [5,1]
  / \   \          /     \          \
 1   2   1      [1,0]    [2,0]     [1,0]
                / \       /  \        /  \
           [0,0] [0,0] [0,0] [0,0]  [0,0] [0,0]
    
    """
    def rob(self, root: TreeNode) -> int:
        return max(self.dfs(root))
    
    def dfs(self, root: TreeNode):
        if not root:
            return (0, 0)
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        return (root.val + left[1] + right[1], max(left[0], left[1]) + max(right[0], right[1]))
      
------------------------------------------------------------------------------------------------------      
  
def rob(self, root):
        def with_without_rob(root):

            if root :
                with_l, without_l = with_without_rob(root.left)
                with_r, without_r = with_without_rob(root.right)        
                return (root.val + without_l + without_r, max(with_l, without_l) + max(with_r, without_r))
            return (0, 0)
            
        return max(with_without_rob(root))
