'''
Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).

Each node will have a reference to its parent node. The definition for Node is below:

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)."
'''

I wanted to pose an easy-to-understand alternative to most answers here. We first find the depth of each pointer, and then move each pointer to the same level in the tree. Then, we move the pointers up level by level until they meet.

Summary:

Find the depth of each pointer
Move the deeper pointer up until it is at the same level as the other pointer
Move each pointer up level-by-level until they meet
Time Complexity: O(h)
Space Complexity: O(1)

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 8
Output: 3
drawing

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
drawing

"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def get_depth(self, p):
		# helper function to find the depth of the pointer in the tree
        depth = 0
        while p:
            p = p.parent
            depth += 1
        return depth
    
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
		# find the depth of each pointer
        p_depth = self.get_depth(p)
        q_depth = self.get_depth(q)
		
		# Move the lower pointer up so that they are each at the same level. 
		# For the smaller depth (p_depth < q_depth or q_depth < p_depth), 
		# the loop will be skipped and the pointer will stay at the same depth.
        for _ in range(p_depth - q_depth):
            p = p.parent
        for _ in range(q_depth - p_depth):
            q = q.parent
        
		# Now that they are at the same depth, move them up the tree in parallel until they meet
        while p != q:
            p=p.parent
            q=q.parent
        return p
      
------------------------------------------------------------------------

First, a more intuitive way -- two passes
To me, a more intuitive way of solving this is to find the length of each path to the root, then iterating on longer path until both pointers are at the same level of the tree.
From there, you can iterate up until they are pointing at the same node.

One pass -- sort of.. Time -> q + p
Instead of precalculating the length of each path, we can use the fact that a+b == b+a to get both nodes on the same level on the tree.

We can say there are two different paths: q_path and p_path

You u can essentially create two equally sized, but different paths.

a_path = q_path + p_path
b_path = p_path + q_path
You can then iterate down each path until the pointers are the same. Then you have found your first common ancestor. (because, by tacking on the other path, they are guarenteed to be at the same level after they each have done a full pass.)

Here are the paths (from child to parent) laid out. Where the two equal each other after doing both paths is the first common ancestor. (in this example, 4)

q_path = [2, 0, 1, 6, 7, 4, 5]
p_path = [9, 8, 3, 4, 5]
                                     
a_path = [2, 0, 1, 6, 7, 4, 5, 9, 8, 3, 4, 5]
b_path = [9, 8, 3, 4, 5, 2, 0, 1, 6, 7, 4, 5]
*<if they start at the same level, they will meet at the first common ancestor without going theough the other's path.>

We don't have q_path and p_path as lists, but we do have each of their starting nodes, and that's all we need.

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        a_node = p
        b_node = q 
        
        while a_node != b_node:
            if a_node.parent: 
                a_node = a_node.parent
            else:
                a_node = q
            
            if b_node.parent:
                b_node = b_node.parent
            else:
                b_node = p
        return a_node

--------------------------------------------------------------------------------------------------------------------------

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
          
        # O(n) time O(1) space
        nodeP,nodeQ=p,q
        while p!=q:
            p=p.parent if p.parent else nodeQ
            q=q.parent if q.parent else nodeP
        
        return p
 class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':       
        #O(N) time and space
        def getParent(x,path):
            if not x.parent:
                return path
            return getParent(x.parent,path+[x.parent])
        pParent=getParent(p,[p])[::-1]
        qParent=getParent(q,[q])[::-1]
        
        
        for np,nq in zip(pParent,qParent):
            if np==nq: lca=np
        return lca
------------------------------------------------------

Think about it, there are three cases:

There is an equal distance between p and q
p has a longer distance to travel than q to the LCA
q has a longer distance to travel than p to the LCA
Here's my first attempt at this problem. Basically, traverse p, then, traverse q and return the first node we've already seen. We could swap p and q and it would still work. The downside is this uses O(n) memory.

def lowestCommonAncestor(p, q):

	seen = set()

	while p:
		seen.add(p)
		p = p.parent

	while q:
		if q in seen: return q
		q = q.parent
-------------------------------------------------------

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p1, q1 = p, q
        
        while p1 != q1:
            if not p1.parent:
                p1 = q
            else:
                p1 = p1.parent
                
            if not q1.parent:
                q1 = p
            else:
                q1 = q1.parent
        
        return p1
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        s = set()
        
        while p:
            s.add(p)
            p = p.parent
        
        while q:
            if q in s:
                return q
            q = q.parent
        
        return None
      
      
    
      
      
