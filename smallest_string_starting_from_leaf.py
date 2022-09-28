'''
You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters 'a' to 'z'.

Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

As a reminder, any shorter prefix of a string is lexicographically smaller.

For example, "ab" is lexicographically smaller than "aba".
A leaf of a node is a node that has no children.
'''

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        paths = []
        
        def dfs(node, string):
            # Translate node value to letter via ASCII
            string += chr(node.val + 97)
            
            if node.left: dfs(node.left, string)
            if node.right: dfs(node.right, string)
            # At leaf node, add reversed tree path to "paths"
            if not node.right and not node.left: paths.append(string[::-1])
                
        dfs(root, '')
        # Sort in lexicographical order and return first path
        paths.sort()
        return paths[0]
