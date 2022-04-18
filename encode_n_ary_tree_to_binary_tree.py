'''
Design an algorithm to encode an N-ary tree into a binary tree and decode the binary tree to get the original N-ary tree. An N-ary tree is a rooted tree in which each node has no more than N children. Similarly, a binary tree is a rooted tree in which each node has no more than 2 children. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that an N-ary tree can be encoded to a binary tree and this binary tree can be decoded to the original N-nary tree structure.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See following example).

For example, you may encode the following 3-ary tree to a binary tree in this way
'''

class Codec:
    def encode(self, root: 'Node') -> TreeNode:
        if not root:
            return
        ans = TreeNode(root.val)
        if root.children:
            children = list(map(self.encode, root.children))
            ans.right = children[0]
            for i in range(len(children)-1):
                children[i].left = children[i+1]
        return ans
        
    def decode(self, data: TreeNode) -> 'Node':
        if not data:
            return
        ans = Node(data.val, [])
        if data.right:
            n = data.right
            while n:
                ans.children.append(self.decode(n))
                n = n.left
        return ans  
      
----------------------------------------------------------------------------
Flatten the tree (both binary and N-ary) into a base_queue then reconstruct it in the necessary form.

class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Node') -> TreeNode:
        if not root: return None
        n_queue = deque([root])
        base_queue = deque()
        while n_queue:
            node = n_queue.popleft()
            if node:
                n_queue.append(None)
                n_queue.extend(node.children)
            base_queue.append(node.val if node else None)
        
        new_root = TreeNode(base_queue.popleft())
        biqueue = deque([new_root])
        while biqueue:
            curnode = biqueue.popleft()
            curnode.left = base_queue.popleft() if base_queue else None
            curnode.right = base_queue.popleft() if base_queue else None
            if curnode.left is not None: 
                curnode.left = TreeNode(curnode.left)
                biqueue.append(curnode.left)
            if curnode.right is not None: 
                curnode.right = TreeNode(curnode.right)
                biqueue.append(curnode.right)
        
        return new_root
        
	
	# Decodes your binary tree to an n-ary tree.
    def decode(self, data: TreeNode) -> 'Node':
        if not data: return None
        n_queue = deque([data])
        base_queue = deque()
        while n_queue:
            node = n_queue.popleft()
            if node:
                base_queue.append(node.val)
                n_queue.extend([node.left, node.right])
            else:
                base_queue.append(None)
        
        new_root = Node(base_queue.popleft(), [])
        base_queue.popleft()
        n_queue = deque([new_root])
        while n_queue:
            parent = n_queue.popleft()
            while base_queue:
                child = base_queue.popleft()
                if child is None: break
                # print(f'parent {parent.val} receives child {child}')
                parent.children.append(Node(child, []))

            n_queue.extend(parent.children)
        
        return new_root
      
-----------------------------------------------------------------------------
The left child of a binary node is the subtree encoding all the children of the corresponding n-ary node.
The right child of a binary node is a chain of the binary root nodes encoding each sibling of the n-ary node.
Hence the root node has no right binary child, because the root has no sibilings.

class Codec:

    def encode(self, root):
        if not root:
            return None

        binary = TreeNode(root.val)                 # create a binary root
        if not root.children:
            return binary

        binary.left = self.encode(root.children[0]) # left child of binary is the encoding of all n-ary children,
        node = binary.left                          #     starting with the first child.
        for child in root.children[1:]:             # other children of n-ary root are right child of previous child
            node.right = self.encode(child)
            node = node.right

        return binary

    def decode(self, data):
        if not data:
            return None

        nary = Node(data.val, [])                   # create n-ary root
        node = data.left                            # move to first child of n-ary root
        while node:                                 # while more children of n-ary root
            nary.children.append(self.decode(node)) # append to list
            node = node.right                       # and move to next child
            
        return nary
-------------------------------------------------------------
   # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Node') -> TreeNode:
        if not root: return None
        
        node = TreeNode(root.val)
        dummy = curr = TreeNode(None)
       
        for head in root.children:
            curr.right = self.encode(head)
            curr = curr.right
        
        node.left = dummy.right
        return node
        

	# Decodes your binary tree to an n-ary tree.
    def decode(self, data: TreeNode) -> 'Node':
        if not data: return None
		
        root = Node(data.val, [])
        child = data.left
        
        while child:
            root.children.append(self.decode(child))
            child = child.right
        
        return root
      
      
