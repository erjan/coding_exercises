'''
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#horrible solution
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        res = []
        l = head
        while l:
            print(l.val)
            res.append(int(l.val))
            l = l.next


        print(res)
        if len(res) % 2 == 0:
            mid = len(res)//2
            lower_half = res[:mid]
            upper_half = res[mid:]
            upper_half = list(reversed(upper_half))
            if lower_half == upper_half:
                return True
            else:
                return False
        else:
            mid = len(res)//2
            lower = res[:mid]
            upper = res[(mid+1):]
            upper = list(reversed(upper))
            if upper == lower:
                return True
            else:
                return False

        return True
