'''
You are given an array of integers nums and the head of a linked list. Return the head of the modified linked list after removing all nodes from the linked list that have a value that exists in nums.


'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        s = set(nums)
        
        while head and head.val in s:
            head = head.next
        
      
        if not head:
            return None

        prev = head
        curr = head.next
        
        while curr:
            if curr.val not in s:
                prev.next = curr
                prev = curr
            curr = curr.next
        
        prev.next = None
        return head

        
