'''
You are given an integer array nums with no duplicates. A maximum binary tree can be built recursively from nums using the following algorithm:

Create a root node whose value is the maximum value in nums.
Recursively build the left subtree on the subarray prefix to the left of the maximum value.
Recursively build the right subtree on the subarray suffix to the right of the maximum value.
Return the maximum binary tree built from nums.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(nums, root):            
            if nums:
            
                cur_max = max(nums)
                cur_max_index = nums.index(cur_max)

                root = TreeNode(cur_max)

                left_subarray = nums[:cur_max_index]
                right_subarray = nums[cur_max_index+1:]

                root.left = helper(left_subarray, root)
                root.right = helper(right_subarray,root)            
                return root            
            else:
                return None
              
        root = helper(nums, None)
        return root
      
#-----------------------------------------------------------------      
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        stack = []  #build a decreasing stack
        for i in nums:
            node = TreeNode(i)
            lastpop = None
            
            while stack and stack[-1].val < i:  #popping process
                lastpop = stack.pop()
            node.left = lastpop
            
            if stack:
                stack[-1].right = node
            stack.append(node)
            
        return stack[0]     
#----------------------------------------------------------------

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        
        def dfs(nums):
            if not nums:
                return None
            
            max_ = max(nums)
            idx = nums.index(max_)
            root = TreeNode(max_)
            
            root.left = dfs(nums[:idx])
            root.right =  dfs(nums[idx+1:])
            return root
                    
        return dfs(nums)
