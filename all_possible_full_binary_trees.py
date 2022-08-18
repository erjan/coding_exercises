'''
Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer must have Node.val == 0.

Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.

A full binary tree is a binary tree where each node has exactly 0 or 2 children.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        
        dp = {0: [], 1:[TreeNode()] }

        def helper(n):       
            if n in dp:
                return dp[n]
                    
            res = []

            for left in range(n):
                right = n - 1 - left
                leftTrees = helper(left)
                rightTrees = helper(right)

                for t1 in leftTrees:
                    for t2 in rightTrees:
                        res.append(TreeNode(0,t1,t2))
            dp[n] = res
            return res

        return helper(n)
        
-----------------------------------------------------        


class Solution:
    def __init__(self):
        
        self.full_bst = dict()
        
        # base case of full binary tree with one node
        self.full_bst[ 1 ] = [ TreeNode(0) ]
    
    
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
    
        if N % 2 == 0:
            # if N is even number, there is no chance to build full binary tree
            return []
        
        if N in self.full_bst:
            # if Full BST with N is constructed before, then reutrn by look-up dictionary
            return self.full_bst[N]
        
        else:
            # Construct Full BST with N Nodes by top-down recursion with memorization

            # a list to store different BST with N Nodes
            tree = []
            
            # total n nodes:
            # 1 for root node
            # left_subtree_nodes for left-sub-full-bst
            # n-1-left_subtree_nodes for right-sub-full-bst
            for left_subtree_nodes in range(1, N, +2):
                
                # Divide-and-conquer
                left_sub_trees = self.allPossibleFBT( left_subtree_nodes )
                right_sub_trees = self.allPossibleFBT( (N-1) - left_subtree_nodes )
                
                # Construct Full BST with all possible combination of left-sub-full-bst and right-sub-full-bst 
                for left_subt in left_sub_trees:
                    for right_subt in right_sub_trees:
                        
                        root = TreeNode(0)
                        root.left = left_subt
                        root.right = right_subt
                        
                        tree.append( root )
            
            self.full_bst[ N ] = tree
            return tree
            
            
