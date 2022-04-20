'''
Given the root of a binary search tree and a node p in it, return the in-order 
successor of that node in the BST. If the given node has no in-order successor in the tree, return null.

The successor of a node p is the node with the smallest key greater than p.val.

 

Example 1:


Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.
Example 2:


Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        curr = root
        stack = []
        is_next = False
        
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            node = stack.pop()
            
            if is_next:
                return node
            
            if node == p:
                is_next = True
                
            curr = node.right
            
        
        return None
            
---------------------------------------------------------

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':      
        cur = root
        candidate = None      
        while cur:
            if cur.val > p.val:
                candidate = cur
                cur = cur.left #move left and see if even smaller val could be greater than p
            else:
                cur = cur.right 
        return candidate
------------------------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        
        self.successor = None
        
        def check_successor(node):
            
            if not node: return
            
            if node.val > p.val:
                
                if self.successor:
                    if self.successor.val > node.val:
                        self.successor = node
                else: self.successor = node
                    
                       
        def util(node):
            
            if node:
                util(node.left)
                check_successor(node)
                util(node.right)
        
        util(root)
        return self.successor

-----------------------------------------

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        if not root:
            return None
        
        if p.val >= root.val:
            return self.inorderSuccessor(root.right, p)
        else:
            return self.inorderSuccessor(root.left, p) or root
-----------------------------------------------

Find the inorder traversal of the tree, which returns a sorted list.
With the sorted list, we can get the number that comes after the value we want the inorder successor of by.
class Solution:

def in_order_traversal(self, root):
    
    elements: List = []
        
    if root is None:
        return root
    
    if root.left:
        elements += self.in_order_traversal(root.left)
        
    elements.append(root)
    
    if root.right:
        elements += self.in_order_traversal(root.right)
        
    return elements

def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
    
    ordered_tree = self.in_order_traversal(root)
    
    for index, element in enumerate(ordered_tree):
        
        if index + 1 < len(ordered_tree) and element == p:
            
            return ordered_tree[index + 1]
        
    return None
---------------------------------------------------------------------

import bisect
class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        nodes_values = []
        nodes = []
        
        def inorder(node):
            nonlocal nodes, nodes_values
            if node:
                if node.left:
                    inorder(node.left)
                
                nodes_values.append(node.val)
                nodes.append(node)
                
                if node.right:
                    inorder(node.right)
                    
        inorder(root)
        index = bisect.bisect_left(nodes_values, p.val)
        
        if index + 1 >= len(nodes):
            return None
        
        else:
            return nodes[index + 1]
          
  
          
      
      
        
