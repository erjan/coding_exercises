'''
Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.
'''

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        columns = defaultdict(list)
        
        q = deque([(root, 0)])
        while q:
            node, x = q.popleft()
            columns[x].append(node.val)
            
            if node.left:
                q.append((node.left, x - 1))
            if node.right:
                q.append((node.right, x + 1))
                
        return [columns[x] for x in range(min(columns), max(columns)+1)]
      
-----------------------------

from collections import defaultdict, deque
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        
        res = defaultdict(list)
        
        queue = deque([(root, 0)])
        
        while queue: 
            node, x = queue.popleft()
            if node: 
                res[x].append(node.val)
                queue.append((node.left, x-1))
                queue.append((node.right, x+1))
        
        return [vals for x, vals in sorted(res.items(), key = lambda x: x[0])]
------------------------------------------------------------

DFS

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
	    # Use a dict to store our answers, keys will be column idxs.
        ans = collections.defaultdict(list)
        
        def helper(node, row, col):
            if not node:
                return
			# Append node vals to column in our dict.
            ans[col].append((row, node.val))
			# Traverse l and r.
            helper(node.left, row + 1, col - 1)
            helper(node.right, row + 1, col + 1)
            
        helper(root, 0, 0)
        # Sort our dict by keys (column vals)
        ans = dict(sorted(ans.items()))
        res = []
		# Loop through our sorted dict appending vals sorted by height (top down order).
        for k, v in ans.items():
            res.append([x[1] for x in sorted(v, key=lambda x:x[0])])
        
        return res
BFS:

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        
        vals = collections.defaultdict(list)
        # Use a deque to stores our nodes, and append starting location.
        q = collections.deque([])
        q.append((root, 0, 0))
        while q:
            node, row, col = q.popleft()
			# If we havea valid node, append vals, and put children in the queue.
            if node:
                vals[col].append((row, node.val))
                q.append((node.left, row + 1, col - 1))
                q.append((node.right, row + 1, col + 1))
        # Sort our dict by keys (column vals)
        vals = dict(sorted(vals.items()))
        res = []
		# Loop through our sorted dict appending vals sorted by height (top down order).
        for k, v in vals.items():
            res.append([x[1] for x in sorted(v, key=lambda x:x[0])])
        
        return res  
      
      --------------------------------------------------------------------
      
      Idea behind this solution : As we move to the left child for a node we can say that we are increasing the width of the tree and as we move to the right child we can say that we are decreasing the width of the tree.

We create a dictionary to hold the width and the node values that correspond to that width.

In the end based on the level and the width we have we sort the dictionaries to get the final output.

This solutions is better than 91% of python solutions. Any suggestions are welcome.

def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        
        # A dictionary that stores width and the nodes at that width with the level at which the nodes are
        dict = defaultdict(list)
        
        
        def preorder(node,width,height):
            """
            Preorder . Assume we add width whenever we go left and we subtract width whenever we go right.
            Example :
                                3
                               /\
                              /  \
                             9    8
                            /\    /\
                           /  \  /  \
                          4    1 0   7
            Width of 3 :  0
            Width of 9 : 1
            Width of 4 : 2
            Width of 1 : 0
            Width of 8 : -1
            Width of 0 : 0
            Width of 7 : -2
            
            Height is being added as we move from one level to another.
            
            Output of Function:
            width : [list of list of (node.val,level) pairs corresponding to the particular width]
            defaultdict(<class 'list'>, {0: [(3, 0), (0, 2), (1, 2)], 1: [(9, 1)], 2: [(4, 2)], -1: [(8, 1)], -2: [(7, 2)]})
            """
            if node:
                dict[width].append((node.val,height))

                if node.left != None:
                    preorder(node.left,width+1,height+1)
                if node.right != None:
                    preorder(node.right,width-1,height+1)

        preorder(root,0,0)
        
        
        # Sort the result to show left to right
        sorted_left_right = sorted(dict.items(),key=lambda p:p[0],reverse=True)
        
        # Sort the result to show top to bottom
        for lst in sorted_left_right:
            lst[1].sort(key=lambda p:p[1])
        
        res = []
        
        # Add the final answer to the result 
        for lst in sorted_left_right:
            
            temp = []
            for values in lst[1]:
                temp.append(values[0])
            res.append(temp)
            
        return res
      
      
--------------------------------------------------------------------------------------
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        def dfs(node, x, y):
            if node is None:
                return
            
            columns[x].append((y, node.val))
            
            dfs(node.left, x - 1, y + 1)
            dfs(node.right, x + 1, y + 1)
            
        if not root:
            return []
            
        columns = defaultdict(list)
        dfs(root, 0, 0)
        
        traversal = []
        for x in range(min(columns), max(columns) + 1):
            traversal.append([val for _, val in sorted(columns[x], key=itemgetter(0))])
        
        return traversal
      
      
      
