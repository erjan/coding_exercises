'''
Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.

Return the number of pseudo-palindromic paths going from the root node to leaf nodes.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        # traverse the tree, the set pairs maintains the number of each element
        # If you already have the same element in pairs, then remove it
        # Else, add it to pairs

        # In the leaf, if the set is empty, then its an even palindrome.
        # In the leaf, if the set has 1 element , its an odd palindrome.
        # In th leaf, if the set has > 1 elements, its not a palindrome.
        
        def traverse(node, pairs):
            if not node:
                return 0
            
            if node.val in pairs:
                pairs.remove(node.val)
            else:
                pairs.add(node.val)
            
            if not node.left and not node.right:
                return 1 if len(pairs) <= 1 else 0
            
            # correct!!
            left = traverse(node.left, set(pairs))
            right = traverse(node.right, set(pairs))
            
            # wrong, becasue pairs will change after we traversed node.left or node.right!
            # left = traverse(node.left, pairs)
            # right = traverse(node.right, pairs)
            
            return left + right
        
        return traverse(root, set())
      
----------------------------------------------------------------------------------------------
from collections import Counter as cc 
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        l=[]
        def dfs(node,s):
            if(node):
                s+=str(node.val)
                if(not node.left and not node.right):
                    l.append(s)
                dfs(node.left,s)
                dfs(node.right,s)
        
        dfs(root,"")
        c=0
        for i in l:
            if(sum(v%2 for v in cc(i).values())<2):
                c+=1
        return c
