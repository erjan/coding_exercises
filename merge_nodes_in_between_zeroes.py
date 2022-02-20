'''
You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning and end of the linked list will have Node.val == 0.

For every two consecutive 0's, merge all the nodes lying in between them into a single 
node whose value is the sum of all the merged nodes. The modified list should not contain any 0's.

Return the head of the modified linked list.
'''

#my own solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        l = list()
        while temp:
            cur_sum = 0
            streak = temp
            while streak.val!= 0:
                cur_sum+= streak.val
                streak = streak.next
            if cur_sum != 0:
                l.append(cur_sum)

            temp = streak.next

        temp = head
        for i in range(len(l)):
            temp.val = l[i]
            temp = temp.next

        c = 0
        temp = head
        for i in range(len(l)):
            temp = temp.next
        temp.next = None

        temp = head
        while(temp.next.next != None):
            temp = temp.next

        lastNode = temp.next
        temp.next = None
        lastNode = None

        return head
