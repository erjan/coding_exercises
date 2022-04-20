'''
Given a node in a binary search tree, return the in-order successor of that node in the BST. If that node has no in-order successor, return null.

The successor of a node is the node with the smallest key greater than node.val.

You will have direct access to the node but not to the root of the tree. Each node will have a reference to its parent node. Below is the definition for Node:

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
'''

Explanation
There are only 3 ways that one node may have a successor
it has a right child
it has a parent
it is the left child of its parent
it is the right child of its parent
Discuss the scenarios accordingly will get the answer, check comments for more detail
Implementation
class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        if not node: return None                        # if not node: return None
        elif node.right:                                # if node has right child, return most left of right child
            node = cur = node.right
            while node: cur, node = node, node.left
            return cur
        elif node.parent and node.parent.left == node:  # if node is a left child of its parent, return parent
            return node.parent
        elif node.parent and node.parent.right == node: # if node is a right child of its parent, reaching to parent until node is a left child of the parent
            while node.parent and node == node.parent.right: 
                node = node.parent
            return node.parent    
        else: return None   
----------------------------------------------------------

There are only two routes we can go:

right and then left as much as possible
up until we find the first parent which is to the right of us
def inorderSuccessor(self, node: 'Node') -> 'Node':
	if not node: return node
	if node.right: # we go right and then left as much as possible
		node = node.right
		while node.left: node = node.left
		return node
	while node.parent: # we go up until we are on the left of our parent
		if node.parent.left == node: return node.parent
		node = node.parent
	return None
--------------------------------------------------

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        
        if not node:
            return None
        
        def get_left(node):
            while node.left:
                node=node.left
            return node
        
        def get_right(node):
            if node.right:
                return get_left(node.right)
        
        def get_parent(node):
            child=node
            while node.parent:
                node=node.parent
                if node.left==child:
                    return node
                child=node

        if node.right:
            return get_right(node)
        
        return get_parent(node)
-------------------------------------------------

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        while node and node.parent and node.parent.val < node.val:
            node = node.parent
        return node.parent if node else None
----------------------------------------

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        # Case 1
        # has right node
        # find left most of right node
        if node.right: 
            ans = node.right
            while ans.left: 
                ans = ans.left
            return ans
        
        # Case 2
        # no right node
        # go up to parent until a node is left child
        # if cannot find then null
        else: 
            parent = node.parent
            while parent != None and node != parent.left: 
                node = node.parent
                parent = node.parent
            if parent != None and parent.left == node: 
                return parent
            else: 
                return None
---------------------------

In Binary Search Tree, the value in each node must be greater than (or equal to) any values in its left subtree but less than (or equal to) any values in its right subtree.
In-order traversal is to traverse the tree in the order of left subtree, root, right subtree.
So the Inorder successor of a node is the node larger than the current node.
There are two cases:
Case 1: if the node has a right child: find the leftmost child of node.right
Case 2: if the node doesn't have a right child: find the first parent whose value larger than the node.

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, parent):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
"""
class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
	# if the node has a right child: find the leftmost child of node.right
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
		# if the node doesn't have a right child: find the first parent whose value larger than the node.
        else:
            val = node.val
            node = node.parent
            while node and node.val < val:
                node = node.parent
            return node
              
      
      

        
