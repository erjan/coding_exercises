'''
Given an integer array nums where the elements are sorted in ascending order, convert it 
to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of 
every node never differs by more than one.
'''
#WRONG SOLUTION - i created 1 sided array.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        tmp = None
        root = None
        for i in range(len(nums)):
            
            if not tmp:
                root = TreeNode(nums[i])
                tmp = root
            
            else:
                d = TreeNode(nums[i])
                t2 = tmp
                if nums[i] < tmp.val:
                    tmp.right = d
                else:
                    tmp = d                    
                    d.left = t2
                    root = d
        return root
            
        
#right solution

def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

    def helper(left,right):
        if left > right:
            return None

        m = (left+right)//2

        mid_el = TreeNode( nums[m])
        mid_el.left = helper(left, m-1 )
        mid_el.right = helper(m+1, right)
        return mid_el # i was thinking returning this element is not needed - but it is needed, cuz recursive calls to left and right go deeper! and build inner subtrees, so we still need to return

    res = helper(0, len(nums)-1)
    return res 

# TIP i learned - still need to return mid_el!
# i was thinking returning this element is not needed - but it is needed, cuz recursive calls to left and right go deeper! and build inner subtrees, so we still need to return

