'''
For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.

Given the roots of two binary trees root1 and root2, return true if the two trees are flip equivalent or false otherwise.
'''

class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 or not root2:
            return not root1 and not root2
        if root1.val != root2.val: return False
        return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) or (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))
      
-----------------------------------------------------------------------------------

def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
	@lru_cache(None)
	def dfs(n1, n2):
		if not(n1 or n2):
			return True
		if not(n1 and n2) or n1.val != n2.val:
			return False
		if((n1.left and n2.left) or (n1.right and n2.right)):
			return (dfs(n1.left, n2.left) and dfs(n1.right, n2.right)) or (dfs(n1.right, n2.left) and dfs(n1.left, n2.right))        
		else:
			return dfs(n1.right, n2.left) and dfs(n1.left, n2.right)
	return dfs(root1, root2)

---------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        '''
        We think of root1 as the "match" tree, that we are looking to match 
        by flipping parts of root2, the "flipper".
        
        We want to traverse the match, while trying a flip and a non-flip at each node in the flipper.
        This makes sure we try every combination of flips, and exit early when they don't match.
        Recursively do this.
        If the regular version matches or the flipped version matches, we return true.
        '''
        
        def dfs(match, flipper):
            
            # Both are None.
            if not match and not flipper:
                return True
            
            # Only one is None, so they don't match.
            if not (match and flipper):
                return False
            
            # They both exist, but values don't match.
            if match.val != flipper.val:
                return False
            
            # No flip.
            regular = dfs(match.left, flipper.left) and dfs(match.right, flipper.right)
            
            # Flip.
            flipped = dfs(match.left, flipper.right) and dfs(match.right, flipper.left)
            
            return regular or flipped
        
        return dfs(root1, root2)
-------------------------------------------------------------------------
Iterative DFS
class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        queue = deque([(root1, root2)])
        while queue:
            node1, node2 = queue.pop()
            if (not node1) and (not node2):
                continue
            elif (not node1) or (not node2) or (node1.val != node2.val):
                return False
            L1, R1, L2, R2 = node1.left, node1.right, node2.left, node2.right
            if (L1 and L2 and L1.val == L2.val) or (R1 and R2 and R1.val == R2.val):
                queue.append((L1, L2))
                queue.append((R1, R2))
            else:
                queue.append((L1, R2))
                queue.append((L2, R1))
        return True
Recursive DFS
class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(node1 = root1, node2 = root2):
            if (not node1) and (not node2):
                return True
            elif (not node1) or (not node2) or (node1.val != node2.val):
                return False
            L1, R1, L2, R2 = node1.left, node1.right, node2.left, node2.right
            if (L1 and L2 and L1.val == L2.val) or (R1 and R2 and R1.val == R2.val):
                return dfs(L1, L2) and dfs(R1, R2)
            else:
                return dfs(L1, R2) and dfs(L2, R1)
        return dfs()
