'''
Given the head of a sorted linked list, delete all nodes
that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
'''

def deleteDuplicates(self, head: ListNode) -> ListNode:
    dummy_head = ListNode(next=head)
    prev, cur = dummy_head, head
    
    while cur and cur.next:
        if cur.val != cur.next.val:
            # If there's no duplicate,
            # move prev and cur one step forward
            prev, cur = cur, cur.next
        else:
            # If there're duplicates,
            # iterate cur to the last duplicate nodes,
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
                
            # and jump over the duplicates
            prev.next = cur.next
            cur = cur.next
    
    return dummy_head.next
  
-----------------------------------------------------------
def deleteDuplicates(self, head: ListNode) -> ListNode:
     # Base case
     if not head or not head.next:
         return head
     
     # Recursive case
     
     # No duplicate in the first part
     if head.next.val != head.val: 
         head.next = self.deleteDuplicates(head.next)
         return head
     
     # Duplicates exist in the first part
     cur = head
     while cur.next and cur.next.val == cur.val:
         cur = cur.next
     return self.deleteDuplicates(cur.next)
