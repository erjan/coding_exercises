

'''
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def insert(root, item):
                        
            temp = ListNode(item)
            temp.next = root
            root = temp
            return root
            
            
            
        a = list()
        save = head
        while head:
            a.append(head.val)
            head = head.next
        
        a[k-1] , a[len(a)-k] = a[len(a)-k], a[k-1]        
        
        del head
        root = None
        for i in range(len(a)-1,-1,-1):
            root = insert(root, a[i])
        return root
                
        
------------------------------------------------------
def swapNodes(self, head: ListNode, k: int) -> ListNode:
	first = last = head
	for i in range(1, k):
		first = first.next
		
	null_checker = first 
	while null_checker.next:
		last = last.next
		null_checker = null_checker.next
	first.val, last.val = last.val, first.val
	return head

----------------------------------------------------------------
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
	
	    # Initial State
        slow, fast = head, head
		
		# Phase 1
        for _ in range(k - 1):
            fast = fast.next
        first = fast

        # Phase 2
        while fast.next:
            slow, fast = slow.next, fast.next
		
		# Last
        first.val, slow.val = slow.val, first.val

        return head
        
            
     
