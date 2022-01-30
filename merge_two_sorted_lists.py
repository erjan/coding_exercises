'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''

#Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 is None and list2 is None:
            return None
        
        if list1 is None and list2 is not None:
            return list2
        if list1 is not None and list2 is None:
            return list1
        
        c1 = list1
        c2 = list2
        
        dummy = ListNode(-1)        
        head = dummy
        
        while list1 and list2:
            if list1.val <= list2.val:                
                dummy.next = list1
                list1 = list1.next
                       
            elif list1.val > list2.val:
                dummy.next = list2
                list2 = list2.next
                                             
            dummy = dummy.next
            
        if list1 is None and list2 is not None:            
            dummy.next = list2
        
        elif list1 is not None and list2 is None:
            dummy.next = list1
        
        head = head.next
        return head
        
            
        
        
        
            
        
                
