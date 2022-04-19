'''
Given the root of a binary tree, return the number of uni-value subtrees.

A uni-value subtree means all nodes of the subtree have the same value.
'''

def countUnivalSubtrees(self, root):
    self.count = 0
    self.checkUni(root)
    return self.count

# bottom-up, first check the leaf nodes and count them, 
# then go up, if both children are "True" and root.val is 
# equal to both children's values if exist, then root node
# is uniValue suntree node. 
def checkUni(self, root):
    if not root:
        return True
    l, r = self.checkUni(root.left), self.checkUni(root.right)
    if l and r and (not root.left or root.left.val == root.val) and \
    (not root.right or root.right.val == root.val):
        self.count += 1
        return True
    return False
  
  ----------------------------------------------------------
  
  # this question is as simple as....
"""
1. How do you calculate the total unival subtrees? 
	a. You add the ones on the left to the ones on the right and add the root if it is unival too.
2. How do you determine if a subtree is unival?
	1. if recurse through all the nodes in the tree and arive at a null then we are at a leaf. Leafs are by default unival, so return true. 
	2. if we have a right subtree and it's root node value isnt the same as our current root value then it is not a unival subtree 
		so return false
	3. same as number 2 but for left subtree
	4. if the curr node has both left and right that are unival subtrees and we know that the rootval matches the left and right 
		child vals then we have a unival subtree.

Now, just put 1 & 2 together by callig the respective functions recursively
"""

class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if not root:
            return 0
        
		# the total count will equal the total count of the left subtree and the total count of the right subtree
        total_count = self.countUnivalSubtrees(root.left) + self.countUnivalSubtrees(root.right)
        
		#but, if the left and right subtrees are also unival then we need to add the root if it is unival too!
        if self.isUniVal(root.left) and self.isUniVal(root.right):
            if self.isUniVal(root):
                total_count += 1
        
        return total_count
        
    
    def isUniVal(self, root):
		# it is a leaf, so it is unival
        if not root:
            return True
        
        if root.right and root.right.val != root.val:
            return False
        
        if root.left and root.left.val != root.val:
            return False
        
		#order matters here, we also know that root.val must be equal to left and right because we just checked it above
        if self.isUniVal(root.left) and self.isUniVal(root.right):
            return True
   
  
  ------------------------------------------------------------------------
  
  
  Each node is either a leaf or the root of a subtree. The set of values in a given subtree is the union of three sets:

The set of values of its left subtree.
The set of values of its right subtree
The set consisting only of the subtree's root.
Once we get the union of the three sets, we simply check that its length is equal to 1 in order to know if the subtree is a univalue or not. If this is the case, we increment the count.

def countUnivalSubtrees(self, root: TreeNode) -> int:
    self.count = 0
    
    def dfs(node, acc):
        if not node:
            return acc
        left = dfs(node.left, acc)
        right = dfs(node.right, acc)
        acc = left.union(right)
        acc.add(node.val)
        self.count += (len(acc) == 1)
        
        return acc
    
    dfs(root, set())
    
    return self.count
  
  ----------------------------------------------------------------------------------
  
  I don't like the accepted solution because it is using an instance variable to keep count. Although it is more readable, I believe a cleaner way is to not have shared state across instance and this is what I have done.

def countUnivalSubtrees(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    # at any point if you know two things:
    # 1) count of univalue subtrees from its left descendants and if its a univalue subtree
    # 2) count of univalue subtrees from its right descendants and if its a univalue subtree
    # Then you can easily calculate outcome of the current level
    
    # count to return will atleast be sum of 1) and 2) 
    
    # Only two possible scenarios for the current level:
    # 1) Add +1 to count and return True if both left/(and)right subtrees are univalue and value of left,right and current level is the same i.e. it is a univalue subtreee
    # 2) keep count same and return False if the current level is not a univalue subtree 
    
    # just handle some corner cases and we are done
    
    def count_subtree(root):
        """
        return: count, boolean indicating if its a univalue subtree
        """
        if not root:
            return 0, False
        
        if not root.left and not root.right:
            return 1, True
        
        left_count, left_is_univalue = count_subtree(root.left)
        
        right_count, right_is_univalue = count_subtree(root.right)
        
        
        if root.left and root.right: 
            if left_is_univalue and right_is_univalue:
                if root.left.val == root.right.val == root.val:
                    return left_count + right_count + 1, True
        elif root.left and left_is_univalue:
            if root.left.val == root.val:
                return left_count + right_count + 1, True
        elif root.right and right_is_univalue:
            if root.right.val == root.val:
                return left_count + right_count +1 , True

        return left_count + right_count, False
    
    
    count, is_uni = count_subtree(root)
    return count
  ---------------------------------------------------------------------
  
  The idea is that the following conditions result in the increment of the result counter:

The node is a leaf (has no children)
The node and it's children have the same value
The node completes a tree recursively
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        
        self.count = 0
        
        def hasChildren(node):
            
            if node.left or node.right:
                return True
            
            return False
        
        def isUniValSubTree(node):
            
            if node is None:
                return True
            
            if not hasChildren(node):
                self.count += 1
                return
                
            if node.left and node.right:
                if node.left.val == node.right.val and node.left.val == node.val:
                    self.count += 1
            elif node.left and not node.right:
                if node.left.val == node.val and not hasChildren(node.left):
                    self.count += 1
            elif node.right and not node.left:
                if node.right.val == node.val and not hasChildren(node.right):
                    self.count += 1
            
            isUniValSubTree(node.left)
            isUniValSubTree(node.right)
            
        isUniValSubTree(root)
        return self.count
      
      
  
