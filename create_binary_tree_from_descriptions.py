'''
You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti] indicates that parenti is the parent of childi in a binary tree of unique values. Furthermore,

If isLefti == 1, then childi is the left child of parenti.
If isLefti == 0, then childi is the right child of parenti.
Construct the binary tree described by descriptions and return its root.

The test cases will be generated such that the binary tree is valid.
'''


Code is self explanatory...
I used hashmap to store node's value as key and node as value... so by using key I can access particular node at any time....
I took nodes set which I pushed all node values in it...
I took children set which I pushed all children values in it..

If a node in the nodes set is not present in children set... that means that node is not a children.. i.e, that node doesnt have any parent... so return that particular node as root....


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        hashmap = {}
        nodes = set()
        children = set()
        for parent,child,isLeft in descriptions:
            nodes.add(parent)
            nodes.add(child)
            children.add(child)
            if parent not in hashmap:
                hashmap[parent] = TreeNode(parent)
            if child not in hashmap:
                hashmap[child] = TreeNode(child)
            if isLeft:
                hashmap[parent].left = hashmap[child]
            if not isLeft:
                hashmap[parent].right = hashmap[child]
        
        for node in nodes:
            if node not in children:
                return hashmap[node]
