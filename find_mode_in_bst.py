'''
Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
'''


#my very clunky solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
            
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        def trav(root):
            if root:
                return trav(root.left) + [root.val]+ trav(root.right)
            else:
                return []
                    
        ar = trav(root)
        d = dict()
        for i in range(len(ar)):
            if ar[i] not in d:
                d[ar[i]] = 1
            else:
                d[ar[i]] +=1


        most_freq = max(d.values())

        res = list()
        for k,v in d.items():
            if v == most_freq:
                res.append(k)
        return res 
