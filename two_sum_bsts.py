'''
Given the roots of two binary search trees, root1 and root2, return 
true if and only if there is a node in the first tree and a node in the second 
tree whose values sum up to a given integer target.
'''



class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        def dfs(node):
            return dfs(node.left) | dfs(node.right) | {node.val} if node else set()
        q1 = dfs(root1)
        return any(target - a in q1 for a in dfs(root2))
Extra
from functools import lru_cache
class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        @lru_cache()
        def dfs(n1, n2):
            if not n1 or not n2:
                return False
            if n1.val + n2.val < target:
                return dfs(n1.right, n2) or dfs(n1, n2.right)
            elif n1.val + n2.val > target:
                return dfs(n1.left, n2) or dfs(n1, n2.left)
            else:
                return True
        return dfs(root1, root2)
-----------------------------------------------------------

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def twoSumBSTs(self, root1, root2, target):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :type target: int
        :rtype: bool
        """
        hashtree1 = set()

        stack = [root1]
        while stack:
            node = stack.pop()
            hashtree1.add(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            
        stack = [root2]
        while stack:
            node = stack.pop()
            if (target - node.val) in hashtree1:
                return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)     
                
        return False
-------------------------------------------------------------

class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        arr1 = []
        arr2 = []

        def inOrderTrav(r: TreeNode, arr: List) -> List:
            if r:
                arr = inOrderTrav(r.left, arr)
                arr.append(r.val)
                arr = inOrderTrav(r.right, arr)
            return arr
        arr1 = inOrderTrav(root1, arr1)
        arr2 = inOrderTrav(root2, arr2)
        complements2 = {}
        for i in range(len(arr2)):
            complements2[arr2[i]] = i

        for i in range(len(arr1)):
            if target - arr1[i] in complements2:
                return True

        return False
---------------------------------------------------------

class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        def bst(root):
            ans = [] 
            def inorder(root):
                if not root:
                    return []
                inorder(root.left)
                ans.append(root.val)
                inorder(root.right)
                return ans
            return inorder(root)
        a1 = bst(root1)
        a2 = bst(root2)
        i, j = 0, len(a2)-1
        while i < len(a1) and j >= 0:
            if a1[i] + a2[j] > target:
                j -= 1
            elif a1[i] + a2[j] < target:
                i += 1
            else:
                return True
        return False
-----------------------------------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        output1 = []
        self.inorder(root1, output1)
        for i in output1:
            cur = root2
            while cur:
                #print(i,cur.val)
                if i+cur.val == target:
                    return True
                else:
                    if i+cur.val < target:
                        cur = cur.right
                    else:
                        cur = cur.left
        return False
           
    def inorder(self,root, output):
        if root == None:
            return 
        else:
            self.inorder(root.left, output)
            output.append(root.val)
            self.inorder(root.right, output)
      
      
      
      
