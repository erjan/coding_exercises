'''
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.
'''


class BSTIterator(object):
    def __init__(self, root: Optional[TreeNode]):
        self.treenodes = deque()
        def inorder(node: Optional[TreeNode]) -> None:
            # Appends the value of each node to self.treenodes
            # via inorder traversal of binary tree
            if node:
                inorder(node.left)
                self.treenodes.append(node.val)
                inorder(node.right)
        inorder(root)
    
    def next(self) -> int:
        return self.treenodes.popleft()

    def hasNext(self) -> bool:
        return bool(self.treenodes)
-----------------------------------------------------
class BSTIterator(object):

    def __init__(self, root):
        # get the in order tree node values
        def inorder(root):
            if not root:    return []
            return inorder(root.left) + [root.val] + inorder(root.right)
        
        self.treenodes = inorder(root)
        
        
    def next(self):
        # pop out the current smallest int
        return self.treenodes.pop(0)
        

    def hasNext(self):
        # check if there are remaining int
        return len(self.treenodes) != 0
