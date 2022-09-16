'''
You are given the head of a linked list containing unique integer values and an integer array nums that is a subset of the linked list values.

Return the number of connected components in nums where two values are connected if they appear consecutively in the linked list.
'''

Take second example in the description:
liked list: 0->1->2->3->4
I highlighed the subset G in linked list with color red.
The problem is just to count how many red part there are.
One red part is one connected components.
To do this, we just need to count tails of red parts.

  def numComponents(self, head, G):
        setG = set(G)
        res = 0
        while head:
            if head.val in setG and (head.next == None or head.next.val not in setG):
                res += 1
            head = head.next
        return res
      
-----------------------------------------
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        itr=head
        c=0
        s=set(nums)
        while itr:
            if itr.val in s and (itr.next==None or itr.next.val not in s):
                c+=1
            itr=itr.next
        return c
