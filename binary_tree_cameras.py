'''
You are given the root of a binary tree. We install cameras on the tree nodes where each camera at a node can monitor its parent, itself, and its immediate children.

Return the minimum number of cameras needed to monitor all nodes of the tree.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        # During depth first search travel of the tree 
        # we can be covered - 'c' -> if we have no node, we are covered. Alternately, if we are observed by left or right, return covered 
            # Node does not exist --> means we do not need to cover it 
            # Node is being observed by one of children --> means we do not need to cover it 
                                   # A 'c'
                            # B 'u'        C 'o'
            # C or B could observe A. C cannot observe B, but A could observe both 
        # we can be unobserved - 'u' -> if children are unobserved, observe here after incrementing result and report observing (parent watches kids)
            # leaf nodes will always be unobserved 
            # leaf nodes have no left or right nodes. As such, the deepening on them has both of the non-existent edges as covered 
            # this means that we have now an unobserved leaf which will return 'u' 
        # we can be observing - 'o' -> if left or right is observing, return covered (kids watch parent)
            # if we have a leaf node child, in either branch, we will have an unobserved child. We must watch them. 
            # this means we have will have at this node a value of observed regardless of the result off of the other branch 
            # if we are have children that are observing, we are being observed, and so we may report covered 
        # return valuation will be based on if root is unobserved + the result (if root is unobserved we need to observe at root)
        self.result = 0 

        def depth_first_search(node) : 
            # base case 
            if node is None : 
                return "c" # covered 
            # recursive deepening 
            left_search, right_search = depth_first_search(node.left), depth_first_search(node.right)
            # check for equality as covered 
            if left_search == right_search == "c" : 
                # if left is covered and right is covered, neither is observing 
                # if neither is observing, then this is unobserved 
                return "u"
            # if left search is unobserved or right search is unobserved 
            if left_search == "u" or right_search == "u" : 
                # we need to observe these unruly children 
                self.result += 1 
                # now that we've done that, we need to observing 
                return "o"
            # if left search or right search are observing 
            if left_search == "o" or right_search == "o" : 
                # we are being watched by our children like an unruly parent 
                return "c"

        # get your final return valuation 
        return_valuation = depth_first_search(root) 
        # if you are unobserved at the root 
        if return_valuation == "u": 
            # increment your result 
            self.result += 1 
        
        return self.result               


        
