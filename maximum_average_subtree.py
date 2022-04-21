'''
Given the root of a binary tree, return the maximum average value of a subtree of that tree. Answers within 10-5 of the actual answer will be accepted.

A subtree of a tree is any node of that tree plus all its descendants.

The average value of a tree is the sum of its values, divided by the number of nodes.
'''

class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        
        max_avg = 0
        
        def helper(node):
            nonlocal max_avg
            if not node:
                return 0, 0
            leftt, leftc = helper(node.left)
            rightt, rightc = helper(node.right)
            avg = (leftt+rightt+node.val)/(leftc+rightc+1)
            max_avg = max(max_avg, avg)
            return (leftt+rightt+node.val), (leftc+rightc+1)
        
        helper(root)
        
        return max_avg
-----------------------------------------

Algo
Traverse the tree in bottom-up post-order.

Implementation

class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        
        def fn(node): 
            """Return sum, count and max average of subtree rooted at node."""
            if not node: return 0, 0, 0
            ls, ln, lv = fn(node.left)
            rs, rn, rv = fn(node.right)
            s = ls + node.val + rs
            n = ln + 1 + rn 
            return s, n, max(s/n, lv, rv)
            
        return fn(root)[2]
Analysis
Time complexity O(N)
Space complexity O(N)

Alternative implementation

class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        
        def fn(node): 
            """Return sum, count and max average of subtree rooted at node."""
            nonlocal ans 
            if not node: return 0, 0
            ls, ln = fn(node.left)
            rs, rn = fn(node.right)
            s = ls + node.val + rs
            n = ln + 1 + rn 
            ans = max(ans, s/n)
            return s, n
        
        ans = 0
        fn(root)
        return ans 
Edited on 9/1/2021
Adding an iterative implementation

class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        ans = 0 
        sm, cnt = {None: 0}, {None: 0}
        node, stack = root, []
        prev = None
        while node or stack: 
            if node: 
                stack.append(node)
                node = node.left
            else: 
                node = stack[-1]
                if node.right and node.right != prev: node = node.right
                else: 
                    sm[node] = node.val + sm[node.left] + sm[node.right]
                    cnt[node] = 1 + cnt[node.left] + cnt[node.right]
                    ans = max(ans, sm[node]/cnt[node])
                    stack.pop()
                    prev = node 
                    node = None
        return ans 
----------------------------------------------------------------------------

# T(N) = O(N)
# S(N) = O(N) rec depth
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_avg_so_far = -1
        
    def postOrderTraversal(self,root): # 55
        # base case: leaf
        if root.left == None and root.right == None:
            # computing avg
            self.max_avg_so_far = max(self.max_avg_so_far,root.val)
            return root.val, 1 # value of the node, size # 5,1
        
        # conditional
        left_subtree_sum = 0
        left_subtree_size = 0
        right_subtree_sum = 0
        right_subtree_size = 0
        
        if root.left:
            left_subtree_sum,left_subtree_size = self.postOrderTraversal(root.left) 
            # 9,1
        if root.right:
            right_subtree_sum,right_subtree_size = self.postOrderTraversal(root.right) 
            # 7,1
        
        total_sum = (left_subtree_sum + right_subtree_sum + root.val) # 9+7+55

        total_size = (left_subtree_size + right_subtree_size + 1) # 1 + 1 + 1
        total_avg = total_sum /total_size
        
        
        self.max_avg_so_far = max(self.max_avg_so_far,total_avg)
        
        return total_sum,total_size # (6+7+3),3
        
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        
        self.postOrderTraversal(root)
        
        return self.max_avg_so_far
        
---------------------------------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.res = 0
        self.recursion(root)
        return self.res
        
    def recursion(self,root):
        if root == None:
            return [0,0.0]
        
        nLeft, sumLeft = self.recursion(root.left)
        
        nRight,sumRight = self.recursion(root.right)
        
        curN = nLeft + nRight + 1
        curSum = sumLeft + sumRight + root.val
        curAverage = curSum/curN
        
        self.res = max(self.res, curAverage)
        
        return [curN, curSum]
-----------------------------------------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from math import inf

class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        
        # Init
        max_avg = -inf
        
        # DFS approach
        def dfs(curr: TreeNode):
            
            nonlocal max_avg
             
            if curr:
                
                # Get no. of nodes from left tree and total value of left tree
                n, tn = dfs(curr.left)
                
                # Get no. of nodes from right tree and total value of right tree
                m, tm = dfs(curr.right)
                
                # Calc average on current node
                max_avg = max(max_avg, (tn+tm+curr.val)/(m+n+1))
                
                # return total no. of nodes and total value from the current node
                return n+m+1, tn+tm+curr.val
            
            return 0,0 # default values
        
        # run dfs on root
        dfs(root)
        
        return max_avg
------------------------------------------------

class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        maxAvg = 0
        
        def dfsAvg(node):
            nonlocal maxAvg
            left, right  = (0, 0), (0, 0)  # (subTreeValue, numberOfSubTreeNodes)
            
            if node.left is None and node.right is None:
                maxAvg = max(node.val, maxAvg)
                return (node.val, 1)
            
            if node.left:
                left = dfsAvg(node.left)
            
            if node.right:
                right = dfsAvg(node.right)
                
            totalNumOfNodes = left[1] + right[1] + 1
            totalValue = left[0] + right[0] + node.val
            maxAvg = max(totalValue/totalNumOfNodes, maxAvg)
            
            return (totalValue, totalNumOfNodes)
        
        dfsAvg(root)
        
        return maxAvg
      
      
        
      
      
