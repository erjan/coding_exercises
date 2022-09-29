'''
Given a binary tree root and a linked list with head as the first node. 

Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.

In this context downward path means a path that starts at some node and goes downwards.
'''

class Solution(object):
    def isSubPath(self, head, root):
        if not root:    
            return False
        if self.issame(head, root):
            return True
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
    def issame(self, head, root):
        if not head:
            return True
        if not root:
            return False
        if head.val != root.val:
            return False
        return self.issame(head.next, root.left) or self.issame(head.next, root.right)
      
-----------------------------------------------------------------------------------------------
class Solution(object):
	def dfs(self, head, root):
		if not head:
			return True

		if not root:
			return False

		if head.val == root.val:
			return self.dfs(head.next, root.left) or self.dfs(head.next, root.right) 

		return False


	def isSubPath(self, head, root):
		"""
		:type head: ListNode
		:type root: TreeNode
		:rtype: bool
		"""
		if not head:
			return True
		if not root:
			return False
		if self.dfs(head, root):
			return True
		return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
