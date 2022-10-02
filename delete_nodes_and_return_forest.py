'''
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest. You may return the result in any order.
'''

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        ans = []
        to_delete = set(to_delete)
        
        def helper(node):
            if not node:
                return None
            node.left = helper(node.left)
            node.right = helper(node.right)
			
			# add children of a node that is to be deleted
            if node.val in to_delete:
                if node.left: 
                    ans.append(node.left)
                if node.right:
                    ans.append(node.right)
                return None
            return node
                
        helper(root)
		# if root is not to be deleted then add it
        if root.val not in to_delete:
            ans.append(root)
        return ans
      
---------------------------------------------------------------------------
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        queue = collections.deque([(root, False)])
        res = []
        deleteSet = set(to_delete)
        
        while queue:
            node, hasParent = queue.popleft()
            # new Root found
            if not hasParent and node.val not in to_delete:
                res.append(node)
                
            hasParent = not node.val in to_delete

            if node.left: 
                queue.append((node.left, hasParent))
                if node.left.val in to_delete:
                    node.left = None
            if node.right:
                queue.append((node.right, hasParent))
                if node.right.val in to_delete:
                    node.right = None
            
        return res
-------------------------------------------------------------------------------------------------------
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        res = []
        stack = [(None, root)]
        to_delete = set(to_delete)
        
        while stack:
            parent, current = stack.pop()
            if not current: continue
            
            if current.val in to_delete:
                stack.append((None, current.left))
                stack.append((None, current.right))
            else:
                if current.left and current.left.val in to_delete:
                    stack.append((None, current.left.left))
                    stack.append((None, current.left.right))
                    current.left = None
                else:
                    stack.append((current, current.left))
                    
                
                if current.right and current.right.val in to_delete:
                    stack.append((None, current.right.left))
                    stack.append((None, current.right.right))
                    current.right = None
                else:
                    stack.append((current, current.right))
                    
                # define the termination condition is when the parent is None and value isn't to be deleted
                if parent is None and current.val not in to_delete:
                    res.append(current)
                    
        return res
      
--------------------------------------------------------------------------------------------------------------------
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        res = []
        stack = [(None, root)]
        to_delete = set(to_delete)
        
        while stack:
            parent, current = stack.pop()
            if not current: continue
            
            if current.val in to_delete:
                stack.append((None, current.left))
                stack.append((None, current.right))
            else:
                if current.left and current.left.val in to_delete:
                    stack.append((None, current.left.left))
                    stack.append((None, current.left.right))
                    current.left = None
                else:
                    stack.append((current, current.left))
                    
                
                if current.right and current.right.val in to_delete:
                    stack.append((None, current.right.left))
                    stack.append((None, current.right.right))
                    current.right = None
                else:
                    stack.append((current, current.right))
                    
                # define the termination condition is when the parent is None and value isn't to be deleted
                if parent is None and current.val not in to_delete:
                    res.append(current)
                    
        return res
