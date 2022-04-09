'''

Given the root of a binary tree, turn the tree upside down and return the new root.

You can turn a binary tree upside down with the following steps:

The original left child becomes the new root.
The original root becomes the new right child.
The original right child becomes the new left child.

The mentioned steps are done level by level. It is guaranteed that every right node has a sibling (a left node with the same parent) and has no children.
'''

def upsideDownBinaryTree(self, root):
    if not root or not root.left:
        return root
    lRoot = self.upsideDownBinaryTree(root.left)
    rMost = lRoot
    while rMost.right:
        rMost = rMost.right
    root, rMost.left, rMost.right = lRoot, root.right, TreeNode(root.val)
    return root
  
  --------------------------
  
  def upsideDownBinaryTree(self, root):
        stack = []
        while root:
            stack.append(root)
            root = root.left
        dummy = TreeNode(None)
        curr = dummy
        while stack:
            node = stack.pop()
            curr.right = node
            curr.left = node.right
            curr = curr.right
        curr.left = curr.right = None
        return dummy.right
