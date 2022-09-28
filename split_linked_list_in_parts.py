'''
Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

Return an array of the k parts.
'''


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        # DON'T do following since this makes head become null
        # while head:
        #     length += 1
        #     head = head.next
        
        # calculate the base size and the number of parts contain extra number
        size, extra = length // k, length % k
        
        # create empty list to store split parts
        res = [[] for _ in range(k)]
        
        # use two ptrs to split parts
        prev, cur = None, head
        
        for i in range(k):
            res[i] = cur
            # if this part contains extra number, it has (size+1) number
            for j in range(size + (1 if extra > 0 else 0)):
                prev, cur = cur, cur.next
            if prev: prev.next = None
            extra -= 1
        
        return res
