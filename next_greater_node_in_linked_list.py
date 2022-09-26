'''
You are given the head of a linked list with n nodes.

For each node in the list, find the value of the next
greater node. That is, for each node, find the value of the first node that is next to it and has a strictly larger value than it.

Return an integer array answer where answer[i] is the value of the next greater node of the ith node (1-indexed). If the ith node does not have a next greater node, set answer[i] = 0.
'''

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        # Stack for our operations, we'll keep runs of lower elements here.
        stack = []
		# vals we'll store the vals we take from the ll.
        vals = []
		# Res will be our result array (upto 10k per the question).
        res = [0] * 10000
		# Track the idx we're working through.
        idx = 0
        cur = head
		# While we have vals in our ll.
        while cur:
		    # We check, if we have a stack and the current val > whats on the top of the stack.
            while stack and cur.val > vals[stack[-1]]:
			    # We pop the idx from the stack, assign the idx in our res to = the current val.
                res[stack.pop()] = cur.val
            # Append the cur idx to the stack (we use idxs not values for ease in assigning res + to handle duplicates!).
            stack.append(idx)
			# Updates idx, append val and move to next node.
            idx += 1
            vals.append(cur.val)
            cur = cur.next
         # Return the res for the number of vals we saw.
        return res[:idx]
