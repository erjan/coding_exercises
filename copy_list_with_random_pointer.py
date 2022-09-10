'''
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy 
should consist of exactly n brand new nodes, where each new 
node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.
'''
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldCopy = {None:None}
        
        cur = head
        while cur:
            copy = Node(cur.val)
            oldCopy[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = oldCopy[cur]
            copy.next = oldCopy[cur.next] 
            copy.random = oldCopy[cur.random]
            cur = cur.next
        
        return oldCopy[head]
