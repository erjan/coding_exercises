'''
Given the root of a binary search tree (BST) and an integer target, split the tree into two subtrees where one subtree has nodes that are all smaller or equal to the target value, while the other subtree has all nodes that are greater than the target value. It Is not necessarily the case that the tree contains a node with the value target.

Additionally, most of the structure of the original tree should remain. Formally, for any child c with parent p in the original tree, if they are both in the same subtree after the split, then node c should still have the parent p.

Return an array of the two roots of the two subtrees.
'''


class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        
        def fn(node):
            """Return splitted BST."""
            if not node: return None, None
            if node.val <= target: 
                left, right = fn(node.right)
                node.right = left
                return node, right
            else: 
                left, right = fn(node.left)
                node.left = right
                return left, node
                
        return fn(root)
-----------------------------------------

class Solution:
    def splitBST(self, root: TreeNode, target: int) -> List[TreeNode]:
        if not root:
            return [None, None]

        if target < root.val:
            se, root.left = self.splitBST(root.left, target)
            return [se, root]
        if target > root.val:
            root.right, gt = self.splitBST(root.right, target)
            return [root, gt]

        # if target == root.val
        se, gt, root.right = root, root.right, None
        return [se, gt]
----------------------------------------

class Solution:
    def splitBST(self, root: TreeNode, V: int) -> List[TreeNode]:
        if not root:
            return [None, None]
        if root.val <= V:
            l, r = self.splitBST(root.right, V)
            root.right = l
            return [root, r]
        else:
            l, r = self.splitBST(root.left, V)
            root.left = r
            return [l, root]
          
      
      
