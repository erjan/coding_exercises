'''
Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.
'''


from collections import defaultdict
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        di = defaultdict(list)
        def dfs(node, level, column):
            if node:
                di[level].append(column)
                dfs(node.left, level+1, column*2)
                dfs(node.right, level+1, column*2+1)
        dfs(root, 0 , 0)
        return max([max(di[level]) - min(di[level]) +1 for level in di])
      
-----------------------------------------------------------------------------------------
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #queue for keeping track
        q = [(0, root)]
        ans = 0
        while q:
            n = len(q)
            # nodes list to store indexes of all nodes at a level
            nodes = []
            for _ in range(n):
                idx, node = q.pop(0)
                nodes.append(idx)
                if node.left:
                    q.append((2*idx+1 , node.left))
                if node.right:
                    q.append((2*idx+2 , node.right))
            # max of ans or (right-most index - left-most index + 1) for a level
            ans = max(ans, max(nodes)-min(nodes)+1)
        return ans
