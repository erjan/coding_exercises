'''
Design your implementation of the circular double-ended queue (deque).

Implement the MyCircularDeque class:

MyCircularDeque(int k) Initializes the deque with a maximum size of k.
boolean insertFront() Adds an item at the front of Deque. Returns true if the operation is successful, or false otherwise.
boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is successful, or false otherwise.
boolean deleteFront() Deletes an item from the front of Deque. Returns true if the operation is successful, or false otherwise.
boolean deleteLast() Deletes an item from the rear of Deque. Returns true if the operation is successful, or false otherwise.
int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty.
int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
boolean isEmpty() Returns true if the deque is empty, or false otherwise.
boolean isFull() Returns true if the deque is full, or false otherwise.
'''


class MyCircularDeque:

    def __init__(self, k: int):
        self.cdq = []*k
        self.size = k

    def insertFront(self, value: int) -> bool:
        if len(self.cdq) < self.size:
            self.cdq.insert(0,value) 
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if len(self.cdq) < self.size:
            self.cdq.insert(self.size-1,value)
            return True
        
        return False

    def deleteFront(self) -> bool:
        if len(self.cdq) ==0:
            return False
        
        del self.cdq[0]
        return True

    def deleteLast(self) -> bool:
        if len(self.cdq) ==0:
            return False
        
        del self.cdq[-1] 
        return True
        
        del self.cdq[0]

    def getFront(self) -> int:
        if len(self.cdq) ==0:
            return -1
        
        return self.cdq[0]
        
    def getRear(self) -> int:
        if len(self.cdq) ==0:
            return -1
        
        return self.cdq[-1]
        

    def isEmpty(self) -> bool:
        return len(self.cdq) <= 0

    def isFull(self) -> bool:
        return len(self.cdq) == self.size
      
----------------------------------------------------------------------------------
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyCircularDeque:
    def __init__(self, k: int):
        self.head = None
        self.last = None
        self.size = k

    def insertFront(self, value: int) -> bool:
        if not self.size: return False
        new_node = Node(value)
        if not self.head: 
            self.head = new_node
            self.last = self.head
        else: 
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size -= 1
        return True

    def insertLast(self, value: int) -> bool:
        if not self.size: return False
        new_node = Node(value)
        if not self.head: 
            self.head = new_node
            self.last = self.head
        else: 
            self.last.next = new_node
            new_node.prev = self.last
            self.last = new_node
        self.size -= 1
        return True

    def deleteFront(self) -> bool:
        if not self.head: return False
        if not self.head.next: 
            self.head = None
            self.last = None
        else: 
            next_node = self.head.next
            self.head.next = None
            next_node.prev = None
            self.head = next_node
        self.size += 1
        return True

    def deleteLast(self) -> bool:
        if not self.head: return False
        if not self.head.next:
            self.head = None
            self.last = None
        else:
            prev_node = self.last.prev
            self.last.next = None
            self.last.prev = None
            prev_node.next = None
            self.last = prev_node
        self.size += 1
        return True

    def getFront(self) -> int:
        if self.head: return self.head.val
        return -1

    def getRear(self) -> int:
        if self.last: return self.last.val
        return -1

    def isEmpty(self) -> bool:
        return True if not self.head else False

    def isFull(self) -> bool:
        return True if not self.size else False
