
'''
Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Implementation the MyCircularQueue class:

MyCircularQueue(k) Initializes the object with the size of the queue to be k.
int Front() Gets the front item from the queue. If the queue is empty, return -1.
int Rear() Gets the last item from the queue. If the queue is empty, return -1.
boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
boolean isEmpty() Checks whether the circular queue is empty or not.
boolean isFull() Checks whether the circular queue is full or not.
You must solve the problem without using the built-in queue data structure in your programming language. 
'''


class Node:
    def __init__(self, val, prev, next):
        self.val = val
        self.prev = prev
        self.next = next


class MyCircularQueue:
    
    def __init__(self, k: int):
        self.head = None
        self.end = None
        self.size = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.size == 0:
            newnode = Node(value, None, None)
            self.head = newnode
            self.end = newnode
            self.end.next = self.head
            self.head.prev = self.end

            self.size += 1
            return True

        elif self.size != 0 and self.size < self.k:

            newnode = Node(value, None, None)
            self.end.next = newnode
            self.end = self.end.next
            self.end.next = self.head
            self.head.prev = self.end
            self.size += 1
            return True
        elif self.size >= self.k:
            return False


    def deQueue(self) -> bool:
        if self.size != 0 and self.size <= self.k:

            self.head = self.head.next
            self.head.prev = self.end
            self.end.next = self.head
            self.size -= 1
            return True

        else:
            return False

    def Front(self):
        if self.size == 0:
            return -1
        return self.head.val

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        return self.end.val

    def isEmpty(self):
        if self.size == 0:
            return True
        return False

    def isFull(self):
        if self.size >= self.k:
            return True
        return False
      
-------------------------------------------------------------------------------------
class ListNode:
    def __init__(self, value: int):
        self.value = value
        self.next = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.head = self.tail = None
        self.len = 0
        self.limit = k

    def enQueue(self, value: int) -> bool:
        if (self.isFull()):
            return False
        
        if (self.head is None):
            self.tail = self.head = ListNode(value)
            self.len += 1
            return True
        
        self.tail.next = ListNode(value)
        self.tail = self.tail.next
        self.len += 1
        return True

    def deQueue(self) -> bool:
        if (self.isEmpty()):
            return False

        self.head = self.head.next
        self.len -= 1
        return True

    def Front(self) -> int:
        if (self.isEmpty()):
            return -1
        return self.head.value
        
    def Rear(self) -> int:
        if (self.isEmpty()):
            return -1
        return self.tail.value
        

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.limit
    
-----------------------------------------------------------------------
class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.rear, self.front = 0, 0
        self.arr = [None] * self.k

    def inc(self, i: int) -> int:
        return 0 if i >= self.k-1 else i + 1

    def dec(self, i: int) -> int:
        return self.k-1 if i == 0 else i - 1

    def enQueue(self, value: int) -> bool:
        if self.arr[self.rear] == None:
            self.arr[self.rear] = value
            self.rear = self.inc(self.rear)
            return True
        return False

    def deQueue(self) -> bool:
        if self.arr[self.front] == None: return False
        self.arr[self.front] = None
        self.front = self.inc(self.front)
        return True

    def Front(self) -> int:
        if self.arr[self.front] == None: return -1
        return self.arr[self.front]

    def Rear(self) -> int:
        if self.arr[self.dec(self.rear)] == None: return -1
        return self.arr[self.dec(self.rear)]

    def isEmpty(self) -> bool:
        if self.arr[self.front] is None and self.arr[self.rear] is None: return True
        return False

    def isFull(self) -> bool:
        if self.arr[self.front] and self.arr[self.rear]: return True
        return False
