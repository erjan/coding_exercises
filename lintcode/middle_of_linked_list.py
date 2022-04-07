#Find the middle node of a linked list and return it.



class Solution:
    """
    @param head: the head of linked list.
    @return: a middle node of the linked list
    """
    
    def middle_node(self, head: ListNode) -> ListNode:
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        if nodes:
            return nodes[(len(nodes) - 1) // 2]
