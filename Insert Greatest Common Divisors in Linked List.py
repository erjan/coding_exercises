'''
Given the head of a linked list head, in which each node contains an integer value.

Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.

Return the linked list after insertion.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#my solution
from math import gcd
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        cur = head
        nxt = head.next

        while cur and nxt:
            newnodeval = gcd(cur.val, nxt.val)

            prev = cur
            cur = cur.next

            prev.next = ListNode(newnodeval)
            prev = prev.next
            prev.next = cur
            nxt = nxt.next
        return head

-------------------------------------------------------------------------------------------------
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insert_greatest_common_divisors(head: ListNode) -> ListNode:
    def gcdmaker(a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    p1 = head
    p2 = head.next

    while p1 and p2:
        gcd = ListNode(gcdmaker(p1.val, p2.val))
        gcd.next = p2
        p1.next = gcd
        p1 = p2
        p2 = p2.next

    return head
