'''
Given a binary tree with the following rules:

root.val == 0
If treeNode.val == x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
If treeNode.val == x and treeNode.right != null, then treeNode.right.val == 2 * x + 2
Now the binary tree is contaminated, which means all treeNode.val have been changed to -1.

Implement the FindElements class:

FindElements(TreeNode* root) Initializes the object with a contaminated binary tree and recovers it.
bool find(int target) Returns true if the target value exists in the recovered binary tree.
 
 '''


class FindElements:
    
    def dfs(self, node, val):
        if node:
            self.store[val] = 1  # adding the value of node to hashmap
            if node.left:
                vl = (2 * val) + 1  # correcting the value of left node
                self.dfs(node.left,vl)  # left sub tree traversal
            if node.right:
                vr = (2* val) + 2  # correcting the value of right node
                self.dfs(node.right, vr)  # right sub tree traversal

    def __init__(self, root: TreeNode):
        self.store = {}  # hashmap for storing the corrected node values. And searching the values.
        self.dfs(root, 0)  # Traversing the incorrect tree and saving correct values on the way

    def find(self, target: int) -> bool:
		# checking if the target value exists in O(1) time
        if self.store.get(target, None) is not None:
            return True
        else:
            return False
            
---------------------------------------------------------------------------------------------------------
class FindElements(object):

    def __init__(self, root):
        self.st = set()
        
        def recover(root, val) :
            if(root):
                self.st.add(val)
                recover(root.left, 2 * val + 1)
                recover(root.right, 2 * val + 2)
        
        recover(root, 0)
        

    def find(self, target):
        return target in self.st
-------------------------------------------------------------------------------------------------------------------------
class FindElements(object):
    def __init__(self, root):
        self.A = A = set()
        #
        def recover(n,x):
            if n:
                A.add(x)
                recover(n.left , 2*x + 1)
                recover(n.right, 2*x + 2)
        #
        recover(root,0)
    #
    def find(self, target):
        return target in self.A
