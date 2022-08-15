'''
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        cur3 = head
        t = 0
        while cur:
            t += 1
            cur = cur.next
        print('total len is %d' % t)

        if t == 1:
            return None
        if t == 2:
            head.next = None
            return head

        mid = t//2
        i = 0

        while i < mid-1:

            cur3 = cur3.next
            i += 1

        if cur3.next.next is None:
            cur3.next = None

        else:
            cur3.next = cur3.next.next
        return head
        
---------------------------------------------------------------------
def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:  
	if not head.next:
		return head.next

	fast, slow = head.next.next, head

	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next

	slow.next = slow.next.next
	return head
  
---------------------------------------------------------------------------------
class Solution:
  def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head: return head
    if head and not head.next: return None
    
    prev = ListNode(0, head)
    slow = fast = head
    while fast and fast.next:
      prev = slow
      slow = slow.next
      fast = fast.next.next

    prev.next = slow.next
    return head     
