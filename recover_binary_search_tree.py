'''
You are given the root of a binary 
search tree (BST), where the values of exactly two nodes 
of the tree were swapped by mistake. Recover the tree without changing its structure.
'''


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # get in-order traversal, sort, check the difference
        container = []
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            container.append((node.val, node))
            traverse(node.right)
        traverse(root)
        target = sorted(container)
        for i in range(len(container)):
            currNode, targetNode = container[i][1], target[i][1]
            if currNode != targetNode:
                currNode.val, targetNode.val = targetNode.val, currNode.val
                break

                
--------------------------------------------------------------------------------------------------
def recoverTree(self, root: Optional[TreeNode]) -> None:
        in_order = []
        def inOrder(node):
            if node is None:
                return
            inOrder(node.left)
            in_order.append(node)
            inOrder(node.right)
        
        inOrder(root)

        sorted_order = sorted(in_order, key=lambda x:x.val)
        for i in range(len(in_order)):
            if in_order[i] != sorted_order[i]:
                in_order[i].val, sorted_order[i].val = sorted_order[i].val, in_order[i].val
                return
