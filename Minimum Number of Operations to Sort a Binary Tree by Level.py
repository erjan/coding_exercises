'''
You are given the root of a binary tree with unique values.

In one operation, you can choose any two nodes at the same level and swap their values.

Return the minimum number of operations needed to make the values at each level sorted in a strictly increasing order.

The level of a node is the number of edges along the path between it and the root node.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def minSwap(self,arr):
        n = len(arr)
        res = 0
        oldarr = arr[:]
        h = {}
        oldarr.sort()

        for i in range(n):
            h[arr[i]] = i


        init = 0
        for i in range(n):
            if arr[i] != oldarr[i]:
            
                res += 1
                init = arr[i]
                arr[i], arr[h[oldarr[i]]] = arr[h[oldarr[i]]], arr[i]
                h[init] = h[oldarr[i]]
                h[oldarr[i]] = i

        return res

    def minimumOperations(self, root: Optional[TreeNode]) -> int:


        res = []
        
        q = deque( [root] if root else [])
        
        while len(q):
            
            qlen = len(q)
            row = []
            
            for _ in range(qlen):
                cur = q.popleft()
                row.append(cur.val)
                
                if cur.left: 
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            
            res.append(row)
            
        res = res[1:]
        total = 0
        for l in res:
            total += self.minSwap(l)
 
        return total
