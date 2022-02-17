#Given the head of a linked list, remove the nth node from the end of the list and return its head.

#my own solution.. quite bad

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def removeNthFromEnd(self, head,  n: int):
        l = 0
        t = head
        while t:
            t = t.next
            l += 1
        #print('length of list : %d' % l)

        #l = l - n
        #print('from the right we need to go %d nodes' % (l-n))
        if (l-n) == 0:
            head = head.next
            return head
        prev = head
        prev2 = head.next
        if n == 1:
            temp = head
            while(temp.next.next != None):
                temp = temp.next
            lastNode = temp.next
            temp.next = None
            lastNode = None
            return head

        l = l - n
        cur = head
        for i in range(l):
            if i == l - 1:
                prev = cur
                cur = cur.next.next
                prev.next = cur
                cur = None
                return head

            cur = cur.next

            
#adding another better solution

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        # use dummy head will make the removal of head node easier
        dummy_head = ListNode(-1)
        dummy_head.next = head
        
        # cur keeps iteration till the end
        # prev_of_removal traverses to the previous node of the one of being removed
        cur, prev_of_removal = dummy_head, dummy_head
        
        
        while cur.next != None:
            
            # n-step delay for prev_of_removal
            if n <= 0:
                prev_of_removal = prev_of_removal.next
                
            cur = cur.next
            
            n -=1
        
        
        # Remove the N-th node from end of list
        n_th_node = prev_of_removal.next
        prev_of_removal.next = n_th_node.next
        
        del n_th_node
        
        return dummy_head.next
    
