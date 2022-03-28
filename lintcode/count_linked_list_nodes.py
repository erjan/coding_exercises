#Count how many nodes in a linked list.

    def count_nodes(self, head: ListNode) -> int:
        # write your code here
        c = 0
        while head:
            c+=1
            head = head.next
        return c

