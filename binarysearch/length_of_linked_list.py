#Given a singly linked list node, return its length. The linked list has fields next and val.

# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):

        c = 0

        while node:
            c+=1
            node = node.next
        return c
        
        
