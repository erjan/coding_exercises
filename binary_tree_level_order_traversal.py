'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque

class Solution:
   
            
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        
        q = deque( [root] if root else [])
        
        while len(q):
            
            qlen = len(q)
            row = []
            
            for _ in range(qlen):
                cur = q.popleft()
                row.append(cur.val)
                
                if cur.left: 
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            
            res.append(row)
            
        return res
        
-----------------------------------------------------------------------------------------
  def levelOrder(self, root):
        res = []
        self.dfs(root, 0, res)
        return res
        
    def dfs(self, root, level, res):
        if not root:
            return 
        if len(res) < level+1:
            res.append([])
        res[level].append(root.val)
        self.dfs(root.left, level+1, res)
        self.dfs(root.right, level+1, res)
        
        
