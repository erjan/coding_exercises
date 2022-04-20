'''
Given the root of a binary tree, return the length of the longest consecutive path in the tree.

A consecutive path is a path where the values of the consecutive nodes in the path differ by one. This path can be either increasing or decreasing.

For example, [1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is not valid.
On the other hand, the path can be in the child-Parent-child order, where not necessarily be parent-child order.
'''

def longestConsecutive(self, root):
    return max(self.get_max(root))

def get_max(self, root):
    """Return max increasing and max decreasing ending at root, and max overall."""
    if not root:
        return 0, 0, 0
        
    inc, dec = 1, 1

    li, ld, lt = self.get_max(root.left)
    ri, rd, rt = self.get_max(root.right)

    if root.left:
        if li and root.left.val - root.val == 1:
            inc = li + 1

        if ld and root.left.val - root.val == -1:
            dec = ld + 1

    if root.right:
        if ri and root.right.val - root.val == 1:
            inc = max(inc, ri + 1)

        if rd and root.right.val - root.val == -1:
            dec = max(dec, rd + 1)

    return inc, dec, max(inc + dec - 1, lt, rt)
  
----------------------------------------------------------------

inc: the longest increasing consecutive sequence started at root.
dec: the longest decreasing consecutive sequence started at root.
out: the longest consecutive sequence in the tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        
        
        inc, dec, out = self.helper(root)
        
        return out
    
    def helper(self, root):
        if root:
            
            l_inc, l_dec, l_out = self.helper(root.left)
            r_inc, r_dec, r_out = self.helper(root.right)
            
            inc = 1; dec = 1; out = 1
            
            if l_inc and root.left.val + 1 == root.val:
                inc = max(inc, l_inc + 1)
            if r_inc and root.right.val + 1 == root.val:
                inc = max(inc, r_inc + 1)
            
            if l_dec and root.left.val - 1 == root.val:
                dec = max(dec, l_dec + 1)
            if r_dec and root.right.val - 1 == root.val:
                dec = max(dec, r_dec + 1)
            
            
            out = max(l_out, r_out, inc, dec)
            if inc == l_inc + 1 and dec == r_dec + 1:
                out = max(out, l_inc + 1 + r_dec)
            if dec == l_dec + 1 and inc == r_inc + 1:
                out = max(out, l_dec + 1 + r_inc)
            
            
            return inc, dec, out 
        
        return 0, 0 , 0 
-------------------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        
        ##longest seq
        ##every node can have asc and desc on 2 branches
        ##answer = (asc-chain) + (desc-chain)
        
        ans = 0
        @lru_cache(None)
        def asc(root,prev_val):##finding the maximum length ascending sequence for the current node
            if root is None:
                return 0
            elif root.val != prev_val+1:
                return 0
 
            
            elif root.val == prev_val + 1:
                return 1 + max(asc(root.left,root.val), asc(root.right,root.val))
            
        @lru_cache(None)    
        def desc(root,prev_val):##finding the maximum length descdending sequence for the current node
            
            if root is None:
                return 0
            
            elif root.val!=prev_val-1:
                return 0
            
                        
            elif root.val == prev_val -1:
                return 1 + max(desc(root.left,root.val),desc(root.right,root.val))
            
        q = [root]
        
        while q:
            
            for x in range(len(q)):
                node = q.pop(0)
                ##-1 as root node will be counted twice
                ans = max(ans, asc(node,node.val-1) + desc(node,node.val+1) - 1)
                
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
                    
        return ans
      
--------------------------------------------------
  def longestConsecutive(self, root: TreeNode) -> int:
        def longest_path(root):
            if not root:
                return 0, 0
            inc, dec = 1, 1
            l_inc, l_dec = longest_path(root.left)
            r_inc, r_dec = longest_path(root.right)
            if root.left:
                if root.left.val == root.val + 1:
                    inc = max(inc, 1 + l_inc)
                if root.left.val == root.val - 1:
                    dec = max(dec, 1 + l_dec)
            if root.right:
                if root.right.val == root.val + 1:
                    inc = max(inc, 1 + r_inc)
                if root.right.val == root.val - 1:
                    dec = max(dec, 1 + r_dec)
            res[0] = max(res[0], inc + dec - 1)
            return (inc, dec)
        
        res = [0]
        longest_path(root)
        return res[0]
      
----------------------------------------------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    longest = 0
    
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root)
        return self.longest 
        
    def dfs(self, node):
        if node is None: 
            return (0, 0)
        left, right = node.left, node.right
        l_inc, l_dec = self.dfs(left)
        r_inc, r_dec = self.dfs(right)
        n_inc = n_dec = 1
        if left and left.val + 1 == node.val:
            n_inc = l_inc + 1
        if right and right.val + 1 == node.val:
            n_inc = max(n_inc, r_inc + 1)
        if left and left.val - 1 == node.val:
            n_dec = l_dec + 1
        if right and right.val - 1 == node.val:
            n_dec = max(n_dec, r_dec + 1)        
        self.longest = max(self.longest, n_inc + n_dec - 1)
        return(n_inc, n_dec)
      
      
