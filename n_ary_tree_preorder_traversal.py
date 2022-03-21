'''
Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)
'''

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def rec(root):
            if root:
                out.append(root.val)
                for c in root.children:
                    rec(c)
                #out.append(root.val)

        out = []
        rec(root)
        return out
