'''
Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.
'''

def maxAncestorDiff(root):
	self.ans = 0
	def dfs(node, a, b):
		if node:
			a, b = min(a, node.val), max(b, node.val)
			self.ans = max(self.ans, b-a)
			dfs(node.left, a, b), dfs(node.right, a, b)
	dfs(root, float('inf'), float('-inf'))
	return self.ans
-----------------------------------------------------------------------------------------------------------------------
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(root, mn, mx):
            # Base Case: If we reach None, just return 0 in order not to affect the result
            if not root: return 0
            
			# The best difference we can do using the current node can be found:
            res = max(abs(root.val - mn), abs(root.val - mx))
			
			# Recompute the new minimum and maximum taking into account the current node
            mn, mx = min(mn, root.val), max(mx, root.val)
			
			# Recurse left and right using the newly computated minimum and maximum
            return max(res, dfs(root.left, mn, mx), dfs(root.right, mn, mx))
        
        # Initialize minimum `mn` and maximum `mx` equals value of given root
        return dfs(root, root.val, root.val)
---------------------------------------------------------------------------------------------------------
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        
        if not root: return 0
        stack=[(root,root.val,root.val)] #node,parent,child
        res=0
        
        while stack:
            node,parent,child=stack.pop()
            res=max(res,abs(parent-child)) 
            if node.left:
                stack.append((node.left,max(parent,node.left.val),min(child,node.left.val)))
            if node.right:
                 stack.append((node.right,max(parent,node.right.val),min(child,node.right.val)))
        return res
