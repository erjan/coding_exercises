'''
We run a preorder depth-first search (DFS) on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  If the depth of a node is D, the depth of its immediate child is D + 1.  The depth of the root node is 0.

If a node has only one child, that child is guaranteed to be the left child.

Given the output traversal of this traversal, recover the tree and return its root.

 
 '''

class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        root = None
        for val in traversal.split('-'):
            if not root or val == '':
                parent = (parent.right if parent.right else parent.left) if root else (root := TreeNode(int(val)))
            else:
                parent, _ = root, setattr(parent, 'right' if parent.left else 'left', TreeNode(int(val)))
        return root
      
----------------------------------------------------------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:

        l, level = collections.deque(), 0
        right, left = 0, 0 
        while left < len(traversal):
            if traversal[left] == '-':
                level += 1
                left += 1
            else:
                right = left
                while right < len(traversal) and traversal[right] != '-':
                    right += 1
                num = int(traversal[left: right])
                l.append((num, level))
                level = 0
                left = right
        
        def dfs(parent=None, d=0, pos=''):
            if not l or  l[0][1] < d:
                return
            node = TreeNode(val=l[0][0])
            l.popleft()
            if parent:
                if pos == 'left':
                    parent.left = node
                else:
                    parent.right = node
            
            dfs(node, d+1, 'left')
            dfs(node, d+1, 'right')

            return node
        root = dfs()
        return root
        
            
