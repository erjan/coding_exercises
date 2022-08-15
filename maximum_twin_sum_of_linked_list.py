'''
In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.
'''

#my own solution!!!!!!!!!!!

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
            res = list()

            while head:
                res.append(head.val)
                head = head.next

            n = len(res)
            twinsum = list()
            for i in range(n//2):

                twinsum.append(res[i] + res[n-1-i])

            res = max(twinsum)
            return res
          
-----------------------------------------------------------------------------------
#best solution 
def pairSum(self, head: Optional[ListNode]) -> int:
	slow, fast = head, head
	maxVal = 0

	# Get middle of linked list
	while fast and fast.next:
		fast = fast.next.next
		slow = slow.next

	# Reverse second part of linked list
	curr, prev = slow, None

	while curr:       
		curr.next, prev, curr = prev, curr, curr.next   

	# Get max sum of pairs
	while prev:
		maxVal = max(maxVal, head.val + prev.val)
		prev = prev.next
		head = head.next

	return maxVal


----------------------------------------------------------------------------
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def reverse(head):
            prev, curr = None, head
            while curr:
                next_node = curr.next
                curr.next = prev
                prev, curr = curr, next_node
            return prev
        
        slow = head
        fast = head
        
        while fast:
            slow = slow.next
            fast = fast.next.next
        
        first = head
        second = reverse(slow)
        max_so_far = 0
        
        while second:
            summ = first.val + second.val
            max_so_far = max(max_so_far, summ)
            first, second = first.next, second.next
        
        return max_so_far
          
