'''
Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

Note that you need to maximize the answer before taking the mod and not after taking it.
'''


'''

Firstly we will find sum of both subtree for each node.
👉 Then we will store the sum of both (left & right) subtree with the node value.
👉 Now find the maximum which will be the sum of all nodes (mainly the value of sum at root node).
👉 Here we will use the stored value "res" , for each sum in res we can get the product of two subtree .
👉 At last return the maximum product after removing one edge.
'''


class Solution:
  def maxProduct(self, root: Optional[TreeNode]) -> int:
    
    def dfs(root):
        if root is None:
            return 0
        ans = dfs(root.left)+dfs(root.right)+root.val
        res.append(ans)
        return ans
    
    res=[]
    dfs(root)
    
    total,m = max(res),float('-inf')
    for s in res:
        m=max(m,s*(total-s))
        
    return m%(10**9+7)
  
----------------------------------------------------------------------------------------------------------
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        
        sums = []
        def dfs(node):
            if node is None:
                return 0
            subtree_sum = dfs(node.left) + dfs(node.right) + node.val
            sums.append(subtree_sum)
            return subtree_sum
        
        
        m = -inf
        total = dfs(root)
        for i in sums:
            prod = i * (total-i)
            if prod > m: m = prod
        
        return m % (10**9 + 7)
