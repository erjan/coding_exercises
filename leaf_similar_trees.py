'''
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
'''
#my own solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
        
            
            
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
    
        leaflist1 = []
        leaflist2 = []
        
        def getleafs1(root):
            if not root:
                return 
            if root.left is None and root.right is None:
                leaflist1.append(root.val)
            
            getleafs1(root.left)
            getleafs1(root.right)
            
        def getleafs2(root):
            if not root:
                return 
            if root.left is None and root.right is None:
                leaflist2.append(root.val)
            
            getleafs2(root.left)
            getleafs2(root.right)
        
        getleafs1(root1)
        print(leaflist1)
        
        getleafs2(root2)
        print(leaflist2)
        
        return leaflist1 == leaflist2
      
#better solution
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:

        def helper( node: TreeNode, leaf_path):

            if node:

                leaf_path = helper( node.left, leaf_path )

                if not node.left and not node.right:
                    leaf_path += str(node.val) + ' '

                leaf_path += helper( node.right, leaf_path )
                
                return leaf_path
            else:
                return ''
            
        leaf_seq_1 = helper( root1, '')
        leaf_seq_2 = helper( root2, '')

        return leaf_seq_1 == leaf_seq_2
