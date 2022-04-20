'''
Given the root of a binary tree, find the largest subtree, which is also a Binary Search Tree (BST), where the largest means subtree has the largest number of nodes.

A Binary Search Tree (BST) is a tree in which all the nodes follow the below-mentioned properties:

The left subtree values are less than the value of their parent (root) node's value.
The right subtree values are greater than the value of their parent (root) node's value.
Note: A subtree must include all of its descendants.
'''

def largestBSTSubtree(self, root):
    def dfs(root):
        if not root:
            return 0, 0, float('inf'), float('-inf')
        N1, n1, min1, max1 = dfs(root.left)
        N2, n2, min2, max2 = dfs(root.right)
        n = n1 + 1 + n2 if max1 < root.val < min2 else float('-inf')
        return max(N1, N2, n), n, min(min1, root.val), max(max2, root.val)
    return dfs(root)[0]
My dfs returns four values:

N is the size of the largest BST in the tree.
If the tree is a BST, then n is the number of nodes, otherwise it's -infinity.
If the tree is a BST, then min and max are the minimum/maximum value in the tree.

---------------------------------------------------

class SubTree(object):
    def __init__(self, largest, n, min, max):
        self.largest = largest  # largest BST
        self.n = n              # number of nodes in this ST
        self.min = min          # min val in this ST
        self.max = max          # max val in this ST

class Solution(object):
    def largestBSTSubtree(self, root):
        res = self.dfs(root)
        return res.largest
    
    def dfs(self, root):
        if not root:
            return SubTree(0, 0, float('inf'), float('-inf'))
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        
        if root.val > left.max and root.val < right.min:  # valid BST
            n = left.n + right.n + 1
        else:
            n = float('-inf')
            
        largest = max(left.largest, right.largest, n)
        return SubTree(largest, n, min(left.min, root.val), max(right.max, root.val))
--------------------------------------------------

Helper function return three variables: Largest BST Subtree starting from this node, minimum node value and maximum node value


class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        return self.helper(root)[0]
    
    def helper(self, root):
        if not root:
            return 0, float("inf"), float("-inf")
        left_count, left_min, left_max = self.helper(root.left)
        right_count, right_min, right_max = self.helper(root.right)
        if left_max < root.val < right_min:
            return left_count + right_count + 1, min(left_min, root.val), max(right_max, root.val)
        return max(left_count, right_count), float("-inf"), float("inf")
      
-----------------------------------------------------------------

def largestBSTSubtree(self, root: TreeNode) -> int:
'''recursion with postorder traversal, TC: O(n), SC: O(n)'''
	self.res = 0
	def recur(node):
		if not node:
			return True, 0, float('inf'), float('-inf')
		bool_bst_l, n_nodes_l, min_val_l, max_val_l = recur(node.left)
		bool_bst_r, n_nodes_r, min_val_r, max_val_r = recur(node.right)
		if bool_bst_l and bool_bst_r and max_val_l<node.val<min_val_r:
			self.res = max(self.res, n_nodes_l+n_nodes_r+1)
			curr_min = min(node.val, min_val_l)
			curr_max = max(node.val, max_val_r)
			return True, n_nodes_l+n_nodes_r+1, curr_min, curr_max
		else:
			return False, 0, float('inf'), float('-inf')
	_,_,_,_ = recur(root)
	return self.res

def largestBSTSubtree(self, root: TreeNode) -> int:
    '''iterative with postorder traversal, TC: O(n), SC: O(n)'''
    if not root:
        return 0
    res = 0
    stack = [(root, False)]
    check = {None: (True, 0, float('inf'), float('-inf'))}
    while stack:
        curr, visited = stack.pop()
        if visited:
            bool_bst_l, n_nodes_l, min_val_l, max_val_l = check[curr.left]
            bool_bst_r, n_nodes_r, min_val_r, max_val_r = check[curr.right]
            if bool_bst_l and bool_bst_r and max_val_l<curr.val<min_val_r:
                res = max(res, n_nodes_l+n_nodes_r+1)
                curr_min = min(curr.val, min_val_l)
                curr_max = max(curr.val, max_val_r)
                check[curr] = (True, n_nodes_l+n_nodes_r+1, curr_min, curr_max)
            else:
                check[curr] = (False, 0, float('inf'), float('-inf'))  
        else:
            stack.append((curr, True))
            if curr.right:
                stack.append((curr.right, False))
            if curr.left:
                stack.append((curr.left, False))
    return res
  
  
      
