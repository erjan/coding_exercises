'''
Given the root of a binary tree, return the lowest 
common ancestor (LCA) of two given nodes, p and q. If either node p or q does not exist in the tree, return null. All values of the nodes in the tree are unique.

According to the definition of LCA on Wikipedia: 
"The lowest common ancestor of two nodes p and q in a binary tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)". A descendant of a node x is a node y that is on the path from node x to some leaf node.

 
 '''

Algo
Traverse the tree and return node that can potentially be the LCA of p and q together with a number x which indicates how many among p and q are seen in the tree.

Implementation

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def fn(node):
            """Return LCA of p and q in sub-tree rooted at node (if found)."""
            if node: 
                (ln, lx), (rn, rx) = fn(node.left), fn(node.right)
                if node in (p, q): return node, 1 + lx + rx
                if ln and rn: return node, lx + rx
                return (ln, lx) if ln else (rn, rx)
            return None, 0
            
        ans, x = fn(root)
        return ans if x == 2 else None 
-------------------------------------------------------------

Differing from 236, we need to count "found nodes".

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        not_found = len((p, q))
        
        def dfs(n: 'TreeNode') -> 'TreeNode':
            nonlocal not_found
            if not n:
                return n
            
            lca, rca = dfs(n.left), dfs(n.right)
            if n in (p, q):
                not_found -= 1
                return n

            return n if lca and rca else lca or rca
            
        r = dfs(root)
        return None if not_found else r
      
------------------------------------------------------------------------

check in advance if p and q exist in Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_exist = False
        q_exist = False
        stack = [root]
        while stack:
            node = stack.pop()
            
            if node:
                if node == p:
                    p_exist = True
                if node == q:
                    q_exist = True
                    
                stack.append(node.left)
                stack.append(node.right)
      
        if not p_exist:
            return None
        if not q_exist:
            return None
        

        def dfs(node):
            nonlocal p
            nonlocal q
            if not node or node == p or node == q:
                return node
            
            left = dfs(node.left)
            right = dfs(node.right)
            if left and right:
                return node
            else:
                return left or right
            
        return dfs(root)
---------------------------------------------------------------

This solution is pretty similar to the solution of Question 236. But here, we need to traverse the entire tree, because one of the given nodes may not present in the tree. So, if the stack becomes empty, we can conclude that one of the given nodes is not present, hence we can return null.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        parent = {root:None}
        
        while p not in parent or q not in parent:
            if not stack:
                return None
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
-------------------------------------------------------------------------------------------------------------      
      
      
      
