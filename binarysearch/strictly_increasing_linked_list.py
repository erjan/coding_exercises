'''
Given the head of a singly linked list head, return whether the values of the nodes are sorted in a strictly increasing order.

Constraints

1 ≤ n ≤ 100,000 where n is the number of nodes in head
'''

# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, head):

        temp = list()
        while head:
            temp.append(head.val)
            head = head.next

        for i in range(len(temp)-1):

            if temp[i] >= temp[i+1]:
                return False
        return True
        
