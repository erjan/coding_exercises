'''
Given a linked list, swap every two adjacent 
nodes and return its head. You must solve the problem without modifying the values 
in the list's nodes (i.e., only nodes themselves may be changed.)
'''


# Iteratively
def swapPairs1(self, head):
    dummy = p = ListNode(0)
    dummy.next = head
    while head and head.next:
        tmp = head.next
        head.next = tmp.next
        tmp.next = head
        p.next = tmp
        head = head.next
        p = tmp.next
    return dummy.next
 
# Recursively    
def swapPairs(self, head):
    if head and head.next:
        tmp = head.next
        head.next = self.swapPairs(tmp.next)
        tmp.next = head
        return tmp
    return head
