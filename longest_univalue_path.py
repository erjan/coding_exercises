'''
Given the root of a binary tree, return the length of the longest path, where each node in the path has the same value. This path may or may not pass through the root.

The length of the path between two nodes is represented by the number of edges between them.
'''


class Solution:
    
    def longestUnivaluePath(self, root: TreeNode) -> int:
        
        
        # keep track of longest univalue path
        longest_uni_path = 0
        
        def helper( node):
            if not node:
                return 0

            else:

                path_of_left = helper( node.left )
                path_of_right = helper( node.right )
                
                # if left node has the same value, extend uni path
                left_uni = path_of_left+1 if node.left and node.left.val == node.val else 0
                
                # if right node has the same value, extend uni path
                right_uni = path_of_right+1 if node.right and node.right.val == node.val else 0
        
                nonlocal longest_uni_path
                # use node as bridge to make uni_path as long as possible
                longest_uni_path = max( longest_uni_path, left_uni + right_uni )

                return max(left_uni, right_uni)        
        
		#------------------------------------------------
        
        helper( root )
        
        return longest_uni_path
