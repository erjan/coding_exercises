'''

Given the root of an N-ary tree of unique values, and two nodes of the tree p and q.

You should move the subtree of the node p to become a direct child of node q. If p is already a direct child of q, do not change anything. Node p must be the last child in the children list of node q.

Return the root of the tree after adjusting it.

 

There are 3 cases for nodes p and q:

Node q is in the sub-tree of node p.
Node p is in the sub-tree of node q.
Neither node p is in the sub-tree of node q nor node q is in the sub-tree of node p.
In cases 2 and 3, you just need to move p (with its sub-tree) to be a child of q, but in case 1 the tree may be disconnected, thus you need to reconnect the tree again. Please read the examples carefully before solving this problem.

'''

class Solution:
    def moveSubTree(self, root: 'Node', p: 'Node', q: 'Node') -> 'Node':
        # make the node-to-parent mapping dictionary
        node2parent = {root: None}
        stack = [root]
        while stack:
            node = stack.pop()
            for child in node.children:
                node2parent[child] = node
                stack.append(child)
                
        # check whether p is already a direct child of q
        # if yes, return the original root directly
        if node2parent[p] == q:
            return root

        # check whether "q" is in the subtree of "p"
        flag = False
        node = q
        while node:
            parent = node2parent[node]
            if parent == p:
                flag = True
                break
            else:
                node = parent
                
        # check whether "p" is the root or not
        p_parent = node2parent[p]
        q_parent = node2parent[q]
        if p_parent is None:
            q_parent.children.remove(q)
            q.children.append(p)
            return q
        else:
            if flag: # if "q" is in the subtree of "p" 
                q_parent.children.remove(q)
                p_index = p_parent.children.index(p)
                p_parent.children[p_index] = q
            else: # "q" is NOT in the subtree of "p"
                p_parent.children.remove(p)
            q.children.append(p)
            return root
