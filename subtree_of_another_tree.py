'''
Given the roots of two binary trees root and subRoot, return true if there is 
a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and 
all of this node's descendants. The tree tree could also be considered as a subtree of itself.
'''


class Solution:
    
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        
        if not s:
            return False
        
        if self.isSameTree(s,t):
            return True
        
        return self.isSubtree(s.left, t) or self.isSubtree(s.right,t)
    
    def isSameTree(self, p, q):
        if not p and not q:             # base case when we reached the bottom of both trees and both nodes are nil    
            return True
    
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
