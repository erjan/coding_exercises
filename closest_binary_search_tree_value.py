'''
Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        
        def helper(root):
            if root:
                return helper(root.left) + [root.val]+ helper(root.right)
            else:
                return []
        
        res = helper(root)
        
        q = list()
        for i in range(len(res)):
            q.append([(abs(res[i] - target)), res[i]])

        q.sort(key=lambda x: x[0])
        q = q[0]
        return q[1]

      
#much better - solution from discussions

def closestValue(self, root, target):
    a = root.val
    kid = root.left if target < a else root.right
    if not kid: return a
    b = self.closestValue(kid, target)
    return min((b, a), key=lambda x: abs(target - x))
  
  
#iterative

def closestValue(self, root, target):
    closest = root.val
    while root:
        closest = min((root.val, closest), key=lambda x: abs(target - x))
        root = root.left if target < root.val else root.right
    return closest

