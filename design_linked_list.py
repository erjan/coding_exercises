'''

Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.

'''



# Singly LinkedList
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or index > self.length-1:
            return -1
        else:
            node = self.head
            if node:
                for _ in range(index):
                    node = node.next
                return node.val
            else:
                return -1
 
    def addAtHead(self, val: int) -> None:
        node = Node(val, self.head)
        self.head = node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        tail = Node(val)
        node = self.head   
        if node:
            for _ in range(self.length-1):
                node = node.next
            node.next = tail
        else:
            self.head = tail        
        
        self.length += 1 
  
    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return
        elif index == 0:
            self.addAtHead(val)
        else:
            node = self.head
            if node:
                for _ in range(index-1):
                    node = node.next
                new_node = Node(val, node.next)
                node.next = new_node
            else:
                return
            
        self.length += 1    
 
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index > self.length-1:
            return
        elif index == 0:
            self.head = self.head.next 
        else:
            node = self.head
            if node:
                for _ in range(index-1):
                    node = node.next
                node.next = node.next.next
            else:
                return
        
        self.length -= 1

###########################################################

# Doubly LinkedList
class Node:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
        
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0
        
    def get(self, index: int) -> int:
        if index < 0 or index > self.length-1:
            return -1
        else:
            node = self.head
            if node:
                for _ in range(index):
                    node = node.next
                return node.val
            else:
                return -1

    def addAtHead(self, val: int) -> None:
        new_head = Node(val, None, self.head)
        self.head = new_head
        self.length += 1        

    def addAtTail(self, val: int) -> None:
        tail = Node(val)
        node = self.head
        if node:
            for _ in range(self.length-1):
                node = node.next
            node.next = tail
            tail.prev = node
        else:
            self.head = tail
            
        self.length += 1  
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return
        elif index == 0:
            self.addAtHead(val)
        else:
            node = self.head
            if node:
                for _ in range(index-1):
                    node = node.next
                new_node = Node(val, node, node.next)
                node.next = new_node
            else:
                return
       
        self.length += 1
    
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index > self.length-1:
            return
        elif index == 0:
            self.head = self.head.next 
        else:
            node = self.head
            if node:
                for i in range(index-1):
                    node = node.next
                node.next = node.next.next
            else:
                return
        
        self.length -= 1
