'''
Given the head of a linked list, return the list after sorting it in ascending order.
'''

class Solution:
    
    def merge(self,left,right):
        
        tail = dummy = ListNode()
        
        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
            
        if left:
            tail.next = left
        if right:
            tail.next = right
        return dummy.next
        
        
    def getMiddle(self, head):
        slow = head
        fast = head.next        
        #finding the middle        
        while fast and fast.next:     
            slow = slow.next
            fast = fast.next.next
        return slow
        
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None
        if head.next is None:
            return head
                
        left = head
        right = self.getMiddle(head)
        
        tmp = right.next
        right.next = None
        right = tmp
        
        left = self.sortList(left)
        right = self.sortList(right)
        
        return self.merge(left,right)
        
        
        
        
        
        
        
