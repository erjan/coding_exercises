'''
Given a single linked list node, representing a binary number with most significant digits first, return it as an integer.

Constraints

n ≤ 30 where n the number of nodes in node
'''

# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        c = ''
        while node:
            c+= str(node.val)

            node = node.next        
        res = int(c,2)
        print(res)
        return res
        
