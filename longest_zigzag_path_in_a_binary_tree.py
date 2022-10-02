'''
You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:

Choose any node in the binary tree and a direction (right or left).
If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
Change the direction from right to left or from left to right.
Repeat the second and third steps until you can't move in the tree.
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.
'''


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        res = 0
        if not root: return res
        q= deque() # node, isLeft, depth
        if root.left: 
            q.append((root.left,True,1))
        if root.right:
            q.append((root.right, False,1))
        
        while q:
            node,isleft,depth = q.popleft()
            res = max(res,depth)
            if isleft:
                if node.right: 
                    q.append((node.right,False,depth+1))
                if node.left:
                    q.append((node.left,True,1))
                
            else:
                if node.left:
                    q.append((node.left,True,depth+1))
                if node.right:
                    q.append((node.right,False,1))
        return res
    
-----------------------------------------------------------------------------------------------------
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root.left,True,1)
        self.dfs(root.right,False,1)
        return self.res
    
    def dfs(self,node,isLeft,depth):
        if not node: return
        self.res = max(self.res,depth)
        
        if isLeft:
            self.dfs(node.left,True,1)
            self.dfs(node.right,False,depth+1)
        else:
            self.dfs(node.left,True,depth+1)
            self.dfs(node.right,False,1)
