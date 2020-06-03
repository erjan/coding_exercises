#Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val  = node.next.val
        node.next = node.next.next
        
        
#stupidiest solution lol! did it myself!
        
