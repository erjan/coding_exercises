'''
You have a binary tree with a small defect. There is exactly one invalid node where its right child incorrectly points to another node at the same depth but to the invalid node's right.

Given the root of the binary tree with this defect, root, return the root of the binary tree after removing this invalid node and every node underneath it (minus the node it incorrectly points to).

Custom testing:

The test input is read as 3 lines:

TreeNode root
int fromNode (not available to correctBinaryTree)
int toNode (not available to correctBinaryTree)
After the binary tree rooted at root is parsed, the TreeNode with value of fromNode will have its right child pointer pointing to the TreeNode with a value of toNode. Then, root is passed to correctBinaryTree.
'''


Explanation
q: Deque for level order traversal
p: Hash table to store a tuple indicates the parent of key {cur_node: (parent_node, is_left_node)}
visited: Hash set to determine whether node is visited
Process:
Start with level order traversal
If same node being visited twice, meaning we meet the child of the wrong node (we call it cur)
Find the grandparent of cur, and let the grandparent node (grand_p) de-link its child (the wrong node)
Return root
Implementation
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        q = collections.deque([root])
        p, visited = dict(), set()
        while q:
            cur = q.popleft()
            if cur in visited:
                grand_p, is_left = p[p[cur][0]]
                if is_left: grand_p.left = None
                else: grand_p.right = None    
                return root
            visited.add(cur)
            if cur.left:
                p[cur.left] = (cur, 1)
                q.append(cur.left)
            if cur.right:
                p[cur.right] = (cur, 0)
                q.append(cur.right)
        return root
------------------------------------------------------------------------------------

Algo
Traverse the tree and find the invalid node.

Implementation
DFS

class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        seen = set()
        stack = [(root, None)]
        while stack:
            node, prev = stack.pop()
            if node.right and node.right.val in seen: 
                if node == prev.left: prev.left = None
                if node == prev.right: prev.right = None
                return root 
            seen.add(node.val)
            if node.left: stack.append((node.left, node))
            if node.right: stack.append((node.right, node))
BFS

class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        queue = [(root, None)]
        seen = set()
        for node, prev in queue: 
            if node.right and node.right.val in seen: 
                if node == prev.left: prev.left = None
                if node == prev.right: prev.right = None
                return root 
            seen.add(node.val)
            if node.right: queue.append((node.right, node))
            if node.left: queue.append((node.left, node))
-------------------------------------------------------------------

Find the node using dfs with the help of dictionary that keeps track of parent and child. If a node is pointing to some other node and then it will be visited twice. So, when you come across a node that is visited twice, fetch the parent. This is the from_node.

Now just delete the from_node by returning None. This deletes the node.

When you return None or just nothing, the child node is treated as None. Hence, it is deleted. :)

class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        
        self.seen = defaultdict(int)
        self.from_node = None
        
        def find_from_node(root, parent):
            if not root:
                return
            
            if root.val in self.seen:
                self.from_node = self.seen[root.val]
                return
            
            self.seen[root.val] = parent.val if parent else None
            find_from_node(root.left, root)
            find_from_node(root.right, root)
            
        find_from_node(root, None)
        
        def traverse(root):
            
            if not root:
                return
            
            if root.val == self.from_node:
                return
            
            root.left = traverse(root.left)
            root.right = traverse(root.right)
            
            return root
        
        traverse(root)
        return root
      
      
              
      
