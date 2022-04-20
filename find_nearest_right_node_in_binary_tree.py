'''
Given the root of a binary tree and a node u in the tree, return the 
nearest node on the same level that is to the right of u, or return null if u is the rightmost node in its level.
'''

class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        queue = deque([[root, 0]])
        
        right, right_depth = None, None
        
        while queue:
            node, depth = queue.popleft()
            
            if depth == right_depth: 
                right = node
                right_depth = None
            
            if node == u: right_depth = depth
            
            if node.left: queue.append([node.left, depth + 1])
            if node.right: queue.append([node.right, depth + 1])
             
        
        return right
      
------------------------------------------------------

Basically, I used deque to keep track of the nodes layer by layer. I used a flag to see if we have found the target node or not, and if found, I return the next node.

class Solution:
    def findNearestRightNode(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        queue = collections.deque([root])
        
        while queue:
            size = len(queue)
            found_flag = False
            for _ in range(size):
                u = queue.popleft()
                if found_flag:
                    return u
                if u == p:
                    found_flag = True
                
                if u.left:
                    queue.append(u.left)
                if u.right:
                    queue.append(u.right)
            if found_flag:
                return None
-----------------------------------------------

class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        def preorder(node = root, n_level = 0):
            nonlocal u_level, right
            if not node or right:
                return
            elif node.val == u.val:
                u_level = n_level
                return
            elif n_level == u_level:
                right = node
                return
            preorder(node.left, n_level+1)
            preorder(node.right, n_level+1)
        u_level, right = None, None
        preorder()
        return right
---------------------------------------------------

Algo
Traverse the tree and return the node to the right of u.

Implementation
BFS by level

class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        queue = [root]
        while queue: 
            prev = None 
            newq = []
            for node in queue: 
                if node == u: return prev 
                prev = node 
                if node.right: newq.append(node.right)
                if node.left: newq.append(node.left)
            queue = newq
BFS by index

class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        ii = -1
        queue = [(root, 0)]
        for node, i in queue: 
            if ii != i: ii, prev = i, None 
            if node == u: return prev
            prev = node 
            if node.right: queue.append((node.right, i+1))
            if node.left: queue.append((node.left, i+1))
(pre-order) DFS by index

class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        seen = {}
        stack = [(root, 0)]
        while stack: 
            node, i = stack.pop()
            if node == u: return seen.get(i, [None])[-1]
            seen.setdefault(i, []).append(node)
            if node.left: stack.append((node.left, i+1))
            if node.right: stack.append((node.right, i+1))
--------------------------------------------------------

Explanation
Obviously, Level order traversal (BFS for Binary Tree) will solve the issue
Once we found the target node, the next node in the same level will be returned
if there is no next node in the same level, return None
Use target_met to note whether the target value is met or not
Implementation
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        q = collections.deque([root])
        target_met = False
        while q:
            tmp_q = collections.deque()
            while q:
                node = q.popleft()
                if target_met: return node
                if node.left: tmp_q.append(node.left)
                if node.right: tmp_q.append(node.right)
                if node.val == u.val: target_met = True
            if target_met: return None
            q = tmp_q        
        return None
A different style in case you don't like while loop

class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        q = collections.deque([root])
        target_met = False
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if target_met: return node
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                if node.val == u.val: target_met = True
            if target_met: return None
        return None
---------------------------------------------------------------

We can do a simple BFS to get the next node to the right. When the node to search u is found, the first node in queue is our answer. Here, we need to keep track of level because the first node in the queue might be the first element in the next level.

def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
	queue = collections.deque()
	queue.append((root, 0))
	while queue:
		node, lvl = queue.popleft()
		if node == u:
			if queue and queue[0][1] == lvl:
				return queue[0][0]
			else:
				return None
		if node.left:
			queue.append((node.left, lvl+1))
		if node.right:
			queue.append((node.right, lvl+1))
	return None
--------------------------------------------------------------------
      
              
      
              
