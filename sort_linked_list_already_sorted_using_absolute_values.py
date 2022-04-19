'''
Given the head of a singly linked list that is sorted in non-decreasing order using the absolute values of its nodes, return the list sorted in non-decreasing order using the actual values of its nodes.
 
 '''

class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr.next:
            if curr.val > curr.next.val: # Insert at the head
                temp = curr.next
                curr.next = temp.next
                temp.next = head
                head = temp
            else:
                curr = curr.next
        return head
      
----------------------------------------------------------------------------------
Approach 1: Using an Array. (The dumb way of doing it.)

We're not making use of the fact that the linked-list is sorted in non-decreasing order using absolute values of the nodes.

def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    l1 = []           # Array to store all the node values
    curr = head
    while curr:
        l1.append(curr.val)
        curr = curr.next
    l1 = sorted(l1)
    curr2 = head
    ptr = 0           # pointer to the current index 
    while curr2:      # 2nd iteration
        curr2.val = l1[ptr]
        ptr += 1
        curr2 = curr2.next
    return head
Approach 2: Pointing the -ve nodes to the head / Moving the -ve nodes to the front of the LL

def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    curr = head
    while curr.next:
        if curr.val > curr.next.val:    # we've to move things
            temp = curr.next            # pointer to the -ve node
            curr.next = temp.next       # temp.next is same as curr.next.next
            temp.next = head            # point the -ve node to the head
            head = temp                 # update head
        else:
            curr = curr.next            # move-on
    return head
--------------------------------------------------------------------------------
class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = head, head.next
        while cur:
            if cur.val <= head.val:
                prev.next = cur.next
                cur.next, head = head, cur
                cur = prev.next
            else:
                prev, cur = cur, cur.next
        return head
      
      
---------------------------------------------------------
class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node and node.next:
            if node.next.val < 0:
                new_head = node.next                
                node.next = node.next.next
                new_head.next = head
                head = new_head
            else:
                node = node.next
        return head
  
      
