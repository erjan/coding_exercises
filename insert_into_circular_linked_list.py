'''

Given a Circular Linked List node, which is sorted in ascending order, write a function to insert a value insertVal into the list such that it remains a sorted circular list. The given node can be a reference to any single node in the list and may not necessarily be the smallest value in the circular list.

If there are multiple suitable places for insertion, you may choose any place to insert the new value. After the insertion, the circular list should remain sorted.

If the list is empty (i.e., the given node is null), you should create a new single circular list and return the reference to that single node. Otherwise, you should return the originally given node.
'''


def insert(self, head: 'Node', insertVal: int) -> 'Node':
    if head is None:
        head = Node(insertVal)
        head.next = head
        return head
    
    if head.next == head:
        head.next = Node(insertVal, head)
        head.next.next = head
        return head
    
    temp = head
    newNode = Node(insertVal)
    while True:
        currVal = temp.val
        nextVal = temp.next.val
        
        if nextVal > currVal and insertVal >= currVal and insertVal <= nextVal:
            newNode.next = temp.next
            temp.next = newNode
            return head
        
        if nextVal < currVal and (insertVal >= currVal or insertVal <= nextVal):
            newNode.next = temp.next
            temp.next = newNode
            return head
        
        temp = temp.next
        if temp == head:
            head.next = Node(insertVal, head.next)
            return head
          
          
------------------------------------------------------------

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        #edge cases
        if not head:
            node = Node(insertVal)
            node.next = node
            return node
                
        curr = head
        while curr.next != head:
            #insert in the normal position
            if curr.val <= insertVal <= curr.next.val:
                break
            #insert in the link position
            if curr.val > curr.next.val and (curr.val <= insertVal or insertVal <= curr.next.val):
                break
            curr = curr.next
        
        #insert new nodes
        insert_node = Node(insertVal, next=curr.next)
        curr.next = insert_node
    
        return head
