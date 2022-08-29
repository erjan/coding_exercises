'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        head = ListNode(None)
        
        cur = head
        h = []
        
        for i in range(len(lists)):
            
            if lists[i]:
                heapq.heappush(h, (lists[i].val,i))
                lists[i] = lists[i].next
        
        
        
        while h:
            val,i = heapq.heappop(h)
            cur.next = ListNode(val)
            cur = cur.next
            
            if lists[i]:
                heapq.heappush(h, (lists[i].val,i))
                lists[i] = lists[i].next
        
        return head.next
