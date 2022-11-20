'''
You are given the root of a binary search tree and an array queries of size n consisting of positive integers.

Find a 2D array answer of size n where answer[i] = [mini, maxi]:

mini is the largest value in the tree that is smaller than or equal to queries[i]. If a such value does not exist, add -1 instead.
maxi is the smallest value in the tree that is greater than or equal to queries[i]. If a such value does not exist, add -1 instead.
Return the array answer.
'''


class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        # Input: root = [6,2,13,1,4,9,15,null,null,null,null,null,null,14], queries = [2,5,16]
        # Output: [[2,2],[4,6],[15,-1]]
        values = []
        def dfs(root):
            if not root: return
            
            dfs(root.left)
            values.append(root.val)
            dfs(root.right)
        dfs(root)

        n = len(values)
        res = []
        for q in queries:
            tmp = []
            l, r = 0 , n-1
            while l < r:
                mid = r - (r-l)//2
                if values[mid] > q:
                    r = mid-1
                else:
                    l = mid
            tmp.append(values[l] if values[l] <= q else -1)
            
            l, r = 0 , n-1
            while l < r:
                mid = l + (r-l)//2
                if values[mid] < q:
                    l = mid+1
                else:
                    r = mid
            tmp.append(values[l] if values[l] >= q else -1)
            res.append(tmp)
        return res
