'''
Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def constr(self, left, right, nums):
        if left > right:
            return None
        else:
            mid = left + (right-left)//2
            root = TreeNode(nums[mid])
            root.left = self.constr(left, mid-1, nums)
            root.right = self.constr(mid+1, right, nums)
            return root

    def INR(self, root, nums):
        if root:
            self.INR(root.left, nums)
            nums.append(root.val)
            self.INR(root.right, nums)

    def balanceBST(self, root: TreeNode) -> TreeNode:

        nums = []
        self.INR(root, nums)

        nums.sort()
        a = nums

        x = self.constr(0, len(a)-1, nums)
        return x
