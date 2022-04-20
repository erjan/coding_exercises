'''
Given a root of an N-ary tree, return a deep copy (clone) of the tree.

Each node in the n-ary tree contains a val (int) and a list (List[Node]) of its children.

class Node {
    public int val;
    public List<Node> children;
}
Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).
'''


class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:  #base case of recursion
            return None
        
        node = Node(root.val) #create new node for the root
        
        for child in root.children:
            node.children.append(self.cloneTree(child)) 
			# Call the method recrusively passing each child and append to the childrens of the new node
            
        return node
      
-------------------------------------------------

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root: return 
        return Node(root.val, [self.cloneTree(x) for x in root.children])
      
-------------------------------------------------

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return root
        output = Node(val = root.val)
        output.children = []
        for child in root.children:
            output.children.append(self.cloneTree(child))
        return output

------------------------------------------------------
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        # bfs goes level by level
        if not root:
            return None
        
        from collections import deque
        
        # init with the root clone node
        clone = Node(root.val, [])
        q = deque([(root, clone)])
        
        # exhaust queue
        while q:
            root, cloned = q.popleft()
            
            # for each child, create clone of child then append as children to current root clone and queue up next level 
            for child in root.children:
                cloned_child = Node(child.val, [])
                cloned.children.append(cloned_child)
                q.append((child, cloned_child))
        return clone
      
--------------------------------------------------------

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        dic = {}
        dic[root] = Node(root.val, [])   
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            for child in node.children:
                queue.append(child)
                dic[child] = Node(child.val, [])
                dic[node].children.append(dic[child])
        
        return dic[root]
      
