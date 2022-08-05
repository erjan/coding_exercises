
'''
Given the head of a linked list, rotate the list to the right by k places.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        tail = head
        l = 1
        while (tail.next):
            tail = tail.next
            l += 1


        k = k % l
            
        tail.next = head
        

        tempNode = head
        for _ in range( l - k - 1 ):
            tempNode = tempNode.next
        
        answer = tempNode.next
        tempNode.next = None
        
        return answer
