'''
Given a non-negative integer represented as a linked list of digits, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list.

 

Example 1:

Input: head = [1,2,3]
Output: [1,2,4]
Example 2:

Input: head = [0]
Output: [1]
'''


Solution 1, reverse and then increase while reversing back
def plusOne(self, head):
    tail = None
    while head:
        head.next, head, tail = tail, head.next, head
    carry = 1
    while tail:
        carry, tail.val = divmod(carry + tail.val, 10)
        if carry and not tail.next:
            tail.next = ListNode(0)
        tail.next, tail, head = head, tail.next, tail
    return head
Solution 2, with pure reverse helper
def plusOne(self, head):
    def reverse(head):
        rev = None
        while head:
            head.next, head, rev = rev, head.next, head
        return rev
    head = node = reverse(head)
    while node.val == 9:
        node.val = 0
        node.next = node = node.next or ListNode(0)
    node.val += 1
    return reverse(head)
If you don't like that bottom while-loop, here's a more normal way I guess:

    while node.val == 9:
        node.val = 0
        if not node.next:
            node.next = ListNode(0)
        node = node.next
-------------------------------------------

Here, we make use of the fact that, in recursion, we return to the previous caller in our stack frame.
So, when we adding, we move to the end of our list, add one(or whatever we want to).
If the val >= 10, we have a carry, which we can simply return to our previous caller and go on.

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        def helper(head):
			#When you reach the last node, add 1 to it, if carry exists, return carry.
            if not head.next:
                carry, head.val = divmod(1 + head.val, 10)
                return carry
            carry = helper(head.next)
            carry, head.val = divmod(carry + head.val, 10)
            return carry
        carry_node = ListNode(1, head)
        if helper(head): return carry_node
        return head
----------------------------------------------

class Solution(object):
    def plusOne(self, head):
        def add(head):
            if not head:
                return 1
            head.val += add(head.next)
            carry, head.val = divmod(head.val, 10)
            return carry
            
        carry = add(head)
        if carry and head:
            addc = ListNode(1)
            addc.next = head
            head = addc
        return head
----------------------------

We are going to solve this problem by using recursion. Our base case is that we have reached the end of the linked list. Because we are going to add one to the number represented by this linked list we are going to return 1, you can think of returning this one as an intial carry over. We add the node value and the carry value and mod it to get the result that we will store in the nodes value. Then we get the carry over of the result of this addition and return it. Once the call to recursice returns, if there is still a carry over then this will be the new head with a value of one and we will link it to the old head and return the new head.

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        def recursive(node):
            if not node:
                return 1
            else:
                carry = recursive(node.next)
                summation = (node.val + carry) % 10
                carry = (node.val + carry) // 10
                node.val = summation
                return carry
            
        carry = recursive(head)
        if carry:
            new_head = ListNode(carry)
            new_head.next = head
            head = new_head
        return head
class Solution {
    public ListNode plusOne(ListNode head) {
        int carry = recursive(head);
        if (carry == 1) {
            ListNode newHead = new ListNode(carry);
            newHead.next = head;
            head = newHead;
        }
        return head;
    }
    
    public int recursive(ListNode node) {
        if (node == null) return 1;
        else {
            int carry = recursive(node.next);
            int summation = (node.val + carry) % 10;
            carry = (node.val + carry) / 10;
            node.val = summation;
            return carry;
        }
    }
}
-----------------------------------------------------------

The code below works in general for any number we'd like to add. We reverse the list, then add the number then reverse it back.
O(1) memory and O(N) time.

def plusOne(self, head: ListNode) -> ListNode:

	def reverse(l):
		prev = None
		while l:
			l.next, prev, l = prev, l, l.next
		return prev

	revhead = reverse(head)
	cur = revhead
	residual = 1  # we can change 1 to something else as well
	while residual:
		residual += cur.val
		cur.val = residual % 10
		residual //= 10
		if residual and not cur.next: cur.next = ListNode()
		cur = cur.next

	return reverse(revhead)
------------------------------------------------------------------------

This question is similar to Add 2 Numbers.

Solution 1 (With a Sentinel Node): Reverse => Add => Reverse

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
		if not head:
			return head
	
		# reverse linked list
		prev_node, curr_node = None, self._reverse_helper(head)
		result = dummy_node = ListNode(0)
		carry_over = 0
	
		while curr_node:
			sum_ = curr_node.val + carry_over
			sum_ = sum_ + 1 if prev_node is None else sum_

			dummy_node.next = ListNode(sum_ % 10)
			carry_over = sum_ // 10

			# move along
			prev_node, curr_node, dummy_node = curr_node, curr_node.next, dummy_node.next

		if carry_over:
			dummy_node.next = ListNode(carry_over)

		return self._reverse_helper(result.next)
	
	
	# helper method to reverse linked-list
	def _reverse_helper(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev
	
Solution 2 (Without a Sentinel Node): Reverse => Add

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
		if not head:
			return head
	
		# reverse linked list
		prev_node, curr_node = None, self._reverse_helper(head)
		result, dummy_node = None, None
		carry_over = 0
		
		while current_node:
            sum_ = current_node.val + carry_over
            sum_ = sum_ + 1 if previous_node is None else sum_
			
			dummy_node = ListNode(sum_ % 10)
            carry_over = sum_ // 10
			
			# add the dummy_node to the front of result
            dummy_node.next = result
            result = dummy_node
            
            # move along
            current_node, previous_node = current_node.next, current_node
			
		if carry_over:
            dummy_node = ListNode(carry_over)
            dummy_node.next = result
            result = dummy_node
            
        return result
		
		
	# helper method to reverse linked-list
	def _reverse_helper(self, head: ListNode) -> ListNode:
		prev, curr = None, head
		while curr:
			curr.next, prev, curr = prev, curr, curr.next
		return prev
-----------------------------------------------------------------------------------------------  
  


      
      
        
