'''
A Binary Matrix is a matrix in which all the elements are either 0 or 1.

Given quadTree1 and quadTree2. quadTree1 represents a n * n binary matrix and quadTree2 represents another n * n binary matrix.

Return a Quad-Tree representing the n * n binary matrix which is the result of logical bitwise OR of the two binary matrixes represented by quadTree1 and quadTree2.

Notice that you can assign the value of a node to True or False when isLeaf is False, and both are accepted in the answer.

A Quad-Tree is a tree data structure in which each internal node has exactly four children. Besides, each node has two attributes:

val: True if the node represents a grid of 1's or False if the node represents a grid of 0's.
isLeaf: True if the node is leaf node on the tree or False if the node has the four children.
'''


class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        if quadTree1.isLeaf:
            return Node(True, True) if quadTree1.val else quadTree2
        if quadTree2.isLeaf:
            return Node(True, True) if quadTree2.val else quadTree1
        temp = Node(False, False)
        temp.topLeft = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
        temp.topRight = self.intersect(quadTree1.topRight, quadTree2.topRight)
        temp.bottomLeft = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
        temp.bottomRight = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)
        if (temp.topLeft.isLeaf and temp.topLeft.val) and (temp.topRight.isLeaf and temp.topRight.val) and (temp.bottomLeft.isLeaf and temp.bottomLeft.val) and (temp.bottomRight.isLeaf and temp.bottomRight.val):
            return Node(True, True)
        return temp
      
---------------------------------------------
class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        if quadTree1.isLeaf and quadTree2.isLeaf:                                    # case 1: both are leaf nodes
            node = Node(quadTree1.val | quadTree2.val, 1, None, None, None, None)
            return node
        elif quadTree1.isLeaf and not quadTree2.isLeaf:                              # case 2: node 1 is leaf node, node 2 is not
            node = Node(0, 0, 
                        self.intersect(quadTree1, quadTree2.topLeft), 
                        self.intersect(quadTree1, quadTree2.topRight), 
                        self.intersect(quadTree1, quadTree2.bottomLeft), 
                        self.intersect(quadTree1, quadTree2.bottomRight))
        elif not quadTree1.isLeaf and quadTree2.isLeaf:                              # case 3: node 2 is leaf node, node 1 is not
            node = Node(0, 0, 
                        self.intersect(quadTree1.topLeft, quadTree2), 
                        self.intersect(quadTree1.topRight, quadTree2), 
                        self.intersect(quadTree1.bottomLeft, quadTree2), 
                        self.intersect(quadTree1.bottomRight, quadTree2))
        else:                                                                        # case 4: neither nodes are leaf 
            node = Node(0, 0, 
                        self.intersect(quadTree1.topLeft, quadTree2.topLeft), 
                        self.intersect(quadTree1.topRight, quadTree2.topRight), 
                        self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft), 
                        self.intersect(quadTree1.bottomRight, quadTree2.bottomRight))
            
        if node.topLeft.isLeaf and node.topRight.isLeaf and node.bottomLeft.isLeaf \
            and node.bottomRight.isLeaf and node.topLeft.val == node.topRight.val \
            == node.bottomLeft.val == node.bottomRight.val:                          # shrink quad nodes to one leaf node is values in 4 areas are the same
            return Node(node.topLeft.val, 1, None, None, None, None)
        return node 
