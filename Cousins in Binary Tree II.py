'''
Given the root of a binary tree, replace the value of each node in the tree with the sum of all its cousins' values.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Return the root of the modified tree.

Note that the depth of a node is the number of edges in the path from the root node to it.
'''



def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    m = Counter()
    def dfs(r, l):
        if not r: return
        m[l] += r.val
        dfs(r.left, l + 1)
        dfs(r.right, l + 1)
    dfs(root, 0)
    
    def dfs1(r, l, curr):
        sum_of_cousins = m[l + 1] - (r.left.val if r.left else 0) - (r.right.val if r.right else 0)
        if r.left:
            curr.left = TreeNode(sum_of_cousins)
            dfs1(r.left, l + 1, curr.left)
        if r.right:
            curr.right = TreeNode(sum_of_cousins)
            dfs1(r.right, l + 1, curr.right)
        return curr
    return dfs1(root, 0, TreeNode(0))
