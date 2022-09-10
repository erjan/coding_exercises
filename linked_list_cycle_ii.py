'''
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast: break
        else: return None  # if not (fast and fast.next): return None
        while head != slow:
            head, slow = head.next, slow.next
        return head
----------------------------------------------------------------------------------------
def detectCycle(self, head: ListNode) -> ListNode:
	if not head:
		return None

	fast, slow = head, head
	isCycle = False

	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next

		if slow == fast:
			isCycle = True
			break

	if not isCycle:
		return None

	slow = head
	while slow != fast:
		slow = slow.next
		fast = fast.next

	return fast
