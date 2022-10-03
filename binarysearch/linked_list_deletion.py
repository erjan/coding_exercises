'''
Given a singly linked list node, and an integer target, return the same linked list with all nodes whose value is target removed.
'''

class Solution:
    def solve(self, node, target):
        if node is None:
            return node

        res = self.solve(node.next, target)

        if node.val == target:return res
        node.next = res
        return node
