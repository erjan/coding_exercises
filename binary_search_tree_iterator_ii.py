'''
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
boolean hasPrev() Returns true if there exists a number in the traversal to the left of the pointer, otherwise returns false.
int prev() Moves the pointer to the left, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

You may assume that next() and prev() calls will always be valid. That is, there will be at least a next/previous number in the in-order traversal when next()/prev() is called.

 
 
 '''


Instead of precalcuating the whole inorder traversal, I have defined an iterative solution which would maintain the stack that would take an additional space of only O(h) where h is the height of the tree(h can be N in worst case).

Because we also need to track prev, we would need to store the list of nodes which are processed after inorder and idx to check where in the list we are.
So in all we need to initialize following instance variables:

stck - stores predecessors of a node
list - stores nodes which are processed after inorder. Remember that the cumulative space for list and stck would be O(N)
idx - stores the index of the iterator
class BSTIterator:

    # T = O(h) where h is height of tree
    def __init__(self, root: Optional[TreeNode]):
        self.stck = [] # for tree traversal
        self.list = [] # for storing the vals once it's processed
        self.idx = -1 # ptr for self.list
        # initialize stack with first left inorder
        self.left_inorder(root) 
    
    # find predecessors for a node and update stck
    def left_inorder(self, node): 
        while node:
            self.stck.append(node)
            node = node.left        
    
    # T = O(1) 
    def hasNext(self) -> bool:
        return len(self.stck)>0 or self.idx < len(self.list)-1   
    
    # T = O(h) 
    def next(self) -> int:        
        if self.idx + 1 < len(self.list): # check if the idx is moved due to prev() calls
            self.idx +=1
            return self.list[self.idx]    
        else:            
            popped = self.stck.pop()
            self.list.append(popped.val) # update list in inorder fashion
            # perform left inorder if needed
            if popped.right:
                self.left_inorder(popped.right) 
            self.idx +=1
            return popped.val
        
    # T = O(1) 
    def hasPrev(self) -> bool:
        return self.idx > 0    
    
    # T = O(1)
    def prev(self) -> int:
        self.idx -= 1
        return self.list[self.idx]    
Time complexity:
O(1) - for hasPrev(), prev() and hasNext() calls
O(h) - for constructor and next() where h is height of the tree (worst case h would be N)

Space complexity:
S = O(N) - for storing the list of all nodes in the tree

----------------------------------------------------------------------


Firstly, please refer to 173. BST iterator and try to solve it. Then, we only need to add a list that stores all the traversed values, and a pointer thats points to the current node, and then we can solve this question.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left 
        self.inorder = []
        self.pointer = -1

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.pointer < len(self.inorder) - 1 or self.stack

    def next(self):
        """
        :rtype: int
        """
        if 0 <= self.pointer < len(self.inorder) - 1:
            self.pointer += 1
            return self.inorder[self.pointer].val
		#This part is simply BST iterator
        node = self.stack[-1]
        if node.right:
            n = node.right
            while n:
                self.stack.append(n)
                n = n.left
        else:
            n = self.stack.pop()
            while self.stack and self.stack[-1].right == n:
                n = self.stack.pop()
        self.inorder.append(node)
        self.pointer += 1
        #print(node.val)
        return node.val
            

    def hasPrev(self):
        """
        :rtype: bool
        """
        return self.pointer >= 1
        

    def prev(self):
        """
        :rtype: int
        """
        self.pointer -= 1
        return self.inorder[self.pointer].val
----------------------------------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.ans = []
        stack = []
        while True:
            
            while root:
                
                stack.append(root)
                root = root.left
            if not stack:
                break
            node = stack.pop()
            self.ans.append(node.val)
            root = node.right
            
        self.i = -1


    def hasNext(self) -> bool:
        
        return self.i + 1 < len(self.ans)
        

    def next(self) -> int:
      
        self.i += 1
        return self.ans[self.i]


    def hasPrev(self) -> bool:
        return self.i - 1 >= 0
        

    def prev(self) -> int:
        self.i-=1
        return self.ans[self.i]
        
---------------------------------------------------------------------

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.mem = []
        self.ptr = 0

        def rec(node):
            if node:
                if node.left:
                    rec(node.left)
                self.mem.append(node.val)
                if node.right:
                    rec(node.right)
        rec(root)

    def hasNext(self) -> bool:
        return self.ptr < len(self.mem)

    def next(self) -> int:
        self.ptr += 1
        return self.mem[self.ptr-1]

    def hasPrev(self) -> bool:
        #print(self.ptr)
        return self.ptr > 1
        
    def prev(self) -> int:
        self.ptr -= 1
        return self.mem[self.ptr-1]
----------------------------------------------------------

class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []

        cur = root
        while cur.left:
            cur = cur.left
        self._min = cur.val
        cur.left = TreeNode(float('-inf'))

        cur = root
        while cur.right:
            cur = cur.right
        self._max = cur.val
        cur.right = TreeNode(float('inf'))

        cur = root
        while cur:
            self.stack.append(cur)
            cur = cur.left

    def hasNext(self) -> bool:
        return self.stack[-1].val < self._max

    def next(self) -> int:
        if self.stack[-1].right:
            # Has a right child, so we can find the next element in the right branch.
            # Leave the last node in the stack as the smallest leaf in that branch.
            cur = self.stack[-1].right
            while cur:
                self.stack.append(cur)
                cur = cur.left
        else:
            # Go up to the first parent that is a left child of his parent,
            # and get that higher parent as the last element in the stack.
            last = self.stack.pop()
            while self.stack[-1].right == last:
                last = self.stack.pop()
        return self.stack[-1].val

    def hasPrev(self) -> bool:
        return self.stack[-1].val > self._min

    def prev(self) -> int:
        if self.stack[-1].left:
            # Has a left child, so we can find the prev element in the left branch.
            # Leave the last node in the stack as the biggest leaf in that branch.
            cur = self.stack[-1].left
            while cur:
                self.stack.append(cur)
                cur = cur.right
        else:
            # Go up to the first parent that is a right child of his parent,
            # and get that higher parent as the last element in the stack.
            last = self.stack.pop()
            while self.stack[-1].left == last:
                last = self.stack.pop()
        return self.stack[-1].val
      
      
        
      
