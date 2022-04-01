'''

You are given the head of a linked list and two integers m and n.

Traverse the linked list and remove some nodes in the following way:

Start with the head as the current node.
Keep the first m nodes starting with the current node.
Remove the next n nodes
Keep repeating steps 2 and 3 until you reach the end of the list.
Return the head of the modified list after removing the mentioned nodes.

'''

class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        
        node = head
        
        while True:
            for _ in range(m-1):
                if node:
                    node = node.next
                else:
                    return head
                    
            for _ in range(n):
                if node and node.next:
                    node.next = node.next.next
                else:
                    return head
                    
            node = node.next
            
