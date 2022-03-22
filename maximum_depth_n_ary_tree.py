'''
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).
'''


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        queue = []
        
        if root: 
            queue.append((root, 1))
            
        depth = 0
        
        for (node, level) in queue:
            depth = level
            
            for child in node.children:
                queue.append( (child, level+1) )
            
        return depth

#DFS

class Solution(object):
    
    def maxDepth(self, root):
        
        stack = []
        if root: stack.append((root, 1))
            
        depth = 0
        while stack:
            
            (node, d) = stack.pop()
            depth = max(depth, d)
            for child in node.children:
                stack.append((child, d+1))
        return depth
