'''
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(0,head)
        
        groupPrev = dummy
        
        while True:
            kth = self.getKth(groupPrev,k)
            if not kth:
                break
            
            groupNext = kth.next
            #reversing the group
            prev,cur = kth.next, groupPrev.next
            while cur!= groupNext:
                tmp = cur.next
                cur.next= prev
                prev = cur
                cur = tmp
                
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
            
        return dummy.next
            
    
    def getKth(self, cur,k):
        while cur and k > 0:
            cur = cur.next
            k = k-1
        return cur
        
