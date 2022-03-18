'''
Given the root of a binary tree, return the sum of values of its deepest leaves.

'''
#bfs

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        #bfs
        
        q = [root]
        ans = 0
        cur = 0
        qlen = 0
        
        while len(q):
            
            qlen = len(q)
            ans = 0
            
            for _ in range(qlen):
                
                cur = q.pop(0)
                
                ans += cur.val
                
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
        return ans
            
        
                
                
                
