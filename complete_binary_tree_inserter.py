'''
A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.

Design an algorithm to insert a new node to a complete binary tree keeping it complete after the insertion.

Implement the CBTInserter class:

CBTInserter(TreeNode root) Initializes the data structure with the root of the complete binary tree.
int insert(int v) Inserts a TreeNode into the tree with value Node.val == val so that the tree remains complete, and returns the value of the parent of the inserted TreeNode.
TreeNode get_root() Returns the root node of the tree.
'''


class CBTInserter:
    def __init__(self, root: Optional[TreeNode]):
        self.d = dict()
        def dfs(node, i):
            if not(node): return 0
            self.d[i] = node
            return 1 + dfs(node.left, 2*i) + dfs(node.right, 2*i+1)
        self.root = root
        self.l = dfs(root, 1)

    def insert(self, val: int) -> int:
        self.l += 1
        self.d[self.l] = TreeNode(val)
        if(self.l % 2):
            self.d[self.l//2].right = self.d[self.l]
        else:
            self.d[self.l//2].left = self.d[self.l]
        return self.d[self.l//2].val

    def get_root(self) -> Optional[TreeNode]:
        return self.root
