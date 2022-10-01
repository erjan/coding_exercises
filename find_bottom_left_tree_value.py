'''
Given the root of a binary tree, return the leftmost value in the last row of the tree.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        curlevel = [root]
        while curlevel:
            leftmost = curlevel[0]
            nxtlevel = []
            for i in range(len(curlevel)):
                v = curlevel[i]
                if v.left: nxtlevel.append(v.left)
                if v.right: nxtlevel.append(v.right)
            curlevel = nxtlevel
        return leftmost.val
--------------------------------------------------------------------------------    

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        
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
            
        return res[-1][0]
      
---------------------------------------------------------------------------------------------
def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
    last_left, last_row = 0, -1

    stack = [(root, 0)]
    while stack:
        cur_node, row = stack.pop()

        if row > last_row:
            last_row = row
            last_left = cur_node.val

        if cur_node.right:
            stack.append((cur_node.right, row + 1))

        if cur_node.left:
            stack.append((cur_node.left, row + 1))

    return last_left
---------------------------------------------------------
def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
    self.last_left, self.last_row = 0, -1

    def dfs(cur_node: Optional[TreeNode], cur_row: int):
        if not cur_node:
            return

        if cur_row > self.last_row:
            self.last_row = cur_row
            self.last_left = cur_node.val

        dfs(cur_node.left, cur_row + 1)
        dfs(cur_node.right, cur_row + 1)

    dfs(root, 0)

    return self.last_left
  
---------------------------------------------------------------------------------
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        
        res = [root.val, 0]
        self.search(root, res, 0)
        return res[0]
    
    def search(self, node, res, curDepth):
        
        if node:
            if curDepth > res[1]:
                res[0], res[1] = node.val, curDepth
            
            self.search(node.left, res, curDepth+1)
            self.search(node.right, res, curDepth+1)
  
