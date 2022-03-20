'''
You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.

For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.

The test cases are generated so that the answer fits in a 32-bits integer.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return []
        res = []
        stack = [(root, "")]
        while stack:
            node,path = stack.pop()
            if not node:
                continue
            if not node.right and not node.left:
                res.append( "{}{}".format(path, node.val))
            else:
                stack.append( (node.left, path + str(node.val) ))
                stack.append( (node.right, path + str(node.val) ))
        #return res
    
        total = 0
        
        print(len(res))
        print('ok')
        
        for i in range(len(res)):
            
            temp = int(res[i],2)
            total += temp
        return total
            
            
