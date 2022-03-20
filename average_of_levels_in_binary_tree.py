'''
Given the root of a binary tree, return 
the average value of the nodes on each 
level in the form of an array. Answers within 10-5 of the actual answer will be accepted.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return
        
        q = [root]
        res = []
        
        while len(q):
            qlen = len(q)
            row = 0
            for i in range(qlen):
                cur = q.pop(0)
                row += cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            res.append(row/qlen)
        return res
