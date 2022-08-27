'''
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
'''

class Codec:

    def serialize(self,root):
        def do(node):
            if node:
                vals.append(str(node.val))
                do(node.left)
                do(node.right)
            else:
                vals.append('#')
        vals = []
        do(root)
        return ' '.join(vals)

    def deserialize(self,s):
        def do():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = do()
            node.right = do()
            return node
        vals = iter(s.split())
        return do()
        
