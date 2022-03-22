'''
Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        
        nums = []
        nodes = [root]
        
        while nodes:
            
            t = nodes.pop()
            
            nums.append(t.val)
            
            if t.left:
                nodes.append(t.left)
            if t.right:
                nodes.append(t.right)
        
        nums = set(nums)
        
        if len(nums) == 1:
            return -1
        
        return sorted(nums)[1]
      
      
#DFS
class Solution:
    
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.first = root.val
        self.second = math.inf
        
        def find_second(root):
            
            if not root:
                return 
            
            if self.first < root.val < self.second:
                self.second = root.val
                
            find_second(root.left)
            find_second(root.right)
            
        find_second(root)
        return -1 if self.second == math.inf else self.second
