'''
You are given n BST (binary search tree) root nodes for n separate BSTs stored in an array trees (0-indexed). Each BST in trees has at most 3 nodes, and no two roots have the same value. In one operation, you can:

Select two distinct indices i and j such that the value stored at one of the leaves of trees[i] is equal to the root value of trees[j].
Replace the leaf node in trees[i] with trees[j].
Remove trees[j] from trees.
Return the root of the resulting BST if it is possible to form a valid BST after performing n - 1 operations, or null if it is impossible to create a valid BST.

A BST (binary search tree) is a binary tree where each node satisfies the following property:

Every node in the node's left subtree has a value strictly less than the node's value.
Every node in the node's right subtree has a value strictly greater than the node's value.
A leaf is a node that has no children.
'''

class Solution:
    def canMerge(self, trees: List[TreeNode]) -> TreeNode:
        roots, leaves, loners, n = {}, {}, set(), len(trees)
        if n == 1:
            return trees[0]
        for tree in trees:
            if not tree.left and not tree.right:
                loners.add(tree.val)
                continue
            roots[tree.val] = tree
            for node in [tree.left, tree.right]:
                if node:
                    if node.val in leaves:
                        return None
                    leaves[node.val] = node
                
        for loner in loners:
            if loner not in leaves and loner not in roots:
                return None
            
        orphan = None
        for val, tree in roots.items():
            if val not in leaves:
                if orphan:
                    return None
                orphan = tree
        if not orphan:
            return None
        
        def build(node, small, big):
            nonlocal roots
            if not node:
                return True
            if small >= node.val or node.val >= big:
                return False
            
            if node.val in roots:
                node.left, node.right = roots[node.val].left, roots[node.val].right
                del roots[node.val]
            return build(node.left, small, node.val) and build(node.right, node.val, big)
        del roots[orphan.val]
        result = build(orphan.left, -inf, orphan.val) and build(orphan.right, orphan.val, inf)
        return orphan if result and not roots.keys() else None
---------------------------------------------------------------------------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def canMerge(self, trees: List[TreeNode]) -> TreeNode:
        freq = defaultdict(int)
        for tree in trees: 
            stack = [tree]
            while stack: 
                x = stack.pop()
                if x: 
                    freq[x.val] += 1
                    stack.append(x.left)
                    stack.append(x.right)
        
        cnt, root = 0, None
        mp = {}
        for tree in trees: 
            if freq[tree.val] & 1: cnt, root = cnt+1, tree
            mp[tree.val] = tree
        if cnt != 1: return None 
        
        stack = [(root, None, 0)]
        total = len(trees)
        while stack: 
            node, parent, left = stack.pop()
            if not node.left and not node.right and node.val in mp: 
                total -= 1
                if not parent: 
                    if len(trees) > 1: return None 
                    return root
                if left: parent.left = node = mp[node.val]
                else: parent.right = node = mp[node.val]
            if node.left: stack.append((node.left, node, 1))
            if node.right: stack.append((node.right, node, 0))
        
        if total > 1: return None 
        
        # in-order traversal 
        prev = -inf
        node = root 
        stack = []
        while stack or node: 
            if node: 
                stack.append(node)
                node = node.left 
            else: 
                node = stack.pop()
                if prev >= node.val: return None
                prev = node.val
                node = node.right
        return root
