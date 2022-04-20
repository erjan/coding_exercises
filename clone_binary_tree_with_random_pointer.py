'''
A binary tree is given such that each node contains an additional random pointer which could point to any node in the tree or null.

Return a deep copy of the tree.

The tree is represented in the same input/output way as normal binary trees where each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (in the input) where the random pointer points to, or null if it does not point to any node.
You will be given the tree in class Node and you should return the cloned tree in class NodeCopy. NodeCopy class is just a clone of Node class with the same attributes and constructors.
'''


class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        # just dfs but there can be cycles, so you need to detect that
        visited = {}
        
        def dfs(root):
            if not root:
                return None
            if root in visited:
                return visited[root]
            
            cloned = NodeCopy(root.val)
            visited[root] = cloned
            
            cloned.left = dfs(root.left)
            cloned.right = dfs(root.right)
            cloned.random = dfs(root.random)
            
            return cloned
        
        return dfs(root)
--------------------------------------

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        def dfs(node):
            if not node:
                return node
            
            if node in newNodes:
                return newNodes[node]
            
            newNode = NodeCopy(node.val)
            newNodes[node] = newNode
            
            newNode.left = dfs(node.left)
            newNode.right = dfs(node.right)
            newNode.random = dfs(node.random)
            
            return newNode
        
        newNodes = {}        
        return dfs(root)
-----------------------------------------------

class Solution:
    def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':
        mp = {}
        
        def fn(node):
            """Return cloned binary tree."""
            if not node: return 
            if node not in mp: 
                mp[node] = NodeCopy(node.val)
                mp[node].left = fn(node.left)
                mp[node].right = fn(node.right)
                mp[node].random = fn(node.random)
            return mp[node]
        
        return fn(root)
class Solution:
    def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':
        if not root: return 
        mp = defaultdict(NodeCopy)
        stack = [root]
        while stack: 
            node = stack.pop()
            mp[node].val = node.val
            if node.left: 
                mp[node].left = mp[node.left]
                stack.append(node.left)
            if node.right: 
                mp[node].right = mp[node.right]
                stack.append(node.right)
            if node.random: mp[node].random = mp[node.random]
        return mp[root]
class Solution {
public:
    NodeCopy* copyRandomBinaryTree(Node* root) {
        if (!root) return nullptr; 
        unordered_map<Node*, NodeCopy*> mp; 
        stack<Node*> stk; 
        stk.push(root); 
        
        while (stk.size()) {
            Node* node = stk.top(); stk.pop(); 
            if (!mp[node]) mp[node] = new NodeCopy(); 
            mp[node]->val = node->val; 
            if (node->left) {
                if (!mp[node->left]) mp[node->left] = new NodeCopy(); 
                mp[node]->left = mp[node->left]; 
                stk.push(node->left); 
            }
            if (node->right) {
                if (!mp[node->right]) mp[node->right] = new NodeCopy(); 
                mp[node]->right = mp[node->right]; 
                stk.push(node->right); 
            }
            if (node->random) {
                if (!mp[node->random]) mp[node->random] = new NodeCopy(); 
                mp[node]->random = mp[node->random]; 
            }
        }
        return mp[root]; 
    }
};
------------------------------------------------------------------------------------


Similar to how we solve the other "clone" style questions, we are going to use a hashmap to store a mapping between old => new values.

We can iterate through the tree using a BFS level order traversal and a queue.

For each node in the queue we need to check whether we have already cloned the random, left and right nodes. If we haven't then we need to clone them and update the current node's clone with the cloned value of random/left/right respectively.

If you are wondering why we also add the random node to the queue in the case that it hasn't been cloned, the reason for this is that in the edge case where the random pointer points to the same node as the next pointer, then the random/left node will not be added to the queue and you will have a missing random index referrence in your final result, failing the judge.

Time: O(N)
Space: O(N)

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        if not root:
            return None
        
        copy_dict = {root: NodeCopy(root.val)}
        
        queue = collections.deque([root])
        
        while queue:
            node = queue.popleft()
                        
            if node.random and node.random not in copy_dict:
                copy_dict[node.random] = NodeCopy(node.random.val)
                queue.append(node.random)
            
            copy_dict[node].random = copy_dict.get(node.random, None)
            
            if node.left and node.left not in copy_dict:
                copy_dict[node.left] = NodeCopy(node.left.val)
                queue.append(node.left)
            
            copy_dict[node].left = copy_dict.get(node.left, None)
        
            if node.right and node.right not in copy_dict:
                copy_dict[node.right] = NodeCopy(node.right.val)
                queue.append(node.right)
            
            copy_dict[node].right = copy_dict.get(node.right, None)
        
        return copy_dict[root]
-----------------------------------------------------

This question is an extension of the question

https://leetcode.com/problems/copy-list-with-random-pointer

Steps:

Modify the tree by creating NodeCopy nodes by making copy of the actual nodes data and keeping that at the left.
Now to populate the random pointer of the NodeCopy tree we
copyNode.random = root.random.left
Now decouple the two trees.
    def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':
        
        self.createNodeCopyNodes(root)
        self.populateRandom(root)
                    
        return self.breakNodes(root)

        
    def breakNodes(self, root):
        if not root:
            return
        
        newRoot = root.left
        
        root.left = newRoot.left
        root.right = newRoot.right
                
        if root.left:
            newRoot.left = self.breakNodes(root.left)
            
        if root.right:
            newRoot.right = self.breakNodes(root.right)
        
        return newRoot

        
    def populateRandom(self, root):
        if not root:
            return
    
        copyNode = root.left
        if root.random:
            copyNode.random = root.random.left
        else:
            copyNode.random = None
            
        self.populateRandom(copyNode.left)
        self.populateRandom(copyNode.right)
        

    def createNodeCopyNodes(self, root):
        if not root:
            return
        
        newNode = NodeCopy(root.val)
        
        newNode.left = root.left
        newNode.right = root.right
        
        root.left = newNode
        root.right = None
        
        self.createNodeCopyNodes(newNode.left)
        self.createNodeCopyNodes(newNode.right)
--------------------------------------------------------------        
        
      

      
