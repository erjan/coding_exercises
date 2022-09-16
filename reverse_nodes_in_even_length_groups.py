'''
You are given the head of a linked list.

The nodes in the linked list are sequentially assigned to non-empty groups whose lengths form the sequence of the natural numbers (1, 2, 3, 4, ...). The length of a group is the number of nodes assigned to it. In other words,

The 1st node is assigned to the first group.
The 2nd and the 3rd nodes are assigned to the second group.
The 4th, 5th, and 6th nodes are assigned to the third group, and so on.
Note that the length of the last group may be less than or equal to 1 + the length of the second to last group.

Reverse the nodes in each group with an even length, and return the head of the modified linked list.
'''

class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        group = 2
        tail = head # tail of previous group
        while tail and tail.next:
            cnt = 1 # actual size of the current group
            cur = tail.next # first node of the current group
            while cur.next and cnt < group:
                cur = cur.next
                cnt += 1
            pre, cur = tail, tail.next
            if cnt % 2 == 0: # if group size is even 
                while cnt and cur:
                    nxt = cur.next
                    cur.next = pre
                    pre = cur
                    cur = nxt
                    cnt -= 1
                first = tail.next # first node of the original group
                first.next = cur
                tail.next = pre
                tail = first
            else:
                while cnt and cur:
                    pre, cur = cur, cur.next
                    cnt -= 1
                tail = pre
            group += 1
        return head
      
-------------------------------------------------------------------------------------------
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return head
        last: Optional[ListNode] = head
        first: Optional[ListNode] = head
        prev: Optional[ListNode] = head
        lastprev: Optional[ListNode] = head
        group: int = 1
        length: int = 1
            
        while last:
            # length += 1
            if length == group:
                if length%2==0:
                    prev.next = last
                    nextG = last.next
                    prev = self.reverse(first,last)
                    prev.next = nextG
                    last = nextG   
                    first = nextG
                    group += 1
                    length = 1
                    continue
                
                first = last.next
                prev = last
                group += 1
                length = 1
                last = last.next
                continue
            length += 1
            lastprev = last
            last = last.next
            
        if (length - 1) != 0 and (length - 1)%2==0:
            prev.next = lastprev
            self.reverse(first,lastprev).next = last
        return head
        
    def reverse(self,first: Optional[ListNode],last: Optional[ListNode]):
        
        # to reverse
        prev: Optional[ListNode] = None
        current: Optional[ListNode] = first
        last: Optional[ListNode] = last.next
        temp: Optional[ListNode]
            
        while (current != last):
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        return first
