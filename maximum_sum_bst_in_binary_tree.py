'''
Given a binary tree root, return the maximum sum of all keys of any sub-tree which is also a Binary Search Tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def dfs(root):
            if not root:
                return True, 0, float('inf'), float('-inf')
            lbst,lsum,lmin,lmax = dfs(root.left)
            rbst,rsum,rmin,rmax = dfs(root.right)
            
            if lbst and rbst and lmax <= root.val < rmin:
                self.res = max(self.res,(lsum+root.val+rsum))
                return True, (lsum+root.val+rsum), min(root.val,lmin),max(root.val,rmax)
            else:
                return False,0,0,0
        dfs(root)
        return self.res
        
                
-------------------------------------------------------------------------------------------------------------
def maxSumBST(self, root: Optional[TreeNode]) -> int:
	ans = [0]
	dp = dict()
	def summ(node):
		if(not node):
			return 0
		if(node in dp):
			return dp[node]
		dp[node] = node.val + summ(node.left) + summ(node.right)
		return dp[node]
		
	def dfs(node):
		if(node.left):
			l_min, l_max, isB_l = dfs(node.left)
			l = isB_l and l_max < node.val
		else:
			l_min = node.val
			l = 1
		if(node.right):
			r_min, r_max, isB_r = dfs(node.right)
			r = isB_r and r_min > node.val
		else:
			r_max = node.val
			r = 1
		if(l and r):
			ans[0] = max(ans[0], summ(node))
			return l_min, r_max, 1
		return -1, -1, 0

	_, _, f = dfs(root)
	if(f): ans[0] = max(ans[0], summ(root))
	return ans[0]

----------------------------------------------------------------------------------------------------------
class Solution:
    
    def find(self, node):
        if node is None:
            return 0, 0, inf, -inf
        
        l_best, l_sum, l_min, l_max = self.find(node.left)
        r_best, r_sum, r_min, r_max = self.find(node.right)
        l_min, r_max = min(node.val, l_min), max(node.val, r_max)
        
        if l_sum != -inf and r_sum != -inf and l_max < node.val < r_min:
            return max(l_best, r_best, l_sum + r_sum + node.val), l_sum + r_sum + node.val, l_min, r_max
        else:
            return max(l_best, r_best), -inf, l_min, r_max
        
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        return self.find(root)[0]
