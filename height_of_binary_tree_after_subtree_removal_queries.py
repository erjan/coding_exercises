'''
You are given the root of a binary tree with n nodes. Each node is assigned a unique value from 1 to n. You are also given an array queries of size m.

You have to perform m independent queries on the tree where in the ith query you do the following:

Remove the subtree rooted at the node with the value queries[i] from the tree. It is guaranteed that queries[i] will not be equal to the value of the root.
Return an array answer of size m where answer[i] is the height of the tree after performing the ith query.

Note:

The queries are independent, so the tree returns to its initial state after each query.
The height of a tree is the number of edges in the longest simple path from the root to some node in the tree.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        lvl_lookup = {}
        lvl_heights = {}

        def dfs(node, level):
            lvl_lookup[node.val] = level
            left, right = 0, 0
            if node.left: left = dfs(node.left, level + 1)
            if node.right: right = dfs(node.right, level + 1)
            height = max(level, left, right)

            if level not in lvl_heights: lvl_heights[level] = []
            lvl_heights[level].append([height, node.val])
            lvl_heights[level].sort(reverse=True)
            # For each level, maintain, at most, the two largest heights
            while len(lvl_heights[level]) > 2: lvl_heights[level].pop()

            return height
        dfs(root, 0)

        output = []
        for query in queries:
            level = lvl_lookup[query]
            result = None
            for height, node in lvl_heights[level]:
                if node != query:
                    result = height
                    break
            if result == None: output.append(level - 1)
            else: output.append(result)

        return output
      
-------------------------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        
		#each node stores (value, max_height to left + own height, max_height to right + own height)
        def get_height(root, current):
            if not root: return [0, 0]
            else:
                left = get_height(root.left, current + 1)
                right = get_height(root.right, current + 1)
                root.val = [root.val, current + max(left), current + max(right)]
                return [max(left) + 1, max(right) + 1]
           
		#traverse the tree and store the solution for all subtrees
		#carry stores the maximum height so far
        def gen_sol(root, carry, dicts):
            if root.left:
                dicts[root.left.val[0]] = max(carry, root.val[2])
                gen_sol(root.left, max(carry, root.val[2]), dicts)
            if root.right:
                dicts[root.right.val[0]] = max(carry, root.val[1])
                gen_sol(root.right, max(carry, root.val[1]), dicts)
                
        dicts = {}
        get_height(root, 0)
        gen_sol(root, -1, dicts)
        
        res = []
        
		#get solutions from the dictionary
        for element in queries:
            res.append(dicts[element])
        
        return res
        
