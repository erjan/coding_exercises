'''
You are given the root of a binary tree and a positive integer k.

The level sum in the tree is the sum of the values of the nodes that are on the same level.

Return the kth largest level sum in the tree (not necessarily distinct). If there are fewer than k levels in the tree, return -1.

Note that two nodes are on the same level if they have the same distance from the root.
'''


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        a = []
        
        def dfs(node, h):
            if not node: return
            if h == len(a):
                a.append([])
            a[h].append(node.val)
            dfs(node.left, h+1)
            dfs(node.right, h+1)
        
        dfs(root, 0)
        ans = []
        for i in range(len(a)):
            ans.append(sum(a[i]))
            
        return sorted(ans)[-k] if len(ans) >= k else -1
        
