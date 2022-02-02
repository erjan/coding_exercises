'''
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    main = []
    
    def helper(self,root, acc):
        if not root:
            return 
        elif root is not None and root.left is None and root.right is None:
            acc += str(root.val)
            self.main.append(acc)
        else:
            acc = acc + str(root.val)
            self.helper(root.left, acc )
            self.helper(root.right, acc ) 
            
    
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.main = []
        res = self.helper(root, "")  
        
        
        res = []
        total_sum = 0
        for i in range( len(self.main)):
            el = int(self.main[i])
            total_sum += el
        return total_sum
            
            
