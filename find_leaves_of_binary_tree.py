'''
Given the root of a binary tree, collect a tree's nodes as if you were doing this:

Collect all the leaf nodes.
Remove all the leaf nodes.
Repeat until the tree is empty.
'''

class Solution(object):
    def findLeaves(self, root):
        def order(root, dic):
            if not root:
                return 0
            left = order(root.left, dic)
            right = order(root.right, dic)
            lev = max(left, right) + 1
            dic[lev] += root.val,
            return lev
        dic, ret = collections.defaultdict(list), []
        order(root, dic)
        for i in range(1, len(dic) + 1):
            ret.append(dic[i])
        return ret
-----------------------------------------

Thought process
post-order traversal, since we would like to add leaf nodes in subtrees first
after processing for both subtrees, we know that the current node is a leaf now
we add it to the result list
we use a level variable to denote which sublist (index) it should be in the res list
level is 0 for original leaf nodes
level will be 1 + the maximum level of the children of the current node
when there is not enough sublists in res list, we simply add enough empty lists to it
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        res = []
        def dfs(root):
            level = 0
            if root.left:
                level = max(level, 1 + dfs(root.left))
            if root.right:
                level = max(level, 1 + dfs(root.right))
            for _ in range(level-len(res)+1):
                res.append([])
            res[level].append(root.val)
            return level
        dfs(root)
        return res
---------------------------------------------------

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        
        res = []
        
        def helper(node):
		    # When we read the leaf return -1 (to help start our levels at 0 - because we add 1 when returned).
            if not node:
                return -1
			# find the height of the l and r subtrees.
            left = helper(node.left)
            right = helper(node.right)
			# We have to take the max height given that we're pruning, eg. must maintain our root
			# as being the max height if our tree is unbalanced (or depths aren't equal).
            level = max(left, right) + 1
			# If we haven't visited a level, append to the results.
            if len(res) <= level:
                res.append([])
			# Append node value at its given level.
            res[level].append(node.val),
            return level
              
        helper(root)

        return res
----------------------------------------------------------------------

Do it for the two subtrees, combine their results, and add the root. Should be slow but got accepted in 52ms (fairly fast for Python).

def findLeaves(self, root):
    if not root: return []
    kids = map(self.findLeaves, (root.left, root.right))
    return map(lambda l, r: (l or []) + (r or []), *kids) + [[root.val]]
-----------------------------------------------

def findLeaves(self, root: TreeNode) -> List[List[int]]:
        res = []
        def recurse(node):
            if not node:
                return None
            if not(node.left or node.right):
                res[-1].append(node.val)
                return None
            node.left = recurse(node.left)
            node.right = recurse(node.right)
            return node
        while root:
            res.append([])
            root = recurse(root)
        return res
-------------------------------------------------------

Algorithm:

I search for the nodes that are leaves and then append them to the list and return the root node back.
When I append the node, I return None and I set the nodes that I have appended to the list to None.
So this is what exactly happens which is same as shown in the figure in the question.
I get the leaves and remove them.
I do this until I get None after setting root to None.
Also, after I do this, I clear the temporary list where I store the item of the leaves.
Time: O(N^2) - in worst case where the trees are left or right skewed. Other wise in balanced trees it will be N because every time I traverse I remove the leaves so roughly the number of nodes in the tree reduce by two because in any Binary Tree, Half of the nodes are leaves.
So, the time complexit will be N+N/2+N/4+....+1 = 2N-1 (Proof: Link)
Not sure about time complexity but this is the best I could come up with. If anybody has a way to correct this or explain this then you're welcome.

Space: O(N) - using list to store the N nodes that are in the Binary Tree and then appending them to final list that is going to be returned.

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        
        ans = []
        final_ans = []
        
        def calc_leaves(node):
            if not node:
                return
            
            if ((node.left is None) and (node.right is None)):
                ans.append(node.val)
                return 
            
            node.left = calc_leaves(node.left)
            node.right = calc_leaves(node.right)
            return node
        
        while root:
            root = calc_leaves(root)
            final_ans.append(list(ans))
            ans.clear()
        
        return final_ans
      
      
      
  
      
      
      
