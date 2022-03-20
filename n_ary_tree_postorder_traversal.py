'''
Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        output = list()
        stack = list()

        if root is None:
            return output

        stack.append(root)
        while stack:
            cur = stack.pop()
            output.append(cur.val)
            for c in cur.children:
                stack.append(c)
        print(output)
        output = output[::-1]
        return output

#recursive

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def rec(root):
            if root:
                for c in root.children:
                    rec(c)
                out.append(root.val)

        out = []
        rec(root)
        return out
    
    
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        postorder_traversal = []
        stack = [[root, False]]
        
        while stack:
            curr, visited = stack.pop()
            if visited:
                postorder_traversal.append(curr.val)
            else:
                stack.append([curr, True])
                children = len(curr.children)
                for i in range(children - 1, -1, -1):
                    stack.append([curr.children[i], False])
        return postorder_traversal    
