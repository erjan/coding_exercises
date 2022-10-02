'''
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        
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
            
            res.append(max(row))
            
        return res
      
----------------------------------------------------------------------------------------

dfs

def largestValues(self, root: TreeNode) -> List[int]:
	res = []
	def dfs(node=root, level=0):
		if not node:
			return
		if len(res)-1 < level:
			res.append(node.val)
		else:
			res[level] = max(node.val, res[level])
		dfs(node.left, level+1)
		dfs(node.right, level+1)
	dfs()
	return res

bfs

    def largestValues(self, root: TreeNode) -> List[int]:
        queue = deque([root])
        res = []
        while queue:
            max_ = float('-inf')
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node:
                    continue
                max_ = max(max_, node.val)
                queue.extend([node.left, node.right])
            if max_ != float('-inf'):
                res.append(max_)
        return res
