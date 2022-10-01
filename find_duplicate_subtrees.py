'''
Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.
'''


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        
        seen = collections.defaultdict(int)
        res = []
        
        def helper(node):
            if not node:
                return
            sub = tuple([helper(node.left), node.val, helper(node.right)])
            if sub in seen and seen[sub] == 1:
                res.append(node)
            seen[sub] += 1
            return sub
        
        helper(root)
        return res
      
---------------------------------------------------------------------------
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        subtrees = {}
        mono_id = 1
        visited = set()
        res = []
        def helper(node: TreeNode) -> int:
            nonlocal mono_id
            if not node:
                return 0
            left_id = helper(node.left)
            right_id = helper(node.right)
            key = (node.val, left_id, right_id)
            if key in subtrees:
                # already seen this unique subtree
                if key not in visited:
                    # first time re-visiting this unique subtree
                    visited.add(key)
                    res.append(node)
            else:
                # first time seeing this unique subtree
                subtrees[key] = mono_id
                mono_id += 1
            return subtrees[key]
        helper(root)
        return res
      
---------------------------------------------------------------------------------------
class Solution:
    def dfs(self, root, lookup, duplicates):
        if not root:
            return '.'
        subtree = str(root.val) + '-' + self.dfs(root.left, lookup, duplicates) + '-' + self.dfs(root.right, lookup, duplicates) 
        if subtree in lookup:
            if lookup[subtree] == 1:
                duplicates.append(root)
            lookup[subtree] += 1
        else:
            lookup[subtree] = 1
        return subtree
    
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:    
        lookup, duplicates = {}, []
        self.dfs(root, lookup, duplicates)
        return duplicates
