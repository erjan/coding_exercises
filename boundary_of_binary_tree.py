'''

The boundary of a binary tree is the concatenation of the root, the left boundary, the leaves ordered from left-to-right, and the reverse order of the right boundary.

The left boundary is the set of nodes defined by the following:

The root node's left child is in the left boundary. If the root does not have a left child, then the left boundary is empty.
If a node in the left boundary and has a left child, then the left child is in the left boundary.
If a node is in the left boundary, has no left child, but has a right child, then the right child is in the left boundary.
The leftmost leaf is not in the left boundary.
The right boundary is similar to the left boundary, except it is the right side of the root's right subtree. Again, the leaf is not part of the right boundary, and the right boundary is empty if the root does not have a right child.

The leaves are nodes that do not have any children. For this problem, the root is not a leaf.

Given the root of a binary tree, return the values of its boundary.
'''


class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        def is_leaf(node: TreeNode):
            if not node:
                return False
            if not node.left and not node.right:
                return True

        def add_left_boundary(node: TreeNode, res: List[int]):
            while node:
                if not is_leaf(node):
                    res.append(node.val)
                if node.left:
                    node = node.left
                else:
                    node = node.right

        def add_leaves(node: TreeNode, res: List[int]):
            if node:
                if is_leaf(node):
                    res.append(node.val)
                else:
                    add_leaves(node.left, res)
                    add_leaves(node.right, res)

        def add_right_boundary(node: TreeNode, res: List[int]):
            stack = []
            while node:
                if not is_leaf(node):
                    stack.append(node.val)
                if node.right:
                    node = node.right
                else:
                    node = node.left
            res += stack[::-1]

        boundary = []

		"""
		Essentially 4 operations
		1. Check root
		2. Add left boundary
		3. Add leaves
		4. Add right bounday (reverse!)
		"""
        if not is_leaf(root):
            boundary.append(root.val)

        add_left_boundary(root.left, boundary)
        add_leaves(root, boundary)
        add_right_boundary(root.right, boundary)

        return boundary
      
-----------------
def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        def is_leaf(node):
            return node and not node.left and not node.right and node != root
        
        def add_leaves(node, li):
            if is_leaf(node):
                li.append(node.val)
                
            if node.left:
                add_leaves(node.left, li)

            if node.right:
                add_leaves(node.right, li)
                    
        def add_left_boundary(t, li):
            if t:
                if not is_leaf(t):
                    li.append(t.val)
                    
                if t.left:
                    add_left_boundary(t.left, li)
                    
                else:
                    add_left_boundary(t.right, li)
                    
        def add_right_boundary(t, li):
            if t:
                if not is_leaf(t):
                    li.append(t.val)
                    
                if t.right:
                    add_right_boundary(t.right, li)
                    
                else:
                    add_right_boundary(t.left, li)
                
        res = []
        right_boundary = []
        
        # 1. Add the root node
        res.append(root.val)
            
        t1 = root.left
        # 2. Generate the left boundary and add to result
        add_left_boundary(t1, res)
        
        # 3. Add the leaf nodes to the result
        add_leaves(root, res)
        
        t2 = root.right
        #4. Generate the right boundary separately (we would reverse it later)
        add_right_boundary(t2, right_boundary)
        
        return res + right_boundary[::-1]
