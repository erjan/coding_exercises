'''
Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.

'''

Just use inorder traversal, which finds the nodes in ascending order, and store the head and previous node in global variables. After the traversal is finished, prev is the "tail" of the double linked list so just connect it to the head.

class Solution(object):
    head = None
    prev = None

    def treeToDoublyList(self, root):
        if not root: return None
        self.treeToDoublyListHelper(root)
        self.prev.right = self.head
        self.head.left = self.prev
        return self.head

    def treeToDoublyListHelper(self, node):
        if not node: return
        self.treeToDoublyListHelper(node.left)
        if self.prev:
            node.left = self.prev
            self.prev.right = node
        else:  # We are at the head.
            self.head = node
        self.prev = node
        self.treeToDoublyListHelper(node.right)
        
-------------------------------------------------------

Intuition
For a binary tree problem, one can often solve it by divide and conquer.
That is to say. Try to formulate your solution by focusing on the root node.

Assume left subtree is solved, what info do you still need to be returned to you to solve the rest of the problem
Assume right subtree is solved, what info do you still need to be returned to to solve the rest of the problem
Given the info above, what actions we want to perform to solve the rest of the problem
For this problem

Assume left subtree is already flattened to a doubly linkedlist, I want the left_head and left_tail. I need the head because root.left is not neccesraily the head anymore after the flattening
Assume right subtree is already flattened I want right_head and right_tail for the same reason.
Now I have left_head, left_tail, right_head and right_tail, all we need to do is to wire them up.
if left_tail:
	left_tail.right = root
	root.left = left_tail

if right_head:
	root.right = right_head
	right_head.left = root
Then We return the head and tail of the current tree to continue the recurion.
if left_head:
	result_head = left_head
else:
	result_head = root

if right_tail:
	result_tail = right_tail
else:
	result_tail = root
return result_head, result_tail

Remember, as human beings. We think about this problem top down but the recursion actually happens bottom up.
Solution

class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return

        head, tail = self.helper(root)
        head.left = tail
        tail.right = head

        return head

    def helper(self, root):
        if not root:
            return None, None

        left_head, left_tail = self.helper(root.left)
        right_head, right_tail = self.helper(root.right)

        if left_tail:
            left_tail.right = root
            root.left = left_tail

        if right_head:
            root.right = right_head
            right_head.left = root

        if left_head:
            result_head = left_head
        else:
            result_head = root

        if right_tail:
            result_tail = right_tail
        else:
            result_tail = root
        return result_head, result_tail
------------------------------------------------------

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        ## RC ##
        ## APPROACH : ITERATIVE + STACK ##
        ## Similar to Leetcode: 94 Binary tree inorder traversal ##
        ## LOGIC ##
        ## 1. using pre order traversal, store the prev node and for current node point that prev node and for that prev node point this current node ##
        ## 2. first when currNode is Node, top of stack is the FirstNode, and as iterating change every next node to LastNode ##
        ## 3. At last link first and last nodes ##
        
		## TIME COMPLEXITY : O(N) ##
		## SPACE COMPLEXITY : O(N) ##

        if not root: 
            return root
        
        if not root.left and not root.right:
            root.left = root
            root.right = root
            return root
        
        stack = []
        currNode = root
        prevNode = None
        firstNode = None
        lastNode = None
        while( stack or currNode ):
            while( currNode ):
                stack.append( currNode )
                currNode = currNode.left
            
            node = stack.pop()
            node.left = prevNode
            if( prevNode ):
                prevNode.right = node
            prevNode = node
            
            if( not firstNode ): 
                firstNode = node
            lastNode = node
            
            currNode = node.right
        
        # joining first and last numbers
        firstNode.left = lastNode
        lastNode.right = firstNode
        
        return firstNode
      
----------------------------------------------

For every node in a BST, the objective is to create 2-way links as follows:

predecessor <--> node
node <--> successor
In a BST:

predecessor is max of left subtree (if there is a left subtree)
successor is min of right subtree (if there is a right subtree)
Algorithm breakdown:

recursively return (min, max) found so far
at each node, we have l_max (predecessor) and r_min (successor), create the 2-way links with the node itself
at the end, we will have the global min and max nodes, connect them separately
return global min node
The idea of returning (min, max) is useful for other problems. For example, 98. Validate Binary Search Tree.

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def link_in_place(root):
            if not root:
                return None, None
            l_min, l_max = link_in_place(root.left)
            r_min, r_max = link_in_place(root.right)
            root.left, root.right = l_max, r_min # predecessor <- node, node -> successor
            if l_max:
                l_max.right = root               # predecessor -> node
            if r_min:
                r_min.left = root                # node <- successor
            return l_min if l_min else root, r_max if r_max else root
        if not root:
            return root
        min_node, max_node = link_in_place(root)
        min_node.left, max_node.right = max_node, min_node
        return min_node
-------------------------------------------------------

Of course, excluding implicit stack space for recursive approach and explicit stack space for iterative approach.

Iterative Approach / In Place :
def ite_trav(root):
	if not root: return root
	stack = []
	prev = cur = head = None
	while stack or root:
		while root:
			stack.append(root)
			root = root.left
		root = stack.pop()
		prev = cur
		cur = root
		if not head: head = cur
		else:
			prev.right = cur
			cur.left = prev
		root = root.right
	cur.right = head
	head.left = cur
	return head
return ite_trav(root)
Recursive Approach :
arr = []
def trav(root):
	if root:
		trav(root.left)
		arr.append(root)
		trav(root.right)

def connect(arr):
	if len(arr) <= 1:
		if not arr: return root
		arr[0].left = arr[0].right = arr[0]
		return arr[0]
	for i in range(len(arr)-1):
		arr[i].right = arr[i+1]
		arr[i].left = arr[i-1]
	j = i+1
	arr[j].right = arr[-j-1]
	arr[j].left = arr[j-1]
	return arr[0]

trav(root)
return connect(arr)


      
      
