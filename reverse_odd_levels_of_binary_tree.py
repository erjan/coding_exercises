'''
Given the root of a perfect binary tree, reverse the node values at each odd level of the tree.

For example, suppose the node values at level 3 are [2,1,3,4,7,11,29,18], then it should become [18,29,11,7,4,3,1,2].
Return the root of the reversed tree.

A binary tree is perfect if all parent nodes have two children and all leaves are on the same level.

The level of a node is the number of edges along the path between it and the root node.
'''

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        def dfs(node1, node2, level):
            if not node1 or not node2:
                return
            if level % 2 != 0:
                node1.val, node2.val = node2.val, node1.val
                
            dfs(node1.left, node2.right, level + 1)
            dfs(node1.right, node2.left, level + 1)
        
        dfs(root.left, root.right, 1)
        return root
        
        

It seems to me that BFS is more natural to come up with, for completeness, dfs is also included in this solution.

BFS:

The idea is to use BFS and reverse the value of the nodes in the queue at an odd level. Note that, since we are only sweeping the value of the nodes in the queue, their children won't change and can still be used to continue the BFS. We can just return the root at the end.

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root]) ### Initialize the queue with root.
        level = 0 ### Start with level 0 (root).
        while q:
            ### When we are at an odd level, reverse the value of each node in the queue.
            if level %2 != 0:
                l = 0           ### left pointer.
                r = len(q)-1    ### right pointer.
                while l<r: 
                    ### Sweep the value of the left node and right node.
                    q[l].val,q[r].val = q[r].val,q[l].val
                    l+=1
                    r-=1
            ### Same as regular BSF, adding the node for the next level.
            for _ in range(len(q)):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            ### Increase the level.
            level += 1
        return root
DFS:

The key to solving this problem recursively for each level independently, we have to pass in two nodes at the same level and these two nodes need to be the left most and right most nodes that have not been visited. Then keep tracking the level to sweep the node values at an odd level.

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node1, node2, level):
            
            ### Actually only need to check one node since it is a perfect binary tree, checking two for easy understanding here.
            if not node1 or not node2:
                return
            
            ### When the level is odd, sweep the value for node1 and node2.
            if level % 2 != 0:
                node1.val, node2.val = node2.val, node1.val
            
            ### The key to using dfs is to pass in the left of node1 and right of node2.
            ### And then, pass in the right of node1 and left of node 2.
            ### These two nodes (node1.left and node2.right) or (node1.right and node2.left) are always on the same level and are the left most and right most nodes that have not been visited.
            dfs(node1.left, node2.right, level + 1)
            dfs(node1.right, node2.left, level + 1)
        
        ### start with level 1, since level 1 only has 2 nodes, just passing in the left and right with level of 1.
        dfs(root.left, root.right, 1)

        return root
