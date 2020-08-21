'''
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        
        if head is None or not head.next or not head.next.next:
            return head
        
        stack = list()
        cur = head
        while cur:
            stack.append(cur)
            cur = cur.next

        mid = (len(stack)-1)//2

        cur = head
        while mid > 0:
            cur_node = stack.pop()
            cur_node.next = cur.next
            cur.next = cur_node
            cur = cur_node.next
            mid-=1
        last = stack.pop()
        last.next = None
