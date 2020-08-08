'''
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
'''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return None

        cur = head
        prev = None
        
         
        while cur:
            if cur.val == val:
                if prev is None:
                    
                    cur = cur.next
                    head = cur #this was the catch!!!!!! - looked up in knowledge center channel
                    
                else:
                    cur = cur.next
                    prev.next = cur

            else:
                prev = cur
                cur = cur.next


        return head
    
    
#a bit modified solution:

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return head
        cur = head
        prev = None

        while cur:
            if cur.val == val:
                if prev is None:

                    head = cur.next
                else:
                    prev.next = cur.next
            else:
                prev = cur

            cur = cur.next

        return head
    
    
#recursive solution

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return head

        res = self.removeElements(head.next, val)

        if head.val == val:return res
        head.next = res
        return head


