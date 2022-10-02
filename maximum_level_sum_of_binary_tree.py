'''
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.
'''

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        ans=[]
        def helper(root,level):
            if root:
                if level>=len(ans):
                    ans.append([root.val])
                else:
                    ans[level].append(root.val)
                helper(root.left,level+1)
                helper(root.right,level+1)
        helper(root,0)
        ans=list(map(lambda x:sum(x),ans))
        return 1+ans.index(max(ans))
      
--------------------------------------------------------------------------------
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
                        
        q = deque([(root,1)])
        
        max_sum = -float('inf')
        
        while q:
            
            level_sum = 0
            
            for _ in range(len(q)):
                cur, level = q.popleft()
                
                level_sum += cur.val
                
                if cur.left:
                    q.append((cur.left,level+1))
                if cur.right:
                    q.append((cur.right,level+1))
            
            if level_sum > max_sum:
                    max_sum, min_level = level_sum, level
                
        return min_level
