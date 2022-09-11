'''
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL
'''



"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return root
        
        queue = collections.deque([root])
        res = []
        
        while queue:
            n = len(queue)
            level = []
            for i in range(n):

                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                level.append(node)
            
            prev = level[0]
            for i in range(1, len(level)):
                
              
                    prev.next = level[i]
                    prev = level[i]
                
        
        
        return root
