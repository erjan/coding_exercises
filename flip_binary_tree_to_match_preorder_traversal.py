'''
You are given the root of a binary tree with n nodes, where each node is uniquely assigned a value from 1 to n. You are also given a sequence of n values voyage, which is the desired pre-order traversal of the binary tree.

Any node in the binary tree can be flipped by swapping its left and right subtrees. For example, flipping node 1 will have the following effect:
'''

class Solution(object):
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        stack = [root]
        i = 0 # pointer pointing in voyage
        res = []
        
        while stack:
            root = stack.pop()
            
            if root.val != voyage[i]: # at any point root's val is not equal to current voyage val
                return [-1]
            i += 1
            
            # swap when next val is not correctly positioned
            if root.left and root.left.val != voyage[i]:
                root.left, root.right = root.right, root.left
                res.append(root.val)
            
            # perform the general preorder 
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        
        return res
      
-------------------------------------------------------------------
 def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        flips = []       # list of values for flipped nodes
        i = 0            # index for value in voyage to match next
        
        # Perform a pre-order traversal, swapping nodes if needed
        nodes = [root]
        while nodes:
            node = nodes.pop()
            if node.val != voyage[i]: # Tree can't be made to match voyage
                return [-1]
            i += 1  # node matched so we advance to the next in voyage
            
            # Flip if the left node doesn't match the next value in voyage
            if node.left and node.left.val != voyage[i]:
                node.left, node.right = node.right, node.left
                flips.append(node.val)

            # Continue the pre-order traversal
            if node.right:
                nodes.append(node.right)
            if node.left:
                nodes.append(node.left)

        return flips 
