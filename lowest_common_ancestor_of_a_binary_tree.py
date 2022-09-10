'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of 
LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p 
and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
'''
-----------------------------------------------------------------
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None or root == p or root == q:
            return root
        
		# Find p/q in left subtree
        l = self.lowestCommonAncestor(root.left, p, q)
		
		# Find p/q in right subtree
        r = self.lowestCommonAncestor(root.right, p, q)
        
		# If p and q found in left and right subtree of this node, then this node is LCA
        if l and r:
            return root
        
		# Else return the node which returned a node from it's subtree such that one of it's ancestor will be LCA
        return l if l else r
    
-----------------------------------------------------------------------
def lowestCommonAncestor(self, root, p, q):
    stack = [root]
    parent = {root: None}
    while p not in parent or q not in parent:
        node = stack.pop()
        if node.left:
            parent[node.left] = node
            stack.append(node.left)
        if node.right:
            parent[node.right] = node
            stack.append(node.right)
    ancestors = set()
    while p:
        ancestors.add(p)
        p = parent[p]
    while q not in ancestors:
        q = parent[q]
    return q
