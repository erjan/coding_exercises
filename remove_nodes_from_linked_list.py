'''
You are given the head of a linked list.

Remove every node which has a node with a strictly greater value anywhere to the right side of it.

Return the head of the modified linked list.
'''

def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(n: ListNode) -> ListNode:
            tail = None
            while n:
                nxt = n.next
                n.next = tail
                tail = n
                n = nxt
            return tail

        cur = tail = reverse(head)
        mx = cur.val
        while cur.next:
            if cur.next.val < mx:
                cur.next = cur.next.next
            else:
                cur = cur.next
                mx = cur.val
        return reverse(tail)
      
----------------------------------------------------------------------
    def removeNodes(self, head):
        if not head: return None
        head.next = self.removeNodes(head.next)
        if head.next and head.val < head.next.val:
            return head.next
        return head
      
      
----------------------------------------------------------------------------------------
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(inf)
        stack = [dummy]
        
        while head:
            while stack and head.val > stack[-1].val:
                stack.pop()
            stack[-1].next = head
            stack.append(head)
            head = head.next
        
        return dummy.next
