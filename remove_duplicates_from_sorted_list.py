#Given a sorted linked list, delete all duplicates such that each element appear only once.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        big_head = head
        while head:
            #time.sleep(1)
            print(head.val)
            if head.next and head.val == head.next.val:
                head.next = head.next.next

            else:
                head = head.next

        return big_head
    
#RECURSIVE SOLUTION
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        if head.next is not None:

            if head.val == head.next.val:
                temp = head.next.next
                head.next = None
                head.next = temp
                self.deleteDuplicates(head)
            else:
                self.deleteDuplicates(head.next)
        return head
