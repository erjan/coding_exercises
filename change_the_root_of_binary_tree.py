'''
Given the root of a binary tree and a leaf node, reroot the tree so that the leaf is the new root.

You can reroot the tree with the following steps for each node cur on the path starting from the leaf up to the root​​​ excluding the root:

If cur has a left child, then that child becomes cur's right child.
cur's original parent becomes cur's left child. Note that in this process the original parent's pointer to cur becomes null, making it have at most one child.
Return the new root of the rerooted tree.

Note: Ensure that your solution sets the Node.parent pointers correctly after rerooting or you will receive "Wrong Answer".

'''

class Solution:
    def flipBinaryTree(self, root: 'Node', leaf: 'Node') -> 'Node':        
        prev, node = None, leaf
        while node: 
            if node == root:
                if prev == node.right: node.right = None
                else: node.left = None
            else: 
                if prev == node.right: node.right = node.left 
                node.left = node.parent
            node.parent, node, prev = prev, node.parent, node 
        return leaf
      
-------------------

class Solution:
    def flipBinaryTree(self, root: 'Node', leaf: 'Node') -> 'Node':
        def dfs(node, parent):
            if not node: return                          # edge case
            elif node == root:
                node.parent = parent; return             # stop at root
            if node.left:                                # update node.right; no need to recursively update node.right
                node.right = node.left
            if node.parent.left == node:                 # update node.parent pointing to None
                node.parent.left = None
            else:
                node.parent.right = None
            node.left, node.parent = node.parent, parent # update node.left & node.parent
            dfs(node.left, node)                         # recursively update node.left
        dfs(leaf, None)    
        return leaf
