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
            
