'''
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize an N-ary tree. An N-ary tree is a rooted tree in which each node has no more than N children. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that an N-ary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following 3-ary tree
'''


# Do preorder travel, but add number of children after the root value
from collections import deque

class Codec:

	def serialize(self, root):
		lst = []
		self.serializeHelper(root, lst)
		return ",".join(lst)


	def deserialize(self, data):
		if len(data) == 0:
			return None
		else:
			lst = data.split(",")
			que = deque()
			[que.append(lst[i]) for i in range(len(lst))]
			return self.deserializeHelper(que)


	def serializeHelper(self, root, lst):
		if not root:
			return ""
		else:
			lst.append(str(root.val))
			lst.append(str(len(root.children)))
			for kid in root.children:
				self.serializeHelper(kid, lst)

	def deserializeHelper(self, que):
		if len(que) > 0:
			val = que.popleft()
			totalKids = int(que.popleft())
			root = Node(int(val), [])
			for i in range(totalKids):
				root.children.append(self.deserializeHelper(que))
			return root
		else:
			return None
    
-------------------------------------------------------------
This is the code for the older requirements. The new requirements of this problem say that after serialization, it should be a string.

Somehow, at the very beginning, I thought it required me to serialize the tree into a string. Later on, I realized a dict or a list was OK, too.
My solution is pretty much like what you could see in a .json file. Very Intuitive.

class Codec:
    def serialize(self, root):
        return {'value': root.val, 'children': [self.serialize(child) for child in root.children]} if root else {}

    def deserialize(self, data):
        return Node(data['value'], [self.deserialize(child) for child in data['children']]) if data else None
      
      
-----------------------------------------------------------------------
ur serializer gives us a result like:

[1, [[3, [[5, []], [6, []]]], [2, []], [4, []]]]
Now, for deserializing we just need recurision to help us out as it did with serializing;
In our funct. we get the root val (k) and then iterate through the nested items:

At every call:
eg: [1, [[3, [[5, []], [6, []]]], [2, []], [4, []]]]
k = 1
for i in [[3, [[5, []], [6, []]]], [2, []], [4, []]]:
    node = Node(k)
	node.children = [helper(x) for x in i]
	                              1
	                            /   \ 
		[3, [[5, []], [6, []]]]       [2, []], [4, []]
		            3                    2        4
				  /   \
			[5,[]]    [6,[]]
			  5          6
		
class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root:
            return ''
        
        def helper(x):
            if x:
                return [[i.val, helper(i)] for i in x.children]
        return [root.val, helper(root)]
        
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None
                
        def helper(vals):
            if not vals:
                return
            k = vals[0]
            for i in vals[1:]:
                node = Node(k)
                node.children = [helper(x) for x in i]
                return node
                    
        return helper(data)
-------------------------------------------------------------------
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root:
            return ""

        res = "{}".format(root.val)
        if root.children:
            res += "["
            for child in root.children:
                res += "{},".format(self.serialize(child))
            res = "{}]".format(res[:-1])
        return res

    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data: return None
        
        """ st -> stack for storing Nodes as they are being deserialized
        """ child_begin -> This is True when the children of the last node in stack need to appended to. If false, it works on the val of the last node in stack
        
        st, child_begin, res = [Node(0, [])], False, None
        for i, elem in enumerate(data):
            if elem.isdigit():
                """ append to children
                if child_begin:
                    if not st[-1].children or data[i - 1] == ',': 
                        st[-1].children.append(Node(0, []))
                    """ this is for tackling situations where the number is more than 1-digit
                    st[-1].children[-1].val = st[-1].children[-1].val * 10 + int(elem)
                else:
                    """ modify node value
                    st[-1].val = st[-1].val * 10 + int(elem)
            
            
            """ append the last child of last element in stack if it exists
            elif elem == "[":
                if st and st[-1].children: 
                    st.append(st[-1].children[-1])
                else: 
                    child_begin = True
            
            """ remove last element whose children were being populated
            elif elem == "]":
                res = st.pop()
                
        res = st.pop() if st else res
        return res
--------------------------------------------------------------
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

'''
Encode: DFS to write a comma separated string. Put an s (start) before children and an e (end) after.
Decode: Turn the input into an iterator. Create a root from the first item and DFS to build children.
'''

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        
        ret = []
        
        def dfs(node):
            if not node:
                return
            ret.append(str(node.val))
            ret.append('s')
            for child in node.children:
                dfs(child)
            ret.append('e')
                
        dfs(root)
                
        return ','.join(ret)
            
        
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None
        
        it = iter(data.split(','))
        
        root = Node(int(next(it)), [])
        
        def dfs(node):
            if next(it) == 's':
                child = next(it)
                while child != 'e':
                    child_node = Node(int(child), [])
                    node.children.append(dfs(child_node))
                    child = next(it)
            return node
        
        return dfs(root)
        
---------------------------------------------------------------
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


# Idea: preorder recursive traversal; add number of children after root val, in order to know when to terminate.
# Example: The example in description is serialized as: "1,3,3,2,5,0,6,0,2,0,4,0"
# Ref: https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/discuss/151421/Java-preorder-recursive-solution-using-queue/169724

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        nodeList = []
        self.serializeHelper(root, nodeList)
        return ','.join(map(str, nodeList))


    def serializeHelper(self, root, nodeList):
        if root is None:
            return
        nodeList.append(root.val)
        nodeList.append(len(root.children))
        for child in root.children:
            self.serializeHelper(child, nodeList)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        if len(data) <= 0:
            return None
        nodeList = data.split(",")
        indexs = [0]
        deserializedData = self.deserializeHelper(nodeList, indexs)
        return deserializedData


    def deserializeHelper(self, nodeList, indexs):
        if indexs[0] == len(nodeList):
            return None
        root = Node(int(nodeList[indexs[0]]), [])
        indexs[0] += 1
        childrenSize = int(nodeList[indexs[0]])
        indexs[0] += 1
        for index in range(childrenSize):
            root.children.append(self.deserializeHelper(nodeList, indexs))
        return root
        
      
      
